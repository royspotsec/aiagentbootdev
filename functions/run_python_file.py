import sys,os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abspath = os.path.abspath(working_directory)
        combinedpath = os.path.join(abspath,file_path)
        target_dir  = os.path.normpath(combinedpath)
        path_list = [abspath, target_dir]
        valid_target_dir=os.path.commonpath(path_list) == abspath
        if valid_target_dir is False :
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_dir.endswith ('py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args is not None :
            command.extend(args)
        result =subprocess.run(command,capture_output=True,text=True,timeout=30) 
        message = []
        if result.returncode != 0 :
            message.append(f"Process exited with code {result.returncode}")
        
        if len(result.stdout.strip()) ==0 and len(result.stderr.strip()) ==0:
            message.append("No output produced")
        if len(result.stdout.strip())>0 :
            message.append(f"STDOUT:{result.stdout}")
        if len(result.stderr.strip())>0 :
            message.append(f"STDERR:{result.stderr}")
        return "\n".join(message)
    except Exception as e :
        return "Error: executing Python file: {e}"
schema_run_python_file = types.FunctionDeclaration(
            
            
            name="run_python_file",
            description="run python file in the working directory",
            parameters=types.Schema(
                required=["file_path"],
                type=types.Type.OBJECT,
                properties={
                    "args": types.Schema(
                        type=types.Type.ARRAY,
                        description="an array",
                        items = types.Schema(
                            type=types.Type.STRING,
                        ),
                    ),
                    
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="its the file path",
                        
                    ),
                },
            ),
        )
