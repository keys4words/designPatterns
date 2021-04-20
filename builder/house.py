class House():
    "The Product"

    def __init__(self, building_type="Apartment", doors=0, windows=0, wall_material="Brick"):
        self.wall_material = wall_material
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        "Return a string describing the construction"
        return f"This is {self.wall_material} {self.building_type} with {self.doors} door(s) and {self.windows} window(s)."