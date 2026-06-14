from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def cost(self) -> int:
        return 100

    def description(self) -> str:
        return "Coffee"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> int:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


class MilkDecorator(CoffeeDecorator):
    def cost(self) -> int:
        return super().cost() + 30

    def description(self) -> str:
        return super().description() + ", milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self) -> int:
        return super().cost() + 10

    def description(self) -> str:
        return super().description() + ", sugar"


class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self) -> int:
        return super().cost() + 50

    def description(self) -> str:
        return super().description() + ", whipped cream"

    
if __name__ == "__main__":
    coffee = SimpleCoffee()
    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)

    print(coffee.description())
    print(coffee.cost())       