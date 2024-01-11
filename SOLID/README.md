### SOLID 
SOLID Principles are a set of 5 principles for Object-Oriented-Programing in sofware design and good basis for developing code in collaborative environmnets. SOLID is the mnenomic cronymn for 5 different principles:
- **S**ingle Responsibility Principle(SRP)
- **O**pen-Cloased Principle(OCP)
- **L**iskov Substitution Principle(ISP)
- **I**nference Segregation Principle(ISP)
- **D**epedency Inversion Priciple(DIP)

### **Single Responsibility Principle (SRP)**
This is first principle of SOLID that states a class should be responsible for only one functionality. In other word, class should have a single reason to change.

```python
class Duck:
   
    def __init__(self, name):
        self.name = name
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

    def greet(self, duck2: 'Duck'):
        print(f"{self.name}: {self.do_sound()}, \
              hello {duck2.name}")
```
The primary purpose of this class is to encapsulate the properties and behaviors of a duck. If we need to modify its definition, we would need to alter the class itself. The issue arises in the `greet()` method, which handles communication between ducks.

To address the challenge of communication between two ducks, we introduce a new class called `Communicator`. The purpose of this class is to serve as an intermediary for communication between ducks.
```python
class Duck:
    def __init__(self, name):
        self.name = name
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

    def greet(self, duck2: 'Duck'):
        print(f"{self.name}: {self.do_sound()}, \
              hello {duck2.name}")

class Communicator:
    def __init__(self, channel):
        self.channel = channel

    def communicate(self, duck1: Duck, duck2: Duck):
        sentence1 = f"{duck1.name}: {duck1.do_sound()}, hello {duck2.name}"
        sentence2 = f"{duck2.name}: {duck2.do_sound()}, hello {duck1.name}"
        conversation = [sentence1, sentence2]
        print(*conversation,
              f"(via {self.channel})",
              sep='\n')
```
### **Open-Closed Principle (OCP)**
The Open/Closed Principle indicates the classes should be open for extension,but closed for modification. i.e, code is written in a way that it can add new functionality but that modificaation donot alter previous functionality, which may be used by other user.

In above example, it is not possible to extend the `Communicator` functionality to comunicate between different species. If we were to modify the `communicate()` method, it violates the OCP principle. So we create a general abstract class and inherit to create communicator.

```python
from typing import final

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
```

### Interface Segregation Principle (ISP)

ISP states that the client should not be forced to rely on methods they do not use and, therefore, suggests the creation of specific interfaces or classes for such clients.

In the above example, we may have methods that are not common to all birds, such as the `swim` method. This method is not valid if we want to add a bird that cannot swim. Users should not be forced to use methods that raise errors unnecessarily for a class. Therefore, we should create separate classes for flying birds and swimming birds. Then, inherit the `Duck` class from both the `FlyingBird` and `SwimmingBird` classes. If a bird can swim but cannot fly, we implement from the `SwimmingBird` class only.

### Dependency Inversion Principle(DIP)
DIP, as the last principle, can be separated into two statements. On one end, it indicates that abstractions should not depend on details, as details depend on abstractions. On the other hand, it indicates that higher-level classes should not depend on low-level classes, since both should depend on abstraction. In other words, **abstraction should depend on abstraction.**
```python
class AbstractChannel(ABC):
    @abstractmethod
    def get_channel_message(self) ->str:
        pass

class SMSChannel(AbstractChannel):
    def get_channel_message(self) -> str:
        return "(via SMS)"

class AbstractCommunicator(ABC):
    def get_channel(self) -> AbstractChannel:
        pass

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
              self.get_channel().get_channel_message(),
              sep = '\n')

class SimpleCommunicator(AbstractCommunicator):  
    def __init__(self, channel : AbstractChannel):
        self._channel = channel
   
    def get_channel(self) -> str:
        return self._channel
```
