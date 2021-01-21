print("Want to find out if two words are an anagram?")
string1 = input("Give me word 1: ").lower()
string2 = input("Give me word 2: ").lower()

def anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        print("This is an anagram!")
    else:
        print("This is not, obviously..")

anagram(string1, string2)