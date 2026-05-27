def search_phone(phone_number):
    print(f"[*] sorry, bad module: {phone_number}")
    dork = f'"{phone_number}" OR "{phone_number[:3]} {phone_number[3:]}"'
    return f"https://www.google.com/search?q={dork}"