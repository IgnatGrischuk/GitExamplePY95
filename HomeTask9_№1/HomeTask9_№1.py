class Soda:

    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        return f"You got soda with {self.flavor} flavor" if self.flavor \
            else "You got soda with ordinary flavor"


soda_with_flavor = Soda(flavor="strawberry")
print(soda_with_flavor)

ordinary_flavor = Soda()
print(str(ordinary_flavor))
