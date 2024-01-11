from typing import final
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def fly(cls):
        pass

    @abstractmethod
    def swim(cls):
        pass

    @abstractmethod
    def do_sound(cls) -> str:
        pass

class Duck(Bird):
    def __init__(self, name):
        super().__init__(name)
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

class Crow(Bird):
    def __init__(self, name):
        super().__init__(name)
   
    def fly(self):
        print(f"{self.name} is flying not very high")
    
    def swim(self):
        raise NotImplementedError("Crow don't swim")

    def do_sound(self) -> str:
        return "Cowwwww!"

class AbstractConversation:
    def do_conversation(self) -> list:
        pass

class SimpleConversation(AbstractConversation):
    def __init__(self, bird1: Bird, bird2: Bird):
        self.bird1 = bird1
        self.bird2 = bird2

    def do_conversation(self) -> list:
        sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, hello {self.bird2.name}"
        sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, hello {self.bird1.name}"
        return [sentence1, sentence2]

class Communicator:  
    def __init__(self, channel):
        self.channel = channel

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
              f"(via {self.channel})",
              sep='\n')

if __name__ == "__main__":
    d = Duck('Jon')
    e = Duck('lil')
    c = SimpleConversation(d, e)
    communicator = Communicator("OPS")
    communicator.communicate(c)
    print("[INFO]: Now crow are communicating")
    crow1 = Crow('Crow R')
    crow2 = Crow('Crow A')
    c_crow = SimpleConversation(crow1, crow2)
    communicator.communicate(c_crow)