import sys
import database
import user_interface


def main():
    args = sys.argv

    if len(args) != 2:
        print("The script should be called with file name argument!")
        sys.exit(-1)

    ui = user_interface.Uinterface()
    data_base = database.Storage(str(args[1]))
    fill_recipes(data_base, ui)


def fill_recipes(data_base, ui):
    while True:
        recipe_name = ui.get_recipe_name()
        if len(recipe_name) > 0:
            recipe_desc = ui.get_recipe_description()
            recipe_id = data_base.save_recipe(recipe_name, recipe_desc)
            periods = data_base.get_data_from_table('meals')
            selected_periods = ui.get_when_can_served(periods)
            data_base.save_serve(selected_periods, recipe_id)
            while True:
                input_quantity = input("Input quantity of ingredient <press enter to stop>:").split(" ")
                if len(input_quantity) == 3:
                    quantity = input_quantity[0]
                    measure_id = data_base.get_id_from_table('measures', input_quantity[1])
                    ingredient_id = data_base.get_id_from_table('ingredients', input_quantity[2])
                elif len(input_quantity) == 2:
                    quantity = input_quantity[0]
                    measure_id = data_base.get_id_from_table('measures', "")
                    ingredient_id = data_base.get_id_from_table('ingredients', input_quantity[1])
                else:
                    break
                if measure_id is not None:
                    if ingredient_id is not None:
                        data_base.save_quantity(quantity, recipe_id, measure_id, ingredient_id)
                    else:
                        print("The ingredient is not conclusive!")
                else:
                    print("The measure is not conclusive!")
                data_base.print_table("quantity")
        else:
            break


if __name__ == "__main__":
    main()
