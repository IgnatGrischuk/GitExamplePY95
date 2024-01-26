class BeeElephant:
    def __init__(self, part_of_bee, part_of_elephant):
        self.part_of_bee = max(0, part_of_bee)
        self.part_of_elephant = max(0, part_of_elephant)

    def fly(self):
        return self.part_of_bee >= self.part_of_elephant

    def trumpet(self):
        return 'tu-tu-doo-doo' if self.part_of_elephant >=\
                                  self.part_of_bee else 'wzzzz'

    def eat(self, meal, value):
        if meal == "nectar":
            self.part_of_elephant = min(100, max(0, self.part_of_elephant
                                                 - value))
            self.part_of_bee = min(100, max(0, self.part_of_bee + value))
        elif meal == "grass":
            self.part_of_elephant = min(100, max(0, self.part_of_elephant
                                                 + value))
            self.part_of_bee = min(100, max(0, self.part_of_bee - value))


bee_elephant_object = BeeElephant(30, 40)
print(bee_elephant_object.part_of_bee, bee_elephant_object.part_of_elephant)

bee_elephant_object.eat("nectar", 50)
print(bee_elephant_object.part_of_bee, bee_elephant_object.part_of_elephant)
