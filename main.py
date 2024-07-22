from tools import create_database
from interface import menu, select


def main():

    create_database()  # Create database

    # Loop
    while True:
        menu()  # Menu
        select()  # Input and interaction

if __name__ == "__main__":
    main()
