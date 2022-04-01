import os
from courses import courses
x=[]
x = dir(os)
for item in x:
    print(item)

"Get list of files in cwd."
print(os.__file__)
my_files=[]
my_files=os.listdir(os.getcwd())
for file in my_files:
    print(file)

" Generate file names in a directory tree."
cwd=os.getcwd()
# Store files in list.
list=[]
#dirs=directories
for(root,dirs,file) in os.walk(cwd):
    for f in file:
        if '.py' in f:
            print('file = ', f)

print('cwd = ', os.getcwd())
print('abspath = ', os.path.abspath(cwd))
print ('os.path.dirname = ', os.path.dirname(cwd))
print ('os.path.relpath = ', os.path.relpath(cwd))

print(os.listdir())