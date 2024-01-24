import math as m


class Sphere:

    def __init__(self, radius=None, x=0, y=0, z=0):
        if radius is None:
            # Unit radius
            self.radius = 1
            # Center at the origin
            self.center = (0, 0, 0)
        else:
            try:
                # Attempt to convert input values to integers
                self.radius = int(radius)
                self.center = (int(x), int(y), int(z))
            except ValueError:
                print("Invalid input. Please enter numeric"
                      " values for radius and center.")
                # Set default values in case of invalid input
                self.radius = 1
                self.center = (0, 0, 0)

    def get_volume(self):
        return (4 / 3) * m.pi * self.radius ** 3

    def get_square(self):
        return m.pi * self.radius**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        # Check if the radius is a valid value
        if radius > 0:
            self.radius = radius
            print("Radius set successfully.")
        else:
            print("Invalid radius. Please provide a positive value.")

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = m.sqrt((x - self.center[0]) ** 2
                          + (y - self.center[1]) ** 2
                          + (z - self.center[2]) ** 2)
        return distance <= self.radius


# Example of using:

# Creating a sphere with a unit radius and centered at the origin
sphere_one = Sphere()

# The volume output
print(sphere_one.get_volume())

# Checking whether a point is inside the sphere
print(sphere_one.is_point_inside(0.7, 0.7, 0.7))

# Creating a sphere with a specified radius and center coordinates
sphere_two = Sphere(radius=3, x=4, y=6, z=3)  #

# The output of the surface area
print(sphere_two.get_square())

# The output of the center coordinates
print(sphere_two.get_center())

# Setting a new radius
sphere_two.set_radius(4)

# The output of the new radius
print(sphere_two.get_radius())
