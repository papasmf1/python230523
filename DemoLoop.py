# DemoLoop.py 
value = 5 
while value > 0:
    print(value)
    value -= 1 

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

d = {"apple":100, "orange":200, "kiwi":300}
for k,v in d.items():
    print(k,v)

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

print("---수열함수---")
print( list(range(10)) )
print( list(range(2000,2024)) )
print( list(range(1,32)) )

lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )
tp = ("apple","kiwi","orange")
print( [len(i) for i in tp] )
d = {100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()] )

lst = [10, 25, 30]
iterL = filter(None, lst)
for i in iterL:
    print("item:{0}".format(i))

print("---필터링---")    

def getBiggerThan20(i):
    return i > 20 

iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print("item:{0}".format(i))

print("---람다함수---")
iterL = filter(lambda x:x>20, lst)
for i in iterL:
    print("item:{0}".format(i))


