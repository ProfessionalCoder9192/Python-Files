class Dog:
    # Class variable
    animal = "Dog"

    # Constructor
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    # Method to display details
    def display_details(self):
        print("Animal Type:", Dog.animal)
        print("Breed:", self.breed)
        print("Color:", self.color)
        print("-" * 25)


# Creating two different dog objects
dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

# Displaying details
dog1.display_details()
dog2.display_details()