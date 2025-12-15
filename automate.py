# import fastapi to create api
from fastapi import FastAPI
from datetime import datetime
# 
from sqlalchemy import create_engine, text

app = FastAPI()

source_engine = create_engine("mysql+pymysql://root:0786@localhost:3306/hero")

# destination database (data jahan daalna hai)
dest_engine = create_engine("mysql+pymysql://root:0786@localhost:3306/apidatabase")

def get_employee():
    query = '''SELECT created_at 
            FROM apidatabase.user_activity 
            order by created_at desc
            limit 1;'''

    with source_engine.connect() as conn:
        result = conn.execute(text(query))
        data =  result.fetchone()

        a = data[0]

    m=a.strftime('%Y-%m-%d')
    n=a.strftime('%H:%M:%S')

    query2=f'''select * from get_data where Time(created_at) > "{n}" and date(created_at)>{m}'''

    with source_engine.connect() as source_conn:
        result = source_conn.execute(text(query2))
        data = [dict(row._mapping) for row in result.fetchall()]
        return data
        
c=get_employee()
print(c)


print("hello")

print("tanzeem sheikh")
