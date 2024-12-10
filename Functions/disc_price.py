from enum import Enum, auto

class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()

def get_discounted_price(cart_weight, total_price, discount_type):
    pass

print(get_discounted_price(12, 100, DiscountType.WEIGHT))