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
            data_base.save_recipe(recipe_name, recipe_desc)
            data_base.print_table("recipes")
        else:
            break


if __name__ == "__main__":
    main()
