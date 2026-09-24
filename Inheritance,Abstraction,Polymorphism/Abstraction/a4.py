from abc import ABC, abstractmethod
class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        print("Restaurant Bill: 500")

    def delivery_charge(self):
        print("Delivery Charge: 0")

class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        print("Home Delivery Bill: 500")

    def delivery_charge(self):
        print("Delivery Charge: 50")

restaurant = RestaurantOrder()
home = HomeDeliveryOrder()
restaurant.calculate_bill()
restaurant.delivery_charge()
home.calculate_bill()
home.delivery_charge()