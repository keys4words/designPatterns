from furniture_factory import FurnitureFactory

furniture = FurnitureFactory.get_furniture('SmallChair')
print(f'{furniture.__class__}: {furniture.get_dimensions()}')

furniture2 = FurnitureFactory.get_furniture('BigTable')
print(f'{furniture2.__class__}: {furniture2.get_dimensions()}')
