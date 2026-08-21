from openai import OpenAI

client = OpenAI(api_key=input("Enter your OpenAI API key: "))

prompt = input("Enter a prompt: ")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=100,
    temperature=0.7
)

print("\nGenerated Text:")
print(response.choices[0].text.strip())