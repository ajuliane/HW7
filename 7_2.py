class Clothes:
    def __init__(self, name):

        self._name = name

    @property
    def name(self):
        # if self.age self.age = 0
        return self._name

    @abstractmethod
    def consumption(self, x):
        pass

class Coat(Clothes):
    def consumption(self, x):
        consumption=(x/6.5 + 0.5)
        print(f'{self.name} requires {consumption} of the cloth')

class Suit(Clothes):
    def consumption(self, x):
        consumption=((2*x + 0.3))
        print(f'{self.name} requires {consumption} of the cloth')

my_suit = Suit('Blue Suit')
my_suit.consumption(5)

my_coat = Coat('Brown coat')
my_coat.consumption(4)