from openai import OpenAI

client = OpenAI(api_key=input("Enter your OpenAI API key: "))

prompt = input("Enter a prompt: ")

response = client.responses.create(
    model="gpt-3.5-turbo-instruct",
    input=prompt
)

print("\nGenerated Text:")
print(response.output_text)