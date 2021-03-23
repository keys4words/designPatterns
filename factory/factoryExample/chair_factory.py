from medium_chair import MediumChair
from small_chair import SmallChair
from big_chair import BigChair


class ChairFactory:
    "The Factory Class"

    @staticmethod
    def get_chair(chair):
        "A static method to get a chair"
        if chair == "BigChair":
            return BigChair()
        if chair == "MediumChair":
            return MediumChair()
        if chair == "SmallChair":
            return SmallChair()
        return None
