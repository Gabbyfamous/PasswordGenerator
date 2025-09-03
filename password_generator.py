#Input require libraries
import secrets

numbers = ['0','1','2','3','4','5','6','7','8','9']
lowercase = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

uppercase = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
symbols = [
    '!','"','#','$','%','&',"'",'(',')','*','+',
    ',','-','.','/',':',';','<','=','>','?','@',
    '[','\\',']','^','_','`','{','|','}','~'
]
while True: #Continue loop until user input correct parameters for all variables
    try:
        password_length = int(input("Enter the password length (must be 8 and above): "))
        if password_length < 8:
            print("Password must be at least 8 characters long")
            continue
        password_count = int(input("Enter How many password you want (must be 1 and above): "))
        if password_count < 1:
            print("Password must be at least 1 character")
            continue

        wants_uppercase = int(input(" Do you wants uppercase: 1 for yes, or any number for no "))
        wants_lowercase = int(input("Do you wants lowercase: 1 for yes, or any number for no "))
        wants_symbols = int(input("Do you wants symbols: 1 for yes, or any number for no "))
        wants_numbers = int(input("Do you wants numbers: 1 for yes, or any number for no "))


        break

    except ValueError:
        print("Please enter a number.")
def generate_password(password_length, password_count, wants_uppercase, wants_lowercase, wants_symbols, wants_numbers) :

    """
    Generates 3 random password of user desired length

    input:
    password_length - length of password to generate
    password_count - how many password you want
    wants_uppercase - whether uppercase or lowercase password
    wants_lowercase - whether lowercase or uppercase password
    wants_symbols - whether symbols password
    wants_numbers - whether numbers password


    returns:
    password - generated password


    """
    password_characters = []
    if wants_uppercase == 1:
        password_characters.extend(uppercase)
    if wants_lowercase == 1:
        password_characters.extend(lowercase)
    if wants_symbols == 1:
        password_characters.extend(symbols)
    if wants_numbers == 1:
        password_characters.extend(numbers)

    if not password_characters:
        print("You must select at least one character type!")
        return []

    my_password = []

    password_iterator = 0
    while password_iterator < password_count:
        password = ""
        for i in range(password_length):
            password += secrets.choice(password_characters)

        my_password.append(password)
        password_iterator += 1

    for i in range(len(my_password)):
        print(f'Password {i+1}',my_password[i])
    return my_password

#Call Function
generate_password(password_length, password_count, wants_uppercase, wants_lowercase, wants_symbols, wants_numbers)





