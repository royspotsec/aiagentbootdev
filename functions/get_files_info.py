from os import *
def get_files_info(working_directory, directory="."):
    abspath = os.path.basename(working_directory)
    combinedpath = os.path.join(abspath,directory)
    target_dir  = os.path.normpath(combinedpath)
    valid_target_dir=os.path.commonpath(target_dir,working_directory) == abspath
    if valid_target_dir is False :
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'


    

