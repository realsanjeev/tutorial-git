from typing import final

class Duck:
    def __init__(self, name):
        self.name = name
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

class AbstractConversation:
    def do_conversation(self) -> list:
        pass

class SimpleConversation(AbstractConversation):
    def __init__(self, duck1: Duck, duck2: Duck):
        self.duck1 = duck1
        self.duck2 = duck2

    def do_conversation(self) -> list:
        sentence1 = f"{self.duck1.name}: {self.duck1.do_sound()}, hello {self.duck2.name}"
        sentence2 = f"{self.duck2.name}: {self.duck2.do_sound()}, hello {self.duck1.name}"
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
