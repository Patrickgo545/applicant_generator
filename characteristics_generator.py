'''
Using functions to generate a handful of characteristics in order to

    1. Achieve a bell curve in the "critical level" population pool
    2. Have the mock data set achieve similar statistics to 
    our actual applicant pool

'''

import random

def critical_level_generator():
    mu = 3 
    sigma = 0.75 
    random_value = random.gauss(mu, sigma)
    random_value = max(1, min(5, random_value))
    rounded_value = round(random_value, 2)
    return rounded_value

def gender_generate():
    genders = ['Male' , 'Female' , 'Other']
    weights = [0.17 , 0.73 , 0.02]
    return random.choices(genders , weights = weights)[0]

def age_generate():
    average_age = 35.1
    min_age = 16
    sigma = 10 

    age = round(random.gauss(average_age, sigma))
    age = max(min_age, age)
    
    return age

def household_size_generate():
    average_household_size = 3.43
    sigma = 1.0

    household_size = round(random.gauss(average_household_size, sigma))
    household_size = max(1, household_size)

    return household_size

def children_generate():
    average_children = 1.36
    sigma = 1.0

    num_children = round(random.gauss(average_children, sigma))
    num_children = max(0, num_children)

    return num_children

def dependent_seniors_generate():
    average_dependent_seniors = 0.25
    sigma = 0.5

    seniors = round(random.gauss(average_dependent_seniors, sigma))
    seniors = max(0, seniors)

    return seniors

def chronic_illnesses_qty_generate():
    average = 2.34
    sigma = 2.0

    num_illness = round(random.gauss(average, sigma))
    num_illness = max(0, num_illness)

    return num_illness

def race_generate():
    races = ['White' , 'Hispanic' , 'Black' , 'No Answer' , 'American Indian' , 'Asian' , 'Multi-Racial' , 'NHOPI']
    weights = [0.489 , 0.256 , 0.141 , 0.061 , 0.027 , 0.014 , 0.007 , 0.005]
    return random.choices(races , weights=weights)[0]

def sexual_orientation_generate(): 
    sexual_orientation = ['Heterosexual' , 'i\'d rather not say' , 'Bi-Sexual' , 'Homosexual' , 'Other']
    weights = [0.7825 , 0.0928 , 0.0616 , 0.0349 , 0.028]
    return random.choices(sexual_orientation , weights=weights)[0]

def income_generate():
    average = 21417.54
    std_dev = 19317.42
    
    income = random.gauss(average , std_dev)
    income = max(0 , income)

    rounded_income = round(income , -3)
    return rounded_income

def household_with_insurance_generate():
    insured = [True , False]
    weights = [0.82 , 0.18]
    return random.choices(insured , weights=weights)[0]

def insurance_plan_generate():
    insurance = ['Commercial / Private' , 'Medicaid' , 'Medicare' , 'Duals']
    weights = [0.42 , 0.4 , 0.12 , 0.06]
    return random.choices(insurance , weights=weights)[0]

def employment_generate():
    status = ['Employed' , 'Need Employment' , 'Need Help Keeping Job' , 'Disabled']
    weights = [.6602 , .2521 , .086 , .0016]
    return random.choices(status , weights=weights)[0]

def benefits_generate(age , income , household_size , gender):
    benefits = []
    income_per_person = income / household_size

    # SOCIAL SECURITY
    if age >= 65 and income <= 30000:
        chance = random.random()

        if chance <= .9:
            benefits.append('SSI')
    

    # TANF - TEMPORARY ASSISTANCE FOR NEEDY FAMILIES
    if income_per_person <= 10000:
        chance = random.random()

        if chance <= .8:
            benefits.append('TANF')


    # SNAP - Supplemental Nutrition Assistance Program
    if income_per_person < 20000:
        chance = random.random()

        if chance <= .8:
            benefits.append('SNAP')


    # WIC - For pregnant women or women with children under 5 yrs old
    if gender == 'Female' and household_size > 1:
        chance = random.random()

        if chance <= .8:
            benefits.append('WIC')


    return benefits



# TURN CHARACTERISTICS INTO A FUNCTION
def characteristics_generator_loop():
    critical_level = critical_level_generator()
    gender = gender_generate()
    age = age_generate()
    household_size = household_size_generate()
    dependent_seniors = dependent_seniors_generate()
    chronic_illness_qty = chronic_illnesses_qty_generate()
    race = race_generate()
    sexual_orientation = sexual_orientation_generate()
    income = income_generate()
    household_with_insurance = household_with_insurance_generate()
    insurance_plan = insurance_plan_generate()
    employment = employment_generate()
    benefits = benefits_generate(age , income , household_size , gender)

    characteristics_dictionary = {
        'critical level' : critical_level, 
        'gender' : gender, 
        'age' : age, 
        'household size' : household_size, 
        'dependent seniors' : dependent_seniors,
        'chronic_illness_qty' : chronic_illness_qty,
        'race / ethnicity' : race,
        'sexual_orientation' : sexual_orientation,
        'income' : income,
        'household_with_insurance' : household_with_insurance,
        'insurance_plan' : insurance_plan,
        'insurance_plan' : insurance_plan,
        'employment' : employment,
        'Benefits' : benefits,
    }

    return characteristics_dictionary

# print(characteristics_generator_loop())