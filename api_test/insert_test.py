# Testing / Preparing the INSERT INTO SQL Command

import random

genders = ["'M'" , "'F'"]
weights = [.5 , .5]

sex = random.choices(genders , weights = weights)[0]
age = random.randint(1,100)
name = "'Test'"

sql_command = f"INSERT INTO [api_test].[dbo].[api_test_table] (Sex, Age, Name) VALUES ({sex}, {age}, {name})"