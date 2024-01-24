class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}," \
               f" pepperoni={self.pepperoni}, " \
               f"mushrooms={self.mushrooms}, onions={self.onions}," \
               f" bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza(size, cheese=False, pepperoni=False,
                           mushrooms=False, onions=False, bacon=False)

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return self.builder.build()


# Example of using

builder = PizzaBuilder(size="Medium")
director = PizzaDirector(builder)

pizza = director.make_pizza()
print(pizza)

builder.add_cheese().add_pepperoni().add_mushrooms().add_onions().add_bacon()
pizza_with_toppings = builder.build()
print(pizza_with_toppings)
