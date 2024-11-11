class Mug:

    def __init__(self, maximum_volume_in_milliliters):
        self._maximum_volume_in_milliliters = maximum_volume_in_milliliters
        self._current_volume_in_milliliters = 0
        self.has_handle = True