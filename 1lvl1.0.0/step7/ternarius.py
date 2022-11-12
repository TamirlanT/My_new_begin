word = 'Привет'

result = []

for i in range(len(word)):
    letter = word[i]
    letter =letter.lower() if i % 2 != 0 else letter.upper()
    result.append(letter)

print(result)
result = ''.join(result)
print(result)