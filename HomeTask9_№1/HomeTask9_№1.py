class Soda:

    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"You got soda with {self.flavor} flavor"
        else:
            return f"You got soda with ordinary flavor"


soda_with_flavor = Soda(flavor="strawberry")
print(soda_with_flavor)

ordinary_flavor = Soda()
print(str(ordinary_flavor))
