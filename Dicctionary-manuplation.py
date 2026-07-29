contacts = {} # create contacts dict 

def add_contacts(name,phone_number):
    contacts[name] = phone_number
    print (name, phone_number)
    return contacts

add_contacts("Alicice","901-678-0000")
add_contacts("David","890-789-0000")
add_contacts("Ganja","906-787-1111")
add_contacts("Coco","890-090-2020")
print(contacts) # this will print out dict
for name, phone_number in contacts.items(): #looping by copying items in contacts to print 
    print(f"Name {name} attached contact number {phone_number}")
