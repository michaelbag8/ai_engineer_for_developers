client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_completion_tokens=150,
  messages=[
    {"role": "system",
     "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "system",
     "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)
