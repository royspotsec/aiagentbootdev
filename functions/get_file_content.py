import sys, os
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    try:
        abspath = os.path.abspath(working_directory)
        combinedpath = os.path.join(abspath,file_path)
        target_dir  = os.path.normpath(combinedpath)
        path_list = [abspath, target_dir]
        valid_target_dir=os.path.commonpath(path_list) == abspath
        if valid_target_dir is False :
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_dir,"r") as file :
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        
        
        return content
    except Exception as e :
        return f"Error:{e}"




#os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# os.path.normpath(): Normalize a path (handles things like ..)
# os.path.commonpath(): Get the common sub-path shared by multiple paths
# os.path.isfile(): Check if a path points to an existing regular file
# open(): Open a file for reading or writing
# .read(): Read a text file to a string, optionally specifying a maximum number of characters
# Example of reading up to a certain number of characters from a text file:

# MAX_CHARS = 10000

# with open(file_path, "r") as f:
#     file_content_string = f.read(MAX_CHARS)
