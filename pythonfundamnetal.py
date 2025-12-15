# WE USE FSTRING AND ALSO USE SCAPE SEQUENCE -

cost_of_product = 2000
product_id = "1001"
product_name = "noise buds"

print(f'''cost of the product is {cost_of_product} 
product ID is {product_id}
product name is {product_name}''')


from loguru import logger
logger.info(f'cost of the product is {cost_of_product}')