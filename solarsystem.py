import itertools
import math
import turtle


class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(self, solar_system, mass, shape, position=(0, 0), velocity=(0, 0)):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.speed(1)
        self.shape(shape)

        solar_system.add_body(self)

    def draw(self):
        self.clear()
        self.display_size = self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )

    def move(self):
        self.speed(1)
        self.goto(self.xcor() + self.velocity[0],
                  self.ycor() + self.velocity[1])

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass


class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, "Assets/sun.gif", position, velocity)
        self.color("yellow")
        self.speed(1)


class Planet(SolarSystemBody):
    colours = itertools.cycle(["red", "green", "blue"])

    def __init__(self, solar_system, mass, shape, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, shape, position, velocity)
        self.color(next(Planet.colours))
        self.speed(1)


class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.screensize(10000, 10000)
        self.solar_system.bgcolor("black")
        self.solar_system.bgpic("Assets/Backgrounds/background3.png")
        self.solar_system.addshape("Assets/sun.gif")
        self.solar_system.addshape("Assets/earth.gif")
        self.solar_system.addshape("Assets/jupiter.gif")
        self.solar_system.addshape("Assets/mars.gif")
        self.solar_system.addshape("Assets/mercury.gif")
        self.solar_system.addshape("Assets/neptune.gif")
        self.solar_system.addshape("Assets/saturn.gif")
        self.solar_system.addshape("Assets/uranus.gif")
        self.solar_system.addshape("Assets/venus.gif")
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        body.clear()
        self.bodies.remove(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    @staticmethod
    def accelerate_due_to_gravity(first: SolarSystemBody, second: SolarSystemBody):
        G = 6.67 * 10 ** -2
        force = G * first.mass * second.mass / first.distance(second) ** 2
        angle = first.towards(second)
        reverse = 1
        for body in first, second:
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y),
            )
            reverse = -1

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.accelerate_due_to_gravity(first, second)
