#!/usr/iin/python3
from models.base_model import BaseModel
from models import storage
from models.user import User
import cmd


class HBNBCommand(cmd.Cmd):
    """instantiates the command interpreter"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """creates a new instance of a given class"""
        if not args:
            print("** class name missing **")
            return
        try:
            class_name, *args = args.split()
            if class_name == "User":
                instance = user()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            pass

    def do_show(self, args):
        """shows the str rep of an instance based on name and id"""
        if not args:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = args.split()
            if class_name == "User":
                key = "{}.{}".format(class_name, instance_id)
                instance = storage.all().get(key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except ValueError:
            print("** instance id missing **")

    def do_update(self, args):
        """updates an instance based on class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = storage.all()
        key = class_name + "." + instance_id
        if key not in all_instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        att_val = args[3]
        instance = all_instances[key]
        if hasattr(instance, attribute_name):
            if attribute_name in ["id", "created_at", "updated_at"]:
                print("** cannot update attribute '{}' **"\
                      .format(attribute_name))
                return
            attribute_type = type(getattr(instance, attribute_name))
            try:
                cast_val = attribute_type(att_val)
            except ValueError:
                print("** invalid value type for attribute '{}' **"\
                      .format(attribute_name))
                return

            setattr(instance, attribute_name, cast_val)
            instance.save()
        else:
            print("** attribute '{}' not found **".format(attribute_name))

    def do_all(self, args):
        """prints string representation of all instances"""
        try:
            class_name = args.strip()
            if class_name == "User":
                instances = [str(instance) for instance in storage.all()\
                             .values() if isinstance(instance, User)]
                print(instances)
            elif not class_name:
                instances = [str(instance) for instance in storage.all()\
                             .values()]
                print(instances)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            pass
        if not instances:
            print("** no instances found **")
        else:
            print(instances)

    def do_destroy(self, args):
        """deletes an instance based on class name and id"""
        if not args:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = args.split()
            if class_name == "User":
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except ValueError:
            print("** instance id missing **")

    def do_quit(self, args):
        """exits the console"""
        return True

    def do_EOF(self, args):
        """signals end of file"""
        print('')
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
