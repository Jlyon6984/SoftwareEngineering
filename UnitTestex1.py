import unittest

# Parent class
class Animal:
    def __init__(self, animal_name):
        self.name = animal_name

    def speak(self):
        return "Some generic sound"

    def __str__(self):
        return f"Animal with name: {self.name}"

# Child class
class Dog(Animal):
    def __init__(self, dog_name, dog_breed):
        super().__init__(dog_name)
        self.breed = dog_breed

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"Dog of breed {self.breed} named {self.name}"
    

# Creating an instance of Animal
generic_animal = Animal("GenericAnimal")
print(generic_animal)  # Output: Animal with name: GenericAnimal
print(generic_animal.speak())  # Output: Some generic sound

# Creating an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog)  # Output: Dog of breed Golden Retriever named Buddy
print(my_dog.speak())  # Output: Woof!



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


class TestDog(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.dog = Dog("Buddy", "Golden Retriever")

    def test_dog_init(self):
        """Test the initialization of the Dog class."""
        self.assertEqual(self.dog.name, "Buddy")
        self.assertEqual(self.dog.breed, "Golden Retriever")

    def test_dog_speak(self):
        """Test the speak method of the Dog class."""
        self.assertEqual(self.dog.speak(), "Woof!")

    def test_dog_str(self):
        """Test the string representation of the Dog class."""
        self.assertEqual(str(self.dog), "Dog of breed Golden Retriever named Buddy")

# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main()
