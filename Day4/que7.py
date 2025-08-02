#  Create two strings `str1` and `str2`. Find the lengths of both strings and concatenate them. Print the concatenated string.
#     Expected Input:** str1 = "Hello", str2 = "World"
#     Expected Output:** "HelloWorld"


str1 = input("Enter your sentence : ") 

str2 = input("Enter your 2nd  sentence : ")

concate = str1 + str2 

length1 = len(str1)

length2 = len(str2)

print("The length of the first string is :",length1)

print("The length of the second string is :",length2) 

print("The length of the concatinating strings are :",len(concate))
