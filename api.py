# import fastapi to create api
from fastapi import FastAPI
# 
from sqlalchemy import create_engine, text

app = FastAPI()

# source database (data jahan se uthana hai)
source_engine = create_engine("mysql+pymysql://root:0786@localhost:3306/hero")

# destination database (data jahan daalna hai)
dest_engine = create_engine("mysql+pymysql://root:0786@localhost:3306/apidatabase")


# --- GET endpoint ---
@app.get("/hello")
def get_employee():
    with source_engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM get_data;"))
        data = [dict(row) for row in result.mappings()]
    return {"hello": data}


# --- POST endpoint (ye wala naya add karna hai) ---
@app.post("/transfer_data")
def transfer_data():
    with source_engine.connect() as source_conn:
        result = source_conn.execute(text("SELECT * FROM get_data;"))
        data = [dict(row) for row in result.mappings()]

    with dest_engine.connect() as dest_conn:
        for row in data:
            columns = ", ".join(row.keys())
            placeholders = ", ".join([f":{key}" for key in row.keys()])
            query = text(f"INSERT INTO user_activity ({columns}) VALUES ({placeholders})")
            dest_conn.execute(query, row)
        dest_conn.commit()

    return {"message": f"{len(data)} rows transferred successfully!"}


