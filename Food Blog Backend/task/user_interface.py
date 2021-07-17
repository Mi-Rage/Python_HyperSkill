class Uinterface:

    def get_recipe_name(self):
        return str(input("Recipe name: "))

    def get_recipe_description(self):
        return str(input("Recipe description: "))

    def get_when_can_served(self, periods):
        print(self.make_str_from_db(periods))
        return input("When the dish can be served: ").split(" ")

    def make_str_from_db(self, source):
        result = ""
        for item in source:
            result += str(item[0]) + ") " + item[1] + " "
        return result
