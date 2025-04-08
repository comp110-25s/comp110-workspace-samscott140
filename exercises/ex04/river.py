"""File to define River class."""

__author__: str = "730650345"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        bears_surv: list[Bear] = []
        fish_surv: list[Fish] = []
        i: int = 0
        ii: int = 0
        while i < len(self.fish):
            if self.fish[i].age <= 3:
                fish_surv.append(self.fish[i])
        while ii < len(self.bears):
            if self.bears[ii].age <= 5:
                bears_surv.append(self.bears[i])
        self.fish = fish_surv
        self.bears = bears_surv

        return None

    def remove_fish(self, amount: int):
        i: int = 0
        while i <= amount:
            self.fish.pop(0)
            i += 1
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bear_list.append(bear)
        self.bears = bear_list
        return None

    def repopulate_fish(self):
        n: int = len(self.fish)
        i: int = 0
        while i < ((n // 2) * 4):
            self.fish.append(Fish())
            i += 1
        return None

    def repopulate_bears(self):
        n: int = len(self.bears)
        i: int = 0
        while i < (n // 2):
            self.bears.append(Bear())
            i += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate 1 week of life in the river"""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
