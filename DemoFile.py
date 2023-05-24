# DemoFile.py 
#파일 쓰기
f = open("c:\\work\\demo.txt", "wt")
f.write("하나\n둘\n세번째\n")
f.close()

#파일 읽기 
f = open(r"c:\work\demo.txt", "rt")
result = f.read()
print( result )
#다시 처음으로 리셋(파일포인터)
f.seek(0)
#코드로 보정 
print( f.readline(), end="" )
print( f.readline(), end="" )
#다시 처음
f.seek(0)
lst = f.readlines() 
print(lst)

f.close()


