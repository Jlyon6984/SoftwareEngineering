import unittest

# Parent class
class Animal:
    def __init__(self, animal_name):
        self.name = animal_name

    def speak(self):
        return "Some generic sound"

    def __str__(self):
        return f"Animal with name: {self.name}"
    
    def ReturnAge(self):
        return "I am an age"

# Child class
class Dog(Animal):
    def __init__(self, dog_name, dog_breed,age):
        super().__init__(dog_name)
        self.breed = dog_breed
        self.age = 6

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"Dog of breed {self.breed} named {self.name}"
    
    def ReturnAge(self):
        return self.age
        
    

# Creating an instance of Animal
generic_animal = Animal("GenericAnimal")
print(generic_animal)  # Output: Animal with name: GenericAnimal
print(generic_animal.speak())  # Output: Some generic sound
print(generic_animal.ReturnAge())

# Creating an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever", 6)
print(my_dog)  # Output: Dog of breed Golden Retriever named Buddy
print(my_dog.speak())  # Output: Woof!
print(my_dog.ReturnAge())



# Unit tests
class TestAnimal(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.animal = Animal("Generic Animal")

    def test_animal_init(self):
        """Test the initialization of the Animal class."""
        self.assertEqual(self.animal.name, "Generic Animal")

    def test_animal_speak(self):
        """Test the speak method of the Animal class."""
        self.assertEqual(self.animal.speak(), "Some generic sound")

    def test_animal_str(self):
        """Test the string representation of the Animal class."""
        self.assertEqual(str(self.animal), "Animal with name: Generic Animal")
        
    def test_animal_age(self):
        """Test the age method of the Animal class."""
        self.assertEqual(self.animal.ReturnAge(), "I am an age")


class TestDog(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.dog = Dog("Buddy", "Golden Retriever",6)

    def test_dog_init(self):
        """Test the initialization of the Dog class."""
        self.assertTrue(self.dog.name, "Buddy")
        self.assertEqual(self.dog.breed, "Golden Retriever")

    def test_dog_speak(self):
        """Test the speak method of the Dog class."""
        self.assertEqual(self.dog.speak(), "Woof!")

    def test_dog_str(self):
        """Test the string representation of the Dog class."""
        self.assertEqual(str(self.dog), "Dog of breed Golden Retriever named Buddy")
        
    def test_dog_str(self):
        """Test the age method of the Dog class."""
        self.assertTrue(self.dog.ReturnAge,6)

# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main()
