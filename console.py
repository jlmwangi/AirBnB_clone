#!/usr/bin/python3
import cmd


class MyConsole(cmd.Cmd):
    """instantiates the command interpreter"""
    intro = "Welcome to hbnb"
    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.reservations = {}

    def do_create(self, args):
        """creates a new object"""
        user, place = args.split()
        if user not in self.reservations:
            self.reservations[user] = place
            print(f"reservation added: {user} - {place}")
        else:
            print(f"{user} already has a reservation")

    def do_read(self, args):
        """shows the list of users and places reserved"""
        if self.reservations:
            for user, place in self.reservations.items():
                print(f"{user} - {place}")
        else:
            print("No reservations")

    def do_retrieve(self, args):
        """retrieves a particular user and their reservation"""
        user = args
        if user in self.reservations:
            print(f"{user} - {self.reservations[user]}")
        else:
            print(f"{user} not found")

    def do_update(self, args):
        """updates user for another reservation"""
        user, new_place = args.split()
        if user in self.reservations:
            self.reservations[user] = new_place
            print(f"reservation updated to {new_place}")
        else:
            self.do_create(args)

    def do_count(self, args):
        """counts number of users with reservations made"""
        print(len(self.reservations))

    def do_delete(self, args):
        """deletes an entry from reservations"""
        user = args
        if user in self.reservations:
            del self.reservations[user]
            print(f"{user} has been removed")
        else:
            print("user not found")

    def do_exit(self, args):
        """exits the console"""
        return True

    def do_EOF(self, args):
        """signals end of file"""
        print("Exiting the console.")
        return True


if __name__ == "__main__":
    MyConsole().cmdloop()
