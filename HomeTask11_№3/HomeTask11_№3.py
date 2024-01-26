class Pizza:
    def __init__(self):
        self.size = "Medium"
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}," \
               f" pepperoni={self.pepperoni}, " \
               f"mushrooms={self.mushrooms}, onions={self.onions}," \
               f" bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza()
        self.pizza.size = size

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
    def __init__(self, size):
        self.builder = PizzaBuilder(size)

    def add_toppings(self, *toppings):
        for topping in toppings:
            if topping == 'cheese':
                self.builder.add_cheese()
            elif topping == 'pepperoni':
                self.builder.add_pepperoni()
            elif topping == 'mushrooms':
                self.builder.add_mushrooms()
            elif topping == 'onions':
                self.builder.add_onions()
            elif topping == 'bacon':
                self.builder.add_bacon()
            else:
                print(f"Unknown topping: {topping}")

    def make_pizza(self):
        return self.builder.build()


# Example of using

director = PizzaDirector(size="Medium")

# Adding toppings directly through the director
director.add_toppings('cheese', 'pepperoni', 'mushrooms', 'onions', 'bacon')

pizza_with_toppings = director.make_pizza()
print(pizza_with_toppings)
