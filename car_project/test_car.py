from car import Car

class TestCar:
    @staticmethod
    def main():

        my_car = Car(1983, "Toyota AE86")

        print("=== ACCELERATE ===")
        for i in range(5):
            my_car.accelerate()
            print("Speed:", my_car.get_speed())

        print("\n=== BRAKE ===")
        for i in range(5):
            my_car.brake()
            print("Speed:", my_car.get_speed())

TestCar.main()