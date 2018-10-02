letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

vorige_letter = ''
aantal_letters = []

for letter in sorted(letters):
    if vorige_letter != letter:
        aantal_letters.append(letters.count(letter))
    vorige_letter = letter

print(aantal_letters)
