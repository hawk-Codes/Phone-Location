import phonenumbers
from phonenumbers import geocoder

number = input("Enter number for searching: ")

ch_number = phonenumbers.parse(number, "CH")

print("Location: ")
print(geocoder.description_for_number(ch_number, "en"))