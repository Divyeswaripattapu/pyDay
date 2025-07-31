#  Create a string variable `sentence` containing any sentence of your choice. Ask the user to input a number, convert it to an integer, and print the sentence repeated that number of times.
#     - **Expected Input:** A number (e.g., "3")
#     - **Expected Output:** The sentence repeated the specified number of times.

sentence = "hello.....30 days in python \n"

user_count = input("Enter the number how much you wanr to print :")

number_count = int(user_count)

print(sentence * number_count)

