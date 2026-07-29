email_phone = {}

def profile_contact(name,email,phone_num):
    email_phone["name"] = {
        "email": email,
        "phone": phone_num
    }
    print(name,email,phone_num)
    return email_phone

profile_contact("Alice", "alice@gmail.com", "901-678-0000")
profile_contact("David", "david@gmail.com", "890-789-0000")
profile_contact("Ganja", "ganja@gmail.com", "906-787-1111")
profile_contact("Coco", "coco@gmail.com", "890-090-2020")

