from igloo_director import IglooDirector
from castle_director import CastleDirector
from houseboat_director import HouseBoatDirector


igloo = IglooDirector.construct()
castle = CastleDirector.construct()
houseboat = HouseBoatDirector.construct()

print(igloo.construction())
print(castle.construction())
print(houseboat.construction())