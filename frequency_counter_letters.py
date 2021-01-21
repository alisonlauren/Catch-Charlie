inp = input("Give me a word: ").lower()

def most_charachters(str):
    if len(str) == 0:
      print("empty input: need word.")

    result = {}
    letter_count = 0

    for letter in str:
        if letter not in result.keys():
            result[letter] = 1
        else:
            result[letter] += 1

        for value in result.values():
            if value > letter_count:
                letter_count = value

        for key in result.keys():
            if result[key] == letter_count:
                print(f'{key}: {result[key]}')

most_charachters(inp)
   

