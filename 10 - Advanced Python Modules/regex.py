import re

text = "The agent's phone number is 408-555-1234. call soon!"
pattern = "phone"
print(re.search(pattern, text))

pattern = "NOT IN TEXT"
print(re.search(pattern, text))


pattern = "phone"
match = re.search(pattern, text)

print(match.span())
print(match.end())

text = "My phone once, my phone twice"
match = re.search("phone", text)
print(match)

matches = re.findall("phone", text)
print(matches)

for match in re.finditer("phone", text):
    print(match.span())
