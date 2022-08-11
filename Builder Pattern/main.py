from user import User
from datetime import datetime


def main() -> None:
    u = User()

    u.set_name("Sarath")
    u.set_date_of_birth(datetime(2004, 7, 23))

    print("User detials: ", u)


if __name__ == "__main__":
    main()
