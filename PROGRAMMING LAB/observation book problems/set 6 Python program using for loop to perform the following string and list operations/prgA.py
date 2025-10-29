
str = input("Enter a string:")
word = {}
# Loop through each character in the input string
for char in str:
# If the character is already in the dictionary, increase its count by 1
    if char in word:
        word[char] += 1
# If the character is not in the dictionary, add it with an initial count of 1
    else:
        word[char] = 1
# Print a header message
print("Character frequency:")
# Loop through each key-value pair in the dictionary
for char, count in word.items():
    # Print each character and its frequency
    print(f"{char}:{count}")