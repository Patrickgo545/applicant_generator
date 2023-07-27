import os
import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= 
[
        {"role": "user", "content": "What color is the sky?"}
    ],
#  [
#    {
#      "role": "system",
#      "content": "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in json with a single key called \"css_code\"."
#    },
#    {
#      "role": "user",
#      "content": "Blue sky at dusk."
#    }
#  ],
  temperature=0,
  max_tokens=1024
)

print(response)