from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow!'


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self, animal_type):
        pass


class ConcreteAnimalFactory(AnimalFactory):
    def create_animal(self, animal_type):
        if animal_type.lower() == 'dog':
            return Dog()
        elif animal_type.lower() == 'cat':
            return Cat()
        else:
            raise ValueError('Unsupported animal type.')


if __name__ == '__main__':

    factory = ConcreteAnimalFactory()
    dog = factory.create_animal('dog')
    print(dog.speak())

    cat = factory.create_animal('cat')
    print(cat.speak())
