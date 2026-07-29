class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
    def bark(self):
        print(f"Woof! my name is {self.name} and I'm a {self.breed}.")
    def introduce(self):
        print(f"Hi! my name is {self.name}.")
        print(f"I am a {self.breed} and I am {self.age} years old.")
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")
        
    def fetch(self, item):
        print(f"{self.name} fetched the {item}.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
dog1 = Dog("Buddy","Golden retriever", 3)
dog1.bark()
dog1.introduce()
dog1.fetch("ball")
dog1.sleep()
dog1.birthday()