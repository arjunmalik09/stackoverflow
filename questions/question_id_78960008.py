from dataclasses import dataclass
from dataclasses import field

@dataclass
class ZooAnimals():
    food_daily_kg: int
    price_food: float
    area_required: float
    name: str = field(default='Zebra', kw_only=True)

c = ZooAnimals(565, 40, 10, name='Monkey')

@dataclass
class Cats(ZooAnimals):
    meowing: str
    def __init__(self, meowing, food_daily_kg, price_food, area_required, name):
        self.meowing = meowing
        super().__init__(food_daily_kg, price_food, area_required, name=name)

z = Cats('Little Bit', 465, 30, 10, name='Leopard')
