def create_user_profile(name,age,race,height,location,age_intersted_on,occopation="Student",intersts=None):
    """ Create user profile with optional interset.
    Args:
        name(str): the user's name required.
        age(int) : the user age (required).
        occopation(str,optional): The users occopation(defaults to "student").
        interest(list,optional): alist of a user's intersets(default to None).
    """
    if intersts is None: # Intializing if None
    	interset = []
    profile = {
        "name": name,
        "age": age,
        "race" : race,
        "height" :int(height),
        "location": location,
        "age intersted on ":age_intersted_on,
        "occopation":occopation,
        "interset": intersts
    }
    return profile
user1 = create_user_profile("Alula",25,"Black",16.5,"USA","34 to 45","Software Enginer",intersts=["Coding","Highking"])
#user2 = create_user_profile("Zukas",18)#this uses default occopation and no intrest
#user3 = create_user_profile("Carlo",30,intersts=["Gardining","Reading"])

print(user1)
#print(user2)
#print(user3)