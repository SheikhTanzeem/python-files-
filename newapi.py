from fastapi import FastAPI, Query
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

source = create_engine("mysql+pymysql://root:0786@localhost:3306/hero")
dest = create_engine("mysql+pymysql://root:0786@localhost:3306/apidatabase")


@app.get("/get_employee")
def get_employee(
    date: Optional[str] = Query(None),
    time: Optional[str] = Query(None)
):
    q = "SELECT * FROM get_data"
    params = {}
    conds = []
    if date:
        conds.append("DATE(created_at)=:date")
        params["date"] = date
    if time:
        conds.append("TIME(created_at)>=:time")
        params["time"] = time
    if conds:
        q += " WHERE " + " AND ".join(conds)
    q += " ORDER BY created_at DESC"
    with source.connect() as conn:
        rows = conn.execute(text(q), params).fetchall()
        data = [dict(row._mapping) for row in rows]
    return {"fetched_rows": len(data), "data": data}


@app.post("/sync_data")
def sync_data(
    date: Optional[str] = Query(None),
    time: Optional[str] = Query(None)
):
    q = "SELECT * FROM get_data"
    params = {}
    conds = []
    if date:
        conds.append("DATE(created_at)=:date")
        params["date"] = date
    if time:
        conds.append("TIME(created_at)>=:time")
        params["time"] = time
    if conds:
        q += " WHERE " + " AND ".join(conds)
    with source.connect() as conn:
        rows = conn.execute(text(q), params).fetchall()
        data = [dict(row._mapping) for row in rows]
    if not data:
        return {"message": "No new data found", "inserted": 0}
    with dest.connect() as conn:
        for row in data:
            conn.execute(
                text("INSERT INTO user_activity (id, price, product_name, created_at) VALUES (:id, :price, :product_name, :created_at)"),
                row
            )
        conn.commit()
    return {"message": f"{len(data)} new rows inserted", "inserted": len(data)}