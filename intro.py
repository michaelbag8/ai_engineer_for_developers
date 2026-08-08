#Introduction to OpenAI
from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  # Specify the model
    model="gpt-4o-mini",
      messages=[
          # Assign the correct role
              {"role": "user", 
                   "content": "Announce my new AI Engineer role on LinkedIn."}]
                   )

print(response.choices[0].message.content)

# Tokens cost calculation 
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")

#Experimenting with Temperature 
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """
Create a detailed product description for SonicPro headphones, it has active noise cancellation, 40 hour battery and with a beautiful foldable design 
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=400,
    temperature=1
)

print(response.choices[0].message.content)


