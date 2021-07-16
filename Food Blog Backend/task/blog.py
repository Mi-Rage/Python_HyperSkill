import sys
import database


def main():
    args = sys.argv

    if len(args) != 2:
        print("The script should be called with file name argument!")
        sys.exit(-1)

    data_base = database.Storage(str(args[1]))
    data_base.print_table()


if __name__ == "__main__":
    main()
