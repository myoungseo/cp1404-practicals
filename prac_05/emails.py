'''
function extract_name_from_email(email)
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name

email_to_name = {}

email = input("Email: ").strip()
while email != ""
    suggested_name = extract_name_from_email(email)
    confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

    if confirmation and confirmation != 'y'
        name = input("Name: ").strip()
    else
        name = suggested_name

    email_to_name[email] = name
    email = input("Email: ").strip()

print("\nStored Emails and Names:")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
'''
def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name

email_to_name = {}

email = input("Email: ").strip()
while email != "":
    suggested_name = extract_name_from_email(email)
    confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

    if confirmation and confirmation != 'y':
        name = input("Name: ").strip()
    else:
        name = suggested_name

    email_to_name[email] = name
    email = input("Email: ").strip()

print("\nStored Emails and Names:")
for email, name in email_to_name.items():
    print(f"{name} ({email})")