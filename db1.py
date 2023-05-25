# db1.py 
import sqlite3

#연결객체를 생성(일단은 메모리에 생성해서 연습)
con = sqlite3.connect(":memory:")
#커서객체를 리턴
cur = con.cursor() 
#테이블 구조 생성
cur.execute("create table if not exists PhoneBook " + 
    " (id integer primary key autoincrement, name text, phoneNum text);")

#1건 입력 
cur.execute("insert into PhoneBook (name, phoneNum) values " +
    " ('홍길동','010-111');")

#파라메터 입력
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values " +
    " (?, ?);", (name, phoneNumber) )

#여러개의 레코드 입력
datalist = (("박문수","01-123"), ("김길동","010-567"))
cur.executemany("insert into PhoneBook (name, phoneNum) values " +
    " (?, ?);", datalist )

#검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print( cur.fetchone() )

print("---fetchmany(2)---")
print( cur.fetchmany(2) )

print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )
