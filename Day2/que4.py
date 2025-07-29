# Define a variable is_raining and ask the user to input either "True" or "False" (as a string). 
# Convert the input to a boolean and print its type.

user_input = input ("Is it raining ? 'True' or 'False :")

is_raining = user_input == "true"

print("The type of is_raining is  :",type(is_raining))

if is_raining :
    print("please carries a umbrilla.....")
else:
    print("Enjoy sunshine/sunset ...🙃")
