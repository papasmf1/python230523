# db2.py 
import sqlite3

#연결객체를 생성(물리적인 DB파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")
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

#수정
cur.execute("update PhoneBook set name='이길동', PhoneNum='010-899' " +
    " where id=1;")
#삭제
cur.execute("delete from PhoneBook where id=2;")

#검색
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )

#작업을 정상적으로 완료
con.commit()