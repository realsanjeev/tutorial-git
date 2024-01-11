from LSP import SimpleConversation, Communicator
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_sound(self) -> str:
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class SwimmingBird(Bird):
    @abstractmethod
    def swim(self):
        pass

class Crow(FlyingBird):
    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def do_sound(self) -> str:
        return "Caw"

class Duck(SwimmingBird, FlyingBird):
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

if __name__=="__main__":
    duck1 = Duck("Rosi")
    duck2 = Duck("Aasutosh")
    c = SimpleConversation(duck1, duck2)
    communicator = Communicator("Mobile")
    communicator.communicate(c)
