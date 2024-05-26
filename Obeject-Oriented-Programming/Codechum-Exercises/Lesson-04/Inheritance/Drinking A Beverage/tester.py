from beverage import Beverage
from water import Water
from beer import Beer
def test_beverages():
    # Test Beverage class
    beverage = Beverage("Juice", 500, True)
    print(beverage)  # Juice (500mL) is still chilled
    print(beverage.is_empty())  # False
    print(beverage.get_name())  # Juice
    print(beverage.get_volume())  # 500
    print(beverage.get_is_chilled())  # True

    # Test Water class
    water = Water(750, True, "Purified")
    print(water)  # Water (750mL) is still chilled
    print(water.is_empty())  # False
    print(water.get_name())  # Water
    print(water.get_volume())  # 750
    print(water.get_is_chilled())  # True
    print(water.get_type())  # Purified

    # Test default type in Water class
    default_water = Water(500, False, "")
    print(default_water.get_type())  # Regular

    # Test Beer class
    beer = Beer(330, True, 0.045)
    print(beer)  # Beer (330mL) is still chilled (4.5% alcoholic content)
    print(beer.is_empty())  # False
    print(beer.get_name())  # Beer
    print(beer.get_volume())  # 330
    print(beer.get_is_chilled())  # True
    print(beer.get_type())  # Regular
    print(beer.get_alcoholic_content())  # 0.045

    # Test type categorization in Beer class
    flavored_beer = Beer(330, True, 0.02)
    strong_beer = Beer(330, True, 0.08)
    print(flavored_beer.get_type())  # Flavored
    print(strong_beer.get_type())  # Strong

test_beverages()