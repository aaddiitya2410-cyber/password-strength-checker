

p=input("enter a password =")
if len(p)<8:
    print("Weak password,enter atleast 8 characters")
else:
    has_upper=False
    has_digit=False
    has_special=False
    
    
for char in p:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        has_upper=True
    elif char in "0123456789":
        has_digit=True
    elif char in "!@#$%^&*()_-+=/":
        has_special=True
    
if has_upper==True and has_digit==True and has_special==True:
    print("Strong password")
else:
    print("Weak password (rules do not match)")   



 
