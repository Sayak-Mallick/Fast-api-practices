class Dog:
    species = "Golden Retriever"  # Shared class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        self.legs = 4
        print("init called")

    def __str__(self):
        # Defines how the object appears when printed.
        return f"{self.name} is {self.age} years old."


# Create two Dog objects.
dog1 = Dog("Buddy", 2)
dog2 = Dog("Charlie", 3)

print(dog1)
print(dog2)
print(dog1.legs)
print(dog2.legs)

# Access object attributes.
print(dog1.name)
print(dog1.age)
print(dog1.species)