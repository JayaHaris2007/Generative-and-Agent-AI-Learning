email = input("Enter your email address: ")

def is_valid_email(email):
    
    if "@" not in email or "." not in email:
        return False   
    
    name , domain = email.split("@", 1)

    if not name or not domain:
        return False
    
    if domain.startswith(".") or domain.endswith("."):
        return False

    return True

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")