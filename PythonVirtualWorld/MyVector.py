from math import ceil, sqrt

class MyVector:

    def __init__(self, y: int, x: int):

        self.__y = y
        self.__x = x


    def getY(self) -> int:

        return self.__y


    def getX(self) -> int:

        return self.__x


    def __eq__(self, other):

        return self.getX() == other.getX() and self.getY() == other.getY()


    def __add__(self, other):

        return MyVector(self.getY() + other.getY(), self.getX() + other.getX())

    def __sub__(self, other):

        return MyVector(self.getY() - other.getY(), self.getX() - other.getX())

    def outside(self, height, width) -> bool:

        return self.__y < 0 or self.__x < 0 or self.__y >= height or self.__x >= width

    def len(self):
        return sqrt(self.__y**2 + self.__x**2)

    def normalised(self):
        len = self.len()

        return MyVector(ceil(self.__y/len), ceil(self.__x/len))
