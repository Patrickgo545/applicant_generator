import os
import openai
import query_components

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages= [
    {
      "role": "system",
      "content": str(query_components.complete_query)
    },
  ],
  temperature=0,
  max_tokens=1024
)

print(response)


'''query_qty = 5

while query_qty > 0:
    print('.')
    query_qty -= 1'''