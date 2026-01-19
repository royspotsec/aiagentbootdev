import sys, os
from functions.get_file_content import get_file_content
result = get_file_content("calculator", "lorem.txt")
print (len(result))
result =get_file_content("calculator", "main.py")
print(result)
result =get_file_content("calculator", "pkg/calculator.py")
print(result)
result =get_file_content("calculator", "/bin/cat") #(this should return an error string)
print(result)
result =get_file_content("calculator", "pkg/does_not_exist.py") #(this should return an error string)
print(result)