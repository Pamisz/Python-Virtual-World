from ....Tools.MyVector import MyVector
from ..Organism import Organism
from ..Plant import Plant


class Guarana(Plant):


    STRENGTH = 0
    BOOST = 3

    def __init__(self, position : MyVector):
        super().__init__(position, Guarana.STRENGTH)

    def giveMod(self, other : Organism):

        other.setStrength(other.getStrength() + Guarana.BOOST)

    def draw(self) -> str:

        return "magenta"


    def __str__(self):

        return "GUARANA"

