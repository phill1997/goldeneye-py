


import os
path = "/home/ec2-user/environment/goldeneye-py"

fun = lambda x : os.path.isfile(os.path.join(path,x))
files_list = filter(fun, os.listdir(path))

size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]    
    
for f,s in size_of_file:
    print("{} : {}MB".format(f, round(s/(1024*1024),3)))