import re
def main():
    #Asks user to choose the type of number to verify
    number = input("Please choose the type of number you want to verify. 1 for phone number, 2 for SSN, 3 for zip code. ")
    while number not in ["1", "2", "3"]:
        number = input("Invalid choice. Please enter 1, 2, or 3. ")
    return number

def phone_num(number):
    #Sets the phone number format and asks for user input
    if number == "1":
        pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
        s = input('Enter a 10-digit tel. number in format xxx-xxx-xxxx: ')
        while not re.fullmatch(pattern, s):
            s = input("Invalid format.")
def socsec_num(number):
    #Sets the SSN format and asks for user input
    if number == "2":
        pattern = r'\d\d\d-\d\d-\d\d\d\d'
        s = input('Enter a 9-digit SSN in format xxx-xx-xxxx: ')
        while not re.fullmatch(pattern, s):
            s = input("Invalid format. Please enter a SSN in xxx-xx-xxxx format. ")
        print('Number accepted.')

def zip_code(number):
    #Sets the zip code format and asks for user input
    if number == "3":
        pattern = r'\d\d\d\d\d'
        s = input('Enter a 5-digit zip code: ')
        while not re.fullmatch(pattern, s):
            s = input("Invalid format. Please enter a zip code in xxxxx format. ")
        print('Number accepted.')

if __name__ == "__main__":
    number = main()
    phone_num(number)
    socsec_num(number)
    zip_code(number)