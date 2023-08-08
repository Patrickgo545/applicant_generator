import os
import openai
import query_components
import pyodbc
import json

openai.api_key = ""


# SQL DATABASE
server = 'LAPTOP-T37NP786' # (SQL) SELECT @@ServerName
database = 'api_test'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def transfer_data_to_sql():
  try:
      # Establish the connection
      connection = pyodbc.connect(connection_string)
      cursor = connection.cursor()

      # Example: Execute a query
      cursor.execute(
          query_components.sql_query,
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
      )
      connection.commit()

      # Close the connection
      connection.close()

  except pyodbc.Error as ex:
      print('Error:', ex)
      print('Error code:', ex.args[0])
      print('Error message:', ex.args[1])



# CHECK GPT RESPONSE
def json_check():
    content_json_string_list = list(content_json_string)

    if content_json_string_list[0] == '[':
        return True
    else: 
        return False



# CREATE LOOP
heq_applicant_count = 0

while heq_applicant_count < 5:
  # GPT Prompt

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages= [
      {
        "role": "system",
        "content": query_components.complete_query()
      },
    ],
    temperature=0,
    max_tokens=1200,
    top_p = 1
  )

  # Target the HEQ - JSON portion only
  content_json_string = str(response['choices'][0]['message']['content'])
  content_json_deserialized = json.loads(content_json_string)
  survey = content_json_deserialized[0]

  response_is_json = json_check()

  try: 
    if response_is_json == True:
      transfer_data_to_sql()

      heq_applicant_count += 1
      print('loop - successful')

  except:
      print('loop - failed')

print('Done')

#print('prompt' , query_components.complete_query())
# print('response' , response)
# print('string' , content_json_string)
#print('deserialized' , content_json_deserialized)

# Print entire GPT response 
# data_dict = json.loads(str(response))
# print(data_dict)