# DemoStr.py 
strA = "python is very powerful"
strB = "파이썬은 강력해"
print( len(strA) )
print( len(strB) )
print( strA.capitalize() )
print( strA.startswith("py") )
print( strA.endswith("ful") )
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

u = "<<<  spam and ham >>>"
result = u.strip("<> ") 
print(u)
print(result)
result = result.replace("spam", "spam egg")
print(result)

lst = result.split()
print(lst)
print( ":)".join(lst) )

#정규표현식을 사용할 경우 
import re 

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
#블럭 선택 주석: ctrl + / 
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())
#연도 
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
#우편번호 
result = re.search("\d{5}", "우리 동네는 54000입니다.")
print(result.group())
