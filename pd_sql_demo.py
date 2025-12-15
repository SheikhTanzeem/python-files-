# import mysql.connector as coco
# import pandas as pd
# from pandasql import sqldf


# conn = coco.connect(
#     host="localhost",
#     user="root",
#     password="0786",
#     database="hero"
# )
# print('succesfull')


# query = """
# select customer_name , price 
# from customer_order
# """
# result = sqldf(query)
# print(result)
# 
import mysql.connector as coco
import pandas as pd

conn = coco.connect(
    host="localhost",
    user="root",
    password="0786",
    database="hero"
)
print('Connection successful ✅')

query = """
SELECT customer_name, price
FROM wwfp
where price <= 200
"""

# Run SQL query directly on MySQL
df = pd.read_sql(query, conn)

print(df)
