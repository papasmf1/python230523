# function2.py 
#가변인자를 사용
def union(*ar):
    #지역변수 
    result = []
    #단어를 짤라서 사용 
    for item in ar:
        #글자를 짤라서 사용
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )


print( globals() )

#이름이 없는 간단한 함수 정의(람다 함수)
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )
print( (lambda x:x*x)(3) )

print( globals() )
