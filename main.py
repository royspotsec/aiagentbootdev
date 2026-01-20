import os
import argparse
from dotenv import load_dotenv
from config import *
from google import genai
from google.genai import types
from prompts import *
from functions.call_function import *
import sys
from google.genai import errors



def main():

    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    done = False
    if api_key == None:
        raise RuntimeError ("You need to set the API")
        
    client = genai.Client(api_key=api_key)
    for _ in range(MAX_ITERS):
    
                
        # Now we can access `args.user_prompt`
       
        response = client.models.generate_content(
            model='gemini-2.5-flash', contents=messages , config=types.GenerateContentConfig( tools=[available_functions],system_instruction=system_prompt),

        )
        if response.candidates :
            for candidate in response.candidates:
                messages.append(candidate.content)
        if response.usage_metadata == None :
            raise RuntimeError ("Runtime error")


        if args.verbose :
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


        if not response.function_calls:
            print("Final response:")
            print(response.text)
            done = True
            break 
        

        function_responses = []
        
        for function_call in response.function_calls:
            
            function_call_result = call_function(function_call, args.verbose)   
            if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
            or not function_call_result.parts[0].function_response.response
            ):
                raise RuntimeError(f"Empty function response for {function_call.name}")
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
        messages.append(types.Content(role="user",parts=function_responses))        
    if not done:
        sys.exit(1)

    
if __name__ == "__main__":
    main()












