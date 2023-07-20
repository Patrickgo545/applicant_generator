import openai

#openai.api_key="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"

"""response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)
"""
query_qty = 5

while query_qty > 0:
    print('.')
    query_qty -= 1