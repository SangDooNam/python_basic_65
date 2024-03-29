#!/usr/bin/env python


class AquariumApp:
    def __init__(self, fish_count, eye_color, skin_color):
        self.skin_color = skin_color
        self.__private_swim_count = 0
        self.eye_color = eye_color
        self._protected_dead_fish = 0
        self.fish_count = fish_count

    def _start(self):
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self.__private_swim_count += 1

        print(
            str(self.fish_count)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.skin_color
            + "."
        )
        print(
            "There are "
            + str(self._protected_dead_fish)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self.__private_swim_count)
            + " times."
        )

    def __die_fish(self, number):
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        self.fish_count -= number
        self._protected_dead_fish += number
        if number > 1:
            print(str(number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    my_aquarium_app = AquariumApp(5, "blue", "red")
    my_aquarium_app._start()
    my_aquarium_app._AquariumApp__die_fish(2)
    my_aquarium_app._start()
    my_aquarium_app._AquariumApp__die_fish(1)
    my_aquarium_app._start()
    my_aquarium_app._AquariumApp__die_fish(2)
    my_aquarium_app._start()
    my_aquarium_app._AquariumApp__die_fish(1)
