# Organizing each component of the GPT query

import characteristics_generator

def read_query_component(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

intro_block = read_query_component('./applicant_generator/query_component_blocks/intro_block.txt')
parameters_block = read_query_component('./applicant_generator/query_component_blocks/parameters_block.txt')
instruction_block = read_query_component('./applicant_generator/query_component_blocks/instruction_block.txt')
final_instruction = read_query_component('./applicant_generator/query_component_blocks/final_instruction.txt')
json_health_equity_questionnaire = \
    read_query_component('./applicant_generator/query_component_blocks/json_health_equity_questionnaire.txt')

characteristics_block = ('Here are some characteristics I want you to apply to this individual ' , \
                         characteristics_generator.characteristics_dictionary)

complete_query = [intro_block, parameters_block , instruction_block , characteristics_block , \
                  final_instruction , json_health_equity_questionnaire]


# SQL QUERY
# CREATE QUERY
sql_query = '''
INSERT INTO dbo.applicant_generator(
story, 
gender,
enough_food,
houshold_size,
insecurity_frequency,
illnesses,
posted,
health_insurance,
health_plan,
children_in_household,
seniors_in_household,
medical_transportation,
grocery_transportation,
dental_transportation,
internet_access,
computer_in_home,
preferred_language,
english_as_second_language,
orientation,
race,
ethnicity,
cant_afford_balanced_meals,
skipped_meals,
benefits,
interested_in_other_programs,
living_situation_today,
problems_with_housing,
assistance_required_for_housing,
risk_of_losing_services,
want_help_with_employment,
how_hard_to_pay_for_basics,
income_bracket,
live_with_illness,
illness_other_family_members,
difficulty_remembering_making_decisions,
difficulty_doing_errands_alone,
health_insurance_type,
physically_hurt_you,
talk_down_to_you,
threaten_you_with_harm,
scream_or_curse_at_you,
date_of_birth,
want_help_with_school_or_training,
need_help_with_day_to_day_activities,
do_you_feel_lonely_or_isolated,
days_per_week_moderate_exercise,
minutes_spent_exercising,
have_little_to_no_interest_in_doing_things,
feeling_down_or_depressed,
do_you_feel_this_kind_of_stress_these_days,
have_you_had_5_or_more_drinks_in_a_day,
tobacco_products_in_the_past_12_months,
prescription_druges_for_non_medical_use,
illegal_drugs_in_the_last_year,
worry_food_run_out
) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

sql_query_values = '''
    survey["story"], 
    survey["gender"],
    survey["enough_food"],
    survey["houshold_size"], 
    survey["insecurity_frequency"], 
    survey["illnesses"],
    survey["posted"], 
    survey["health_insurance"], 
    survey["health_plan"], 
    survey["children_in_household"], 
    survey["seniors_in_household"],
    survey["medical_transportation"], 
    survey["grocery_transportation"], 
    survey["dental_transportation"], 
    survey["internet_access"],
    survey["computer_in_home"], 
    survey["preferred_language"], 
    survey["english_as_second_language"], 
    survey["orientation"], 
    survey["race"],
    survey["ethnicity"], 
    survey["cant_afford_balanced_meals"], 
    survey["skipped_meals"], 
    survey["benefits"], 
    survey["interested_in_other_programs"],
    survey["living_situation_today"], 
    survey["problems_with_housing"], 
    survey["assistance_required_for_housing"],
    survey["risk_of_losing_services"], 
    survey["want_help_with_employment"], 
    survey["how_hard_to_pay_for_basics"], 
    survey["income_bracket"],
    survey["live_with_illness"], 
    survey["illness_other_family_members"], 
    survey["difficulty_remembering_making_decisions"],
    survey["difficulty_doing_errands_alone"], 
    survey["health_insurance_type"], 
    survey["physically_hurt_you"], 
    survey["talk_down_to_you"],
    survey["threaten_you_with_harm"], 
    survey["scream_or_curse_at_you"], 
    survey["date_of_birth"], 
    survey["want_help_with_school_or_training"],
    survey["need_help_with_day_to_day_activities"], 
    survey["do_you_feel_lonely_or_isolated"], 
    survey["days_per_week_moderate_exercise"],
    survey["minutes_spent_exercising"], 
    survey["have_little_to_no_interest_in_doing_things"], 
    survey["feeling_down_or_depressed"],
    survey["do_you_feel_this_kind_of_stress_these_days"], 
    survey["have_you_had_5_or_more_drinks_in_a_day"],
    survey["tobacco_products_in_the_past_12_months"], 
    survey["prescription_druges_for_non_medical_use"],
    survey["illegal_drugs_in_the_last_year"], 
    survey["worry_food_run_out"]
'''