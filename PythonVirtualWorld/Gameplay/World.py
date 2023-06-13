import copy
from random import randint

from ..Tools.Notifications import Notifications
from ..Tools.MyVector import MyVector
from Organisms.Organism import Organism
from Organisms.Animals import Antelope, CyberSheep, Sheep, Human, Wolf, Turtle, Fox
from Organisms.Plants import Dandelion, NightShade, PineBorsht, Grass, Guarana
from enum import Enum

class World:

    class Move(Enum):
        Up = 0
        Down = 1
        Left = 2
        Right = 3
        Ult = 4
        Stand = 5

    def __init__(self, height: int, width: int, organisms=None):

        if organisms is None:
            organisms = []
        else:
            for org in organisms:
                org.setWorld(self)

        self.__height = height
        self.__width = width
        self.__organisms = organisms
        self.__round = 0
        self.__nots = Notifications()
        self.__move = World.Move.Stand


    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getOrganisms(self):
        return self.__organisms

    def getRound(self):
        return self.__round

    def getNots(self):
        return self.__nots

    def getMove(self):
        return self.__move


    def setRound(self, value):
        self.__round = value

    def setMove(self, move : Move):
        self.__move = move

    def popMove(self):

        tmp = copy.deepcopy(self.__move)
        self.__move = World.Move.Stand

        return tmp


    def addOrg(self, org: Organism):
        org.setWorld(self)
        self.__organisms.append(org)
  

    def getCollision(self, org):

        tmp =  [x for x in self.__organisms if x.getPosition() == org.getPosition() and x != org]

        if len(tmp):
            return tmp[0]

        return None


    def __actions(self):

        self.__organisms = sorted(self.__organisms,reverse=True, key= lambda x: x.getAge())
        self.__organisms = sorted(self.__organisms, reverse=True, key= lambda x: x.getInitiative())

        for org in self.__organisms:

            if org.isAlive():

                org.action()
                org.collision()

            org.ageUp()


    def runRound(self):

        self.__nots.clear()

        for org in self.__organisms:
            org.newRound()

        self.__round+=1
        self.__actions()

        self.__organisms = [x for x in self.__organisms if x.isAlive()]


    def getOrganismAt(self, position : MyVector) -> Organism:

        wanted = None

        for org in self.__organisms:

            if org.getPosition() == position and org.isAlive():

                if wanted is None or wanted.getStrength() < org.getStrength():

                    wanted = org

        return wanted


    def getFreeSquare(self, position : MyVector, range = 1):

        for dy in [-1 * range, 0, range]:

            for dx in [-1 * range, 0, range]:

                point =  MyVector(dy,dx) + position

                if point != position \
                        and self.getOrganismAt(point) is None \
                        and not point.outside(self.getHeight(),self.getWidth()):
                    return point

        return position


    def getFreeRandomSquare(self, position : MyVector, range = 1):

        points = []

        for dy in [-1 * range, 0, range]:

            for dx in [-1 * range, 0, range]:

                point =  MyVector(dy, dx) + position

                if point != position \
                        and self.getOrganismAt(point) is None \
                        and not point.outside(self.getHeight(),self.getWidth()):
                    points.append(point)

        if len(points):
            return points[randint(0,len(points) - 1)]

        return None

    def basic(self):
        w = World(20, 20)
        w.addOrg(Wolf(1, 1))
        w.addOrg(Wolf(3, 1))

        w.addOrg(Turtle(5, 5))
        w.addOrg(Turtle(7, 5))

        w.addOrg(Sheep(10, 7))
        w.addOrg(Sheep(13, 7))

        w.addOrg(Fox(15, 10))
        w.addOrg(Fox(17, 10))

        w.addOrg(Antelope(18, 12))
        w.addOrg(Antelope(19, 12))

        w.addOrg(CyberSheep(2, 8))
        w.addOrg(CyberSheep(12, 6))

        w.addOrg(Dandelion(19, 0))
        w.addOrg(Dandelion(19, 19))

        w.addOrg(Grass(1, 10))
        w.addOrg(Grass(19, 10))

        w.addOrg(Guarana(10, 15))
        w.addOrg(Guarana(10, 18))

        w.addOrg(NightShade(16, 8))
        w.addOrg(NightShade(9, 15))

        w.addOrg(PineBorsht(19, 0))
        w.addOrg(PineBorsht(15, 18))

        w.addOrg(Human(10, 19))
        return w



    




