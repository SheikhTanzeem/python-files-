from loguru import logger

# # negative indexing
# LABOUR_NAME = ["RAMESH","SURESH","ANKIT","RAJA"]
# logger.info(f'The first name of labour is {LABOUR_NAME[-1]}')
# # POSTIVE INDEXING

# LABOUR_NAME2=["RAJA","SHAYAM","MOHIT"]
# logger.info(f'this index labour name is{LABOUR_NAME2[1]}')

# # ADD VALUE

# LABOUR_NAME.append("hero")

# logger.info(f'{LABOUR_NAME2}')

# FOR INSERT MULTIPLE VLAUES IN ONE TIME
# # EXTEND IS A FUNCTION WHICH INSERT MULTIPLE VALUES IN ONE TIME 
# # FIRST YOU CREAT A VARIBLE OF VALUES 

# NEW_LABOUR = ["NANU","HERO2","RAJU"]
# LABOUR_NAME.extend(NEW_LABOUR)

# logger.info(F'{LABOUR_NAME}')

# # IF YOU WANT TO ADD VALUE ON A PERTICULAR INDEX SO YOU USE 
# # INSER FUNCTION

# LABOUR_NAME.insert(0,"TANZEEM")
# logger.info(f'{LABOUR_NAME}')


# MULTIDIMENSION LIST 

# labour_and_cost = [["lala",500],["jala",600],["chcha",450]]
# # logger.info(F'THE LABOUR NAME IS {labour_and_cost[0][0]} AND HE COSTING FOR A DAY IS {labour_and_cost[0][1]}')


# NAME_AND_CLASS =  [['TANZEEM','12TH'],['AKIB','12TH'],['SHARIQ','12TH'],['MOHAN','12TH']]
# logger.info(F'THIS IS A STUDENT NAME{[NAME_AND_CLASS[0][0]]} AND THIS A CLASS OF STUDENT{[NAME_AND_CLASS[0][1]]}')

# labour_name_cost =['ram','rohit','manoj','naman',300,400,400,600,450]

# labour_name_cost.pop()
 
# wage = labour_name_cost.pop()

# if wage > 400:
#     print("mahega labour hai")

# TO REOMOVE ANY VALUE
# labour_name_cost.remove(400)
# logger.info(f'{labour_name_cost}')

# TO DELECT LIST

# del labour_name_cost
# print(labour_name_cost)

# TO CHANGE THE VALUE OF LIST 

# labour_name_cost[0] = "saham"
# labour_name_cost[4] = 700

# logger.info(f'{labour_name_cost}')

# # FOR MULTIPLE CHANGING VALUES 

# labour = ['spider ','super ','bat']
# logger.info(f'{labour}')

# labour[0:3] = ['spider man','super man','bat man']

# logger.info(f'{labour}')
 
 
# path = "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\students_nested.json"
# splited = path.split("\\")
# logger.info(f'{splited}')

# logger.info(f'{splited[0:3]}')
