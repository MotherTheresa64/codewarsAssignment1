#Even_or_Odd--------------------------------------------------------------
def even_or_odd(number):
    # Check if the number is divisible by 2 (even number)
    if number % 2 == 0:
        # If the remainder when divided by 2 is 0, it is an even number.
        return "Even"
    else:
        # If the remainder is not 0, it is an odd number.
        return "Odd"

#Convert a Number to a String---------------------------------------------
def number_to_string(num):
    # Convert the number 'num' to a string using the str() function
    num = str(num)
    # Return the number as a string
    return num

#Remove String Spaces-------------------------------------------------------------
def no_space(x):
    # Replace all spaces in the string 'x' with an empty string
    return x.replace(" ", "")

#Vowel Count ----------------------------------------------------------------
def get_count(sentence):
    # sum() is used to count the vowels in the sentence.
    # Inside sum(), we're using a generator expression to iterate over each character in the sentence.

    # 'char in sentence' loops through each character in the sentence string.
    # 'char in "aeiou"' checks if the character is one of the vowels (a, e, i, o, u).
    # If it is, the generator produces '1' for that character.
    
    return sum(1 for char in sentence if char in "aeiou")  # Count the number of vowels and return the total.