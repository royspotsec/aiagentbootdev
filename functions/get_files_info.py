import sys, os
from google.genai import types
def get_files_info(working_directory, directory="."):
    try:
        abspath = os.path.abspath(working_directory)
        combinedpath = os.path.join(abspath,directory)
        target_dir  = os.path.normpath(combinedpath)
        path_list = [target_dir, abspath]
        valid_target_dir=os.path.commonpath(path_list) == abspath
        if valid_target_dir is False :
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        file_listed = os.listdir(target_dir)
        result = []
        for file in file_listed :
            file_path = os.path.join(target_dir,file)
            if os.path.isdir(file_path):
                is_dir=True
            else:
                file_name = file
                is_dir  = False
            file_size = os.path.getsize(file_path)
            info_string = f"- {file}: file_size={file_size}, is_dir={is_dir}"
            result.append(info_string)
        return "\n".join(result)
    except Exception as e :
        return f"Error: {e}"
schema_get_files_info = types.FunctionDeclaration(
            name="get_files_info",
            description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "directory": types.Schema(
                        type=types.Type.STRING,
                        description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                    ),
                },
            ),
        )
# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# os.path.normpath(): Normalize a path (handles things like ..)
# os.path.commonpath(): Get the common sub-path shared by multiple paths
# os.listdir(): List the contents of a directory
# os.path.isdir(): Check if a path points to an existing directory
# os.path.isfile(): Check if a path points to an existing regular file
# os.path.getsize(): Get the size of a file (in bytes)
# .join(): Join a list of strings together with a given separator 