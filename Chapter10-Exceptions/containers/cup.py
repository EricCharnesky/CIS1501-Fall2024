class Cup:

    def __init__(self, maximum_volume_in_milliliters):
        self._maximum_volume_in_milliliters = maximum_volume_in_milliliters
        self._current_volume_in_milliliters = 0

    def drink(self, milliliters_to_drink):
        if milliliters_to_drink > self._current_volume_in_milliliters:
            raise ValueError("Not enough current volume")
        self._current_volume_in_milliliters -= milliliters_to_drink

    def fill(self, milliliters_to_fill):
        if milliliters_to_fill + self._current_volume_in_milliliters > self._maximum_volume_in_milliliters:
            raise ValueError("cup will overflow!")
        self._current_volume_in_milliliters += milliliters_to_fill

    # https://umgpt.umich.edu/
    # prompt: please write the get functions for the attributes of this class
    #
    # class Cup:
    #
    #     def __init__(self, maximum_volume_in_milliliters):
    #         self._maximum_volume_in_milliliters = maximum_volume_in_milliliters
    #         self._current_volume_in_milliliters = 0

    # Getter function for maximum_volume_in_milliliters
    def get_maximum_volume_in_milliliters(self):
        return self._maximum_volume_in_milliliters

    # Getter function for current_volume_in_milliliters
    def get_current_volume_in_milliliters(self):
        return self._current_volume_in_milliliters


if __name__ == "__main__":
    print("Hi from cup")