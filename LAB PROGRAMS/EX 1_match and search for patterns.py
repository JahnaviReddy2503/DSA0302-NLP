import re

text = "Natural Language Processing is an exciting field of Artificial Intelligence."

pattern = "Language"

result = re.search(pattern, text)

if result:
    print("Word found:", result.group())
else:
    print("Word not found")

matches = re.findall(r'\bA\w+', text)

print("Words starting with 'A':")
print(matches)