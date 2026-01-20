import sys,os
from google.genai import types



def write_file(working_directory, file_path, content):
    abspath = os.path.abspath(working_directory)
    combinedpath = os.path.join(abspath,file_path)
    target_dir  = os.path.normpath(combinedpath)
    path_list = [abspath, target_dir]
    valid_target_dir=os.path.commonpath(path_list) == abspath
    if valid_target_dir is False :
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if  os.path.isdir(target_dir):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    with open (target_dir,"w") as file :
        file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    raise Exception ("Error:f'not Successfully didn't write to {file_path}")

schema_write_file = types.FunctionDeclaration(
            
            
            name="write_file",
            description="write file in a specified directory relative to the working directory, writing in the file",
            parameters=types.Schema(
                required=["file_path","content"],
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="its the file path of the file",
                    ),
                    "content": types.Schema(
                        type=types.Type.STRING,
                        description="the content of the user",
                    ),
            },
            ),
        )

