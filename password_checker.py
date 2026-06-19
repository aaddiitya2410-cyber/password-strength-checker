

# p=input("enter a password =")
# if len(p)<8:
#     print("Weak password,enter atleast 8 characters")
# else:
#     has_upper=False
#     has_digit=False
#     has_special=False
    
    
# for char in p:
#     if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         has_upper=True
#     elif char in "0123456789":
#         has_digit=True
#     elif char in "!@#$%^&*()_-+=/":
#         has_special=True
    
# if has_upper==True and has_digit==True and has_special==True:
#     print("Strong password")
# else:
#     print("Weak password (rules do not match)")   


text = input("Encrypt karne ke liye text likhein (e.g., hello): ")
secret_text = ""

# Ek-ek karke har letter ko if-else se badalna
for char in text:
    if char == "a":
        secret_text += "b"
    elif char == "b":
        secret_text += "c"
    elif char == "c":
        secret_text += "d"
    elif char == "d":
        secret_text += "e"
    elif char == "e":
        secret_text += "f"
    elif char == "h":
        secret_text += "i"
    elif char == "l":
        secret_text += "m"
    elif char == "o":
        secret_text += "p"
    # Agar koi aisa letter hai jo upar nahi likha, toh woh same rahega
    else:
        secret_text += char

print("🔒 Secret Code:", secret_text)
 
