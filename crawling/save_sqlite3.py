# SQLite3에 저장하기
import sqlite3

conn = sqlite3.connect('top_cities.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')

c.execute('''
    CREATE TABLE cities(
        rank integer,
        city text,
        population integer
    )
''')

c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '상하이', 24150000))

#파라미터가 딕셔너리일 때는 플레이스홀더를 :<이름> 형태로 지정합니다.
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
            {'rank': 2, 'city': '카라치', 'population': 23500000})

#executemany() 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서
#여러 개의 SQL 구문을 실행할 수 있습니다.
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank':3, 'city': '베이징', 'population': 21516000},
    {'rank':4, 'city': '텐진', 'population': 14722100},
    {'rank':5, 'city': '이스탄불', 'population': 14160467},
])

conn.commit()

c.execute('SELECT * FROM cities')

for row in c.fetchall():
    print(row)

conn.close()