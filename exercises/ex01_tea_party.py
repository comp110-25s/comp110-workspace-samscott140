"""Calculate the total cost of a tea party"""

__author__: str = "730650345"


def main_planner(guests: int) -> None:
    """Entrypoint of the program"""
    print("A Cozy Tea Party For", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print(
        "Cost: $", cost(tea_count=tea_bags(guests), treat_count=treats(guests)), sep=""
    )


def tea_bags(people: int) -> int:
    """Determines the number of teabags based on the number of guests"""
    return 2 * people


def treats(people: int) -> int:
    """Determines number of treats needed"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the total cost of tea bags and treats combined"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
