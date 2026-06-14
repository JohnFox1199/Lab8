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
    
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(coffee)