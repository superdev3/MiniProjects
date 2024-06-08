from phonenumbers import parse
from phonenumbers.geocoder import description_for_number


while True:
    user_input = input("Phone number to trace: ")
    
    try:
        phone_number = parse(user_input)
        print(description_for_number(phone_number, "eu"))
        
    except Exception:
        print("Invalid phone number")
        continue
