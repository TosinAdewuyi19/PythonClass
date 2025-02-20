class AirCondition:
    def __init__(self):
        self.is_on = False
        self.temperature = 24


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False

    def increase_temperature(self):
        if self.is_on and self.temperature < 30:
            self.temperature += 1

    def decrease_temperature(self):
        if self.is_on and self.temperature > 16:
            self.temperature -= 1

    def get_temperature(self):
        return self.temperature

    def get_status(self):
        if self.is_on:
            return "On"




