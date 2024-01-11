class Duck:
    def __init__(self, name):
        self.name = name
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

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

if __name__ == "__main__":
    d = Duck("Roney")
    e = Duck("Louis")
    c = Communicator("SOLID")
    c.communicate(d, e)
