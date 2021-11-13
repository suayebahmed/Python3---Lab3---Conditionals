"""
This is a program that takes zipcode as input and tell the area of the zipcode.
"""

# Take a 5 zip code digit input from user
zip_code = input("Enter 5-digit ZIP code: ")

# USing conditional statements to determine the city related to zipcode.
if 370 <= int(zip_code[:3]) <= 372:
    print(f"Mail with ZIP code {zip_code} is handled by Nashville.")
elif 373 <= int(zip_code[:3]) <= 374:
    print(f"Mail with ZIP code {zip_code} is handled by Chattanooga.")
elif 375 == int(zip_code[:3]) or 380 <= int(zip_code[:3]) <= 381:
    print(f"Mail with ZIP code {zip_code} is handled by Memphis.")
elif "376" in zip_code:
    print(f"Mail with ZIP code {zip_code} is handled by Johnson City.")
elif 377 <= int(zip_code[:3]) <= 379:
    print(f"Mail with ZIP code {zip_code} is handled by Knoxville.")
elif "382" in zip_code:
    print(f"Mail with ZIP code {zip_code} is handled by McKenzie.")
elif "383" in zip_code:
    print(f"Mail with ZIP code {zip_code} is handled by Jackson.")
elif "384" in zip_code:
    print(f"Mail with ZIP code {zip_code} is handled by Columbia.")
elif "385" in zip_code:
    print(f"Mail with ZIP code {zip_code} is handled by Cookeville.")
else:
    print(zip_code, "is outside of Tennessee")
