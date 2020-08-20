user_input_string = input("Enter a string and we will give you the length: ")

def iterLength(user_input_string):
    count = 0
    for i in range(len(user_input_string)):
        count += 1 
    return count 


print(iterLength(user_input_string))

def recursiveLength(user_input_string):
    
    if user_input_string == '':
        return 0
    return 1 + recursiveLength(user_input_string[1:])
print(recursiveLength(user_input_string))
    
    
