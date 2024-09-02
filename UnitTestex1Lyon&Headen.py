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
    
# Child class - Cat
class Cat(Animal):
    def __init__(self, cat_name, color, age):
        super().__init__(cat_name)
        self.color = color
        self.age = age

    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"Cat with color {self.color} named {self.name}"
    
    def ReturnAge(self):
        return self.age

# Child class - Bird
class Bird(Animal):
    def __init__(self, bird_name, species, age):
        super().__init__(bird_name)
        self.species = species
        self.age = age

    def speak(self):
        return "Chirp!"

    def __str__(self):
        return f"Bird of species {self.species} named {self.name}"
    
    def ReturnAge(self):
        return self.age
        
    

# Creating instances of Animal, Dog, Cat, and Bird
generic_animal = Animal("GenericAnimal")
print(generic_animal)  # Output: Animal with name: GenericAnimal
print(generic_animal.speak())  # Output: Some generic sound
print(generic_animal.ReturnAge())

my_dog = Dog("Buddy", "Golden Retriever", 6)
print(my_dog)  # Output: Dog of breed Golden Retriever named Buddy
print(my_dog.speak())  # Output: Woof!
print(my_dog.ReturnAge())

my_cat = Cat("Whiskers", "Gray", 3)
print(my_cat)  # Output: Cat with color Gray named Whiskers
print(my_cat.speak())  # Output: Meow!
print(my_cat.ReturnAge())

my_bird = Bird("Tweety", "Canary", 1)
print(my_bird)  # Output: Bird of species Canary named Tweety
print(my_bird.speak())  # Output: Chirp!
print(my_bird.ReturnAge())


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
        self.dog = Dog("Buddy", "Golden Retriever", 6)

    def test_dog_init(self):
        """Test the initialization of the Dog class."""
        self.assertEqual(self.dog.name, "Buddy")
        self.assertEqual(self.dog.breed, "Golden Retriever")
        self.assertEqual(self.dog.age, 6)

    def test_dog_speak(self):
        """Test the speak method of the Dog class."""
        self.assertEqual(self.dog.speak(), "Woof!")

    def test_dog_str(self):
        """Test the string representation of the Dog class."""
        self.assertEqual(str(self.dog), "Dog of breed Golden Retriever named Buddy")
        
    def test_dog_age(self):
        """Test the age method of the Dog class."""
        self.assertEqual(self.dog.ReturnAge(), 6)


class TestCat(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.cat = Cat("Whiskers", "Gray", 3)

    def test_cat_init(self):
        """Test the initialization of the Cat class."""
        self.assertEqual(self.cat.name, "Whiskers")
        self.assertEqual(self.cat.color, "Gray")
        self.assertEqual(self.cat.age, 3)

    def test_cat_speak(self):
        """Test the speak method of the Cat class."""
        self.assertEqual(self.cat.speak(), "Meow!")

    def test_cat_str(self):
        """Test the string representation of the Cat class."""
        self.assertEqual(str(self.cat), "Cat with color Gray named Whiskers")
        
    def test_cat_age(self):
        """Test the age method of the Cat class."""
        self.assertEqual(self.cat.ReturnAge(), 3)


class TestBird(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.bird = Bird("Tweety", "Canary", 1)

    def test_bird_init(self):
        """Test the initialization of the Bird class."""
        self.assertEqual(self.bird.name, "Tweety")
        self.assertEqual(self.bird.species, "Canary")
        self.assertEqual(self.bird.age, 1)

    def test_bird_speak(self):
        """Test the speak method of the Bird class."""
        self.assertEqual(self.bird.speak(), "Chirp!")

    def test_bird_str(self):
        """Test the string representation of the Bird class."""
        self.assertEqual(str(self.bird), "Bird of species Canary named Tweety")
        
    def test_bird_age(self):
        """Test the age method of the Bird class."""
        self.assertEqual(self.bird.ReturnAge(), 1)


# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main()