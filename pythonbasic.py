import logging
from loguru import logger

# length_of_land = 100
# breath_of_land = 100
# bricks_cost_per_piece = 10.20
# labour_mistri1 = "jagmohan"
# labour_mistri2 = "rahul"




# total_land = length_of_land * breath_of_land

# logger.info(f'The total area of land is {total_land} sq ft')

# # MODULO OPERATOR 


# MODELO = 15%6

# logger.info(f'THE MODULO OF THIS NUMBERS ARE {MODELO}')

# A = 25
# B = 25.99

# logger.info(F'{(A+B)}')





# TYPES OF TYPE CASTING 
# 1 EXPLICIT TYPE CASTING - BY DEVELOPER
# 2 IMPLICIT TYPE CASTING  - BY PYTHON AUTOMATIC
#  abs = convert negative value in positive   


length_of_land = float(input("please entre the length"))
breadth_of_land = float(input("please entre your breadth"))
total_land_area = float(length_of_land)*float(breadth_of_land)

logger.info(f'total area of land is {total_land_area}')