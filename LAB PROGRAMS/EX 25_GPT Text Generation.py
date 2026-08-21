from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompt = input("Enter a prompt: ")

result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
)

print("\nGenerated Text:")
print(result[0]["generated_text"])