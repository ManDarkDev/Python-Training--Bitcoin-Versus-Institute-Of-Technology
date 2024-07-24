#Dont be a gatekeeper. Share your knowldedge with whoever is willing to listen. 
#However, Pearls gifted to swine are just plain ol' rocks to them. 
#Understand who's able to appreciate the jewels you possess.

def max_num (num1, num2, num3):# Define a function 'max_num' that takes three arguments: num1, num2, and num3
    if num1 >= num2 and num1 >= num3: #if num1 is greater than or equal to num2 and num1 is greater than or equal to num3
        return num1 # If true, return num1
    elif num2 >= num1 and num2 >= num3: # Otherwise, check if num2 is greater than or equal to both num1 and num3
        return num2 # If true, return num2
    else: 
        return num3 # Return num3


    
print(max_num(1000,21,555,)) # Call the 'max_num' function with arguments 1000, 21, and 555, and print the result
