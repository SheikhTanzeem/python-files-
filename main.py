# from fastapi import FastAPI
# from sqlalchemy import create_engine, text

# engine = create_engine("mysql+pymysql://root:0786@localhost:3306/praticeadvance")
# app = FastAPI()

# @app.get("/ajao")  # URL me space mat use karo
# def get_data():
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT * FROM employee_pratice;"))
#         # Saare rows ko list of dicts me convert karo
#         data = [dict(row) for row in result]
#     return {"employees": data}  # JSON-friendly return


# @app.get("/students")
# def get_students():
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT * FROM students;"))
#         # Row ko dictionary me convert karke return kar rahe hain
#         data = [dict(row) for row in result]
#     return {"students": data}

# from fastapi import FastAPI
# from sqlalchemy import create_engine, text

# # engine = create_engine("mysql+pymysql://root:0786@localhost:3306/praticeadvance")
# # app = FastAPI()

# # @app.get("/hey")  
# # def get_employee():
# #     with engine.connect() as connection:
# #         result = connection.execute(text("SELECT * FROM employee_pratice;"))
        
# #         data = [dict(row) for row in result]
# #     return {"hey":data}  

# # python -m uvicorn main:app -- reload

from fastapi import FastAPI
from sqlalchemy import create_engine ,text

engine = create_engine("mysql+pymysql://root:0786@localhost:3306/hero")
app = FastAPI()


@app.get("/hello")
def get_employee():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM  get_data;"))
        data = [row for row in result.mappings()] 
    return {"hello": data}

# x,y,z = 'hey','bey','nice'
# print(x)



# from fastapi import FastAPI
# from sqlalchemy import create_engine, text

# engine = create_engine("mysql+pymysql://root:0786@localhost:3306/hero")
# app = FastAPI()

# @app.get("/hello")
# def get_employee(date: str = None, time: str = None):
#     with engine.connect() as connection:
   
#         query = "SELECT * FROM api_data"
#         params = {}

     
#         if date:
#             query += " WHERE DATE(purchase_date) = :date"
#             params["date"] = date

        
#         elif time:
#             query += " WHERE TIME(purchase_date) = :time"
#             params["time"] = time

#         # agar dono diye gaye hain
#         elif date and time:
#             query += " WHERE DATE(purchase_date) = :date AND TIME(purchase_date) = :time"
#             params["date"] = date
#             params["time"] = time

#         result = connection.execute(text(query), params)
#         data = [row for row in result.mappings()]

#     return {"data": data}
