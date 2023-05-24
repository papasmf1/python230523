# DemoOS.py 
from os.path import * 

print( abspath("python.exe") )
print( basename("c:\\work\\demo.txt") )

if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일이 없습니다.")

import os 

print("운영체제:{0}".format(os.name))

import glob 

result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)

    
