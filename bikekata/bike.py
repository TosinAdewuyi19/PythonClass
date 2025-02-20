class Bike:
    def __init__(self):
        self.is_on = False
        self.speed = 0
        self.gear = 1

    def turn_on(self):
        self.is_on = True

    def Turn_off(self):
        self.is_on = False

    def get_status(self):
        return self.is_on

    def accelerate(self):
        if self.is_on:
            if self.gear == 1:
                self.speed += 1
            elif self.gear == 2:
                self.speed += 2
            elif self.gear == 3:
                self.speed += 3
            elif self.gear == 4:
                self.speed += 4
            self.update_gear()

    def decelerate(self):
        if self.is_on:
            if self.gear == 1:
                self.speed -= 1
            elif self.gear == 2:
                self.speed -= 2
            elif self.gear == 3:
                self.speed -= 3
            elif self.gear == 4:
                self.speed -= 4
            self.update_gear()

    def get_speed(self):
        return self.speed

    def get_gear(self):
        return self.gear

    def update_gear(self):
        if self.speed <= 20:
            self.gear = 1
        elif 21 <= self.speed <= 30:
            self.gear = 2
        elif 31 <= self.speed <= 40:
            self.gear = 3
        elif self.speed >= 41:
            self.gear = 4

