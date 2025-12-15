# # CREATING LIST 

# from loguru import logger

# labout_name_and_cost = {

#     "ramesh":500,
#     "raja":900,
#     "raju":500,
#     "kaju":300      
# }

# # TO ADD MORE LABOUR IN DICT

# labout_name_and_cost["jadu"] = 700
# labout_name_and_cost["jagmohan"] = 600

# logger.info(f'{labout_name_and_cost}')

# for name in labout_name_and_cost: 
#     print(name)


# for name in labout_name_and_cost:
#     logger.info(f'{name} {labout_name_and_cost [name]}')


NAMES_MARKS = {

    "TANZEEM":100,
    "ZAID":55,
    "TANVEER":54,
    "HUDA":66
}
# print(NAMES_MARKS)
# print(NAMES_MARKS.keys())
# print(NAMES_MARKS.values())
NAMES_MARKS.update({"TANVEER":88})
print(NAMES_MARKS)