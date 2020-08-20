#here I check and print all of the charecters that are not vowels in a given list
vowels = "aeiou"
input_string = "iamacoolkid"


def rec_not_a_vowel(vowels,input_string, idx=0):
    while idx <= len(input_string) -1:
        if input_string[idx].lower() not in vowels:
            print(input_string[idx])
        return rec_not_a_vowel(vowels,input_string, idx+1)
print("")
print("Here are the non vowels in the string : ")
rec_not_a_vowel(vowels,input_string, 0)


#Here I do the same thing but instead I print out all of the vowels instead
print("")
print("Here are the vowels in the string: ")
def rec_is_a_vowel(vowels, input_string, idx = 0):

    while idx <= len(input_string) -1:
        if input_string[idx].lower() in vowels:
            print(input_string[idx])
        return rec_is_a_vowel(vowels, input_string, idx +1)

rec_is_a_vowel(vowels, input_string, 0)