import os

relative_path = './module_debug/path.py'
absolute_path =  os.path.abspath(relative_path)

print(absolute_path)

curr_dir = os.path.dirname(os.path.abspath(__file__))
print(curr_dir)