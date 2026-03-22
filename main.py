
import random

# List of lowercase and uppercase letters
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

# List of digits
numbers = ["0","1","2","3","4","5","6","7","8","9"]

# List of special characters (symbols)
symbols = [
    "!","@","#","$","%","^","&","*","(",")",
    "-","_","=","+","[","]","{","}",
    ";",":",",",".","<",">","?","/","|"
]

# This list will store all selected characters for the password
password_list = []

# Loop to add characters to the password
# Each loop adds:
# - 1 letter
# - 1 number
# - 1 symbol
# Total length = 6 * 3 = 18 characters
for i in range(6):
    password_list.append(random.choice(letters))
    password_list.append(random.choice(numbers))
    password_list.append(random.choice(symbols))

# Shuffle the list to make the password more random
random.shuffle(password_list)

# Join all characters into one string
password = "".join(password_list)

# Print the final password
print("A strong password is:", password)
