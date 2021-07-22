import sys
import database
import user_interface
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("db_file_name", default=None)
    parser.add_argument("-i", "--ingredients", default=None)
    parser.add_argument("-m", "--meals", default=None)

    args = parser.parse_args()
    if args.db_file_name is None:
        print("The script should be called with file name argument!")
        sys.exit(-1)
    else:
        db_file = args.db_file_name

    ingredients = args.ingredients.split(',') if args.ingredients is not None else None
    meals = args.meals.split(',') if args.ingredients is not None else None

    print(ingredients)
    print(meals)

    ui = user_interface.Uinterface()
    data_base = database.Storage(db_file)

    if ingredients is None and meals is None:
        fill_recipes(data_base, ui)
    else:
        print("DO THERE")
        get_selected(data_base, ui, ingredients, meals)


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
                    measure_id = 8
                    # measure_id = data_base.get_id_from_table('measures', "")
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


def get_selected(data_base, ui, ingredients, meals):
    print(meals)
    meals_id = data_base.get_list_id_from_table_meal(meals)
    print(meals_id)
    print(ingredients)
    ingr_id = data_base.get_list_id_from_table_ing(ingredients)
    print(ingr_id)
    recipe_in_serve = data_base.get_recipe_in_serve(meals_id, ingr_id)
    if len(recipe_in_serve) > 0:
        recipe_name = data_base.get_name_from_recipe(recipe_in_serve)
        print(", ".join(recipe_name))
    else:
        print("There are no such recipes in the database.")

if __name__ == "__main__":
    main()
