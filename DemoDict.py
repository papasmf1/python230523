# DemoDict.py 
#딕셔너리(사전식) 무조건 키중심 
device = {"아이폰":5, "아이패드":10, "윈도우":15}
#디버깅할 때 중단점(Break Point)
for item in device.items():
    print(item)

print( device["아이폰"] )
device["맥북"] = 20 
device["아이폰"] = 6 
print( device )
del device["아이폰"]
print( device )

#참조 복사(전달)
phone = {"kim":"111", "lee":"222", "park":"333"}
print( "kim" in phone )
print( "moon" not in phone )
p = phone 
p["kang"] = "123"
print(p)
print(phone)
print( id(phone), id(p) )

isRight = True 
print(isRight)
print( 1 < 2 )
print( 1 != 2 )
print( 1 == 2)
print( True and True and False )
print( True and True and True )
print( True or False or False )




