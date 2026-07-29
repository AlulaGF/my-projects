def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# Ask the user to enter some text
text = input("Enter a word or sentence: ")

# Call the function and print the result
print(f"The number of vowels is: {count_vowels(text)}")