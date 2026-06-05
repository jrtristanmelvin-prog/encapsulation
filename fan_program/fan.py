class Fan:
    # Constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Getters
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on

    # Setters
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

    # Display method
    def display(self):
        return (
            f"Speed: {self.__speed}\n"
            f"Radius: {self.__radius}\n"
            f"Color: {self.__color}\n"
            f"On: {self.__on}"
        )

class SmartFan(Fan):
    def __init__(self, speed=Fan.SLOW, radius=5.0, color="blue", on=False, wifi=False):
        super().__init__(speed, radius, color, on)
        self.__wifi = wifi

    # Getter
    def get_wifi(self):
        return self.__wifi

    # Setter
    def set_wifi(self, wifi):
        self.__wifi = wifi

    # Override display method (Polymorphism)
    def display(self):
        return super().display() + f"\nWiFi Enabled: {self.__wifi}"