from fastapi import FastAPI
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connections
source = create_engine("mysql+pymysql://root:0786@localhost:3306/hero")
dest = create_engine("mysql+pymysql://root:0786@localhost:3306/apidatabase")


def fetch_new_data():
    # Get last created_at from target
    q1 = "SELECT created_at FROM user_activity ORDER BY created_at DESC LIMIT 1"
    with dest.connect() as conn:
        r = conn.execute(text(q1)).fetchone()
        if not r:
            last_date, last_time = "1970-01-01", "00:00:00"
        else:
            last_date = r[0].strftime("%Y-%m-%d")
            last_time = r[0].strftime("%H:%M:%S")

    # Get new data from source (hero.get_data)
    q2 = f'''
        SELECT * FROM get_data
        WHERE (DATE(created_at) > "{last_date}")
        OR (DATE(created_at) = "{last_date}" AND TIME(created_at) > "{last_time}");
    '''
    with source.connect() as conn:
        result = conn.execute(text(q2))
        return [dict(row._mapping) for row in result.fetchall()]



def insert_to_target(data):
    if not data:
        return 0
    
    with dest.connect() as conn:
        for prd in data:
            q = text("""
                INSERT INTO user_activity (id, price, product_name, created_at)
                VALUES (:id, :price, :product_name, :created_at)
            """)
            conn.execute(q, prd)
        conn.commit()
    
    return len(data)

@app.get("/get_employee")
def get_employee():
    q = "SELECT * FROM get_data ORDER BY created_at DESC"
    with source.connect() as conn:
        result = conn.execute(text(q))
        data = [dict(row._mapping) for row in result.fetchall()]
    return {"fetched_rows": len(data), "data": data}


@app.post("/sync_data")
def sync_data():
    new_rows = fetch_new_data()
    count = insert_to_target(new_rows)
    if count == 0:
        return {"message": "No new data found", "inserted": 0}
    return {"message": f"{count} new rows inserted", "inserted": count, "data": new_rows}


