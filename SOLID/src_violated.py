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
        
if __name__=="__main__":
    d = Duck('jonny')
    e = Duck('Kelly')
    d.greet(e)