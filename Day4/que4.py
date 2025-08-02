#  Ask the user to enter a word and a number. Repeat the word as many times as the given number and print the result.
    #  **Expected Input:** word = "Hello", number = 3
    # **Expected Output:** "HelloHelloHello"

user_name = input("Enter the your name : ")

num = int(input("Enter your number that means that number reating the user name : ")) 

repeat =  (user_name + " ") * num

print(repeat)