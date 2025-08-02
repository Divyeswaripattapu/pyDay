# Ask the user to input a sentence. Find the length of the sentence, and print the last character of the sentence.
# Expected Output:** Length of the sentence and the last character.

# user_put = input("Enter your sentence : ")

# length = len(user_put) 

# last_word = last_word(user_put.split(),key=len)

# print("Last word is  : ",last_word)
# print(last_word)



# Ask the user to input a sentence
sentence = input("Enter a sentence: ")

# Find the length of the sentence
length = len(sentence)

# Print the length of the sentence
print("Length of the sentence:", length)

# Print the last character of the sentence
if length > 0:
    print("Last character of the sentence:", sentence[-1])
else:
    print("The sentence is empty.")







    # print word of last


    # Get input from user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.strip().split()

# Check if there are any words
if words:
    print("Last word:", words[-1])
else:
    print("No words found in the sentence.")