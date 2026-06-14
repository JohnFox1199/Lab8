from decorators import (
    SimpleCoffee,
    MilkDecorator,
    SugarDecorator,
    WhippedCreamDecorator,
)


def test_simple_coffee():
    coffee = SimpleCoffee()
    assert coffee.description() == "Coffee"
    assert coffee.cost() == 100


def test_coffee_with_milk_and_sugar():
    coffee = SimpleCoffee()
    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)

    assert coffee.description() == "Coffee, milk, sugar"
    assert coffee.cost() == 140


def test_coffee_with_all_toppings():
    coffee = SimpleCoffee()
    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)
    coffee = WhippedCreamDecorator(coffee)

    assert coffee.description() == "Coffee, milk, sugar, whipped cream"
    assert coffee.cost() == 190