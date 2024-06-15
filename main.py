import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pyPlanet")

WHITE = (255, 255, 255)
YELLOW = (255, 205, 7)
BLUE = (3, 126, 183)
ORANGE = (216, 104, 6)
SILVER = (102, 102, 102)
BEIGE = (244, 222, 155)


class Planet:
    # distance from sun
    AU = 149.6e6*1000
    # gravitational constant
    G = 6.67430e-11
    SCALE = 300 / AU  # 1AU = 100pixel
    TIMESTEP = 3600*24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            update_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                update_points.append((x, y))

            pygame.draw.lines(WINDOW, self.color, False, update_points, 2)
        pygame.draw.circle(window, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 6.95700, YELLOW, 1.9885 * 10 ** 30)
    sun.sun = True

    earth = Planet(Planet.AU, 0, 12.756, BLUE, 5.9722 * 10 ** 24)
    earth.y_vel = -29.8 * 1000

    mars = Planet(Planet.AU * 1.524, 0, 6.792, ORANGE, 6.4171 * 10 ** 23)
    mars.y_vel = -24.1 * 1000

    mercury = Planet(Planet.AU * 0.39, 0, 4.879, SILVER, 3.3011 * 10 ** 23)
    mercury.y_vel = -47.9 * 1000

    venus = Planet(Planet.AU * 0.72, 0, 12.104, BEIGE, 4.867 * 10 ** 24)
    venus.y_vel = -35.0 * 1000


    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WINDOW.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            print(str(planet.x) + " " + str(planet.y))
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()


main()
