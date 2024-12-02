
class Mammal:

    def __init__(self, sound, height):
        self.sound = sound
        self.height = height

    def make_noise(self):
        print(self.sound)

class Gorilla(Mammal):

    def __init__(self, sound, height, fur_color):
        super().__init__(sound, height)
        self.fur_color = fur_color

    def climb(self):
        print('climb')


class Human(Mammal):

        def __init__(self, sound, height, eye_color):
            super().__init__(sound, height)
            self.eye_color = eye_color

        def smile(self):
            print("smile")


eric = Human("happy monday", 6, 'hazel')

eric.make_noise()
eric.smile()


class Polygon:

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.side_lengths = []
        for side in range(number_of_sides):
            self.side_lengths.append(0)

    def set_side_length(self, side_index, length):
        self.side_lengths[side_index] = length

    # assumes it's a closed shape
    def perimeter(self):
        return sum(self.side_lengths)

    def get_area(self):
        raise NotImplemented

class Rectangle(Polygon):

    def __init__(self, length = 0, width = 0):
        super().__init__(4)
        self.set_side_length(0, length)
        self.set_side_length(1, width)

    def set_side_length(self, side_index, length):
        if side_index % 2: # means it's not 0
            super().set_side_length(1, length)
            super().set_side_length(3, length)
        else:
            super().set_side_length(0, length)
            super().set_side_length(2, length)

    def set_width(self, width):
        self.set_side_length(1, width)

    def set_length(self, length):
        self.set_side_length(0, length)

    def get_area(self):
        return self.side_lengths[0] * self.side_lengths[1]

class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def set_side_length(self, side_index, length):
        super().set_side_length(0, length)
        super().set_side_length(1, length)

    def set_length(self, length):
        super().set_width(length)
        super().set_length(length)

    def set_width(self, width):
        super().set_width(width)
        super().set_length(width)




polygon = Polygon(7)
polygon.set_side_length(0, 5)

rectangle = Rectangle(3, 2)

square = Square(4)

print(polygon.perimeter())
print(rectangle.perimeter())
print(square.perimeter())

print(rectangle.get_area())
print(square.get_area())


