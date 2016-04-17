__author__ = 'nimbus'
from datetime import datetime
import rules
import yaml
import requests

class CLiDL(object):

    def __init__(self):
        self.session_date   = datetime.now()
        self.database       = {}

        with open("config.yml", "r") as db:
            try:
                # print(yaml.load(db))
                self.database = yaml.load(db)
                print(self.database['db_ip'])
            except yaml.YAMLError as exc:
                print(exc)

    def connect(self):
        ip = self.database["db_ip"]
        port = self.database["db_port"]
        http = True

        r = requests.get(url="{}{}:{}".format("http://" if http else "https://", ip, port))
        print(r.url)
        print(r.text)
        print(r.status_code)

    # def test_put(self):
    #
    #     url = "{}{}".format(self.database["db_full"], "/customer/external")
    #     data = {"name": "Jane Doe"}
    #
    #     r = requests.put(url=url, data=data)
    #     print(r.text)
    #     print("*"*50)
    #     print(r.status_code)

    # def httpbin(self):
    #     # ip = self.database["db_ip"]
    #     # self.database["db_port"]
    #     end_point = '/twitter/tweet/1'
    #
    #     url = "http://{}:{}{}".format(self.database["db_ip"], self.database["db_port"], end_point)
    #     print(url)
    #
    #     r = requests.get(url=url)
    #     print(r.text)
    #     print(r.status_code)


class functions(object):

    @classmethod
    def add(self, *args, **kwargs):
        """
        Create
        :return:
        """
        print("This adds something to the database")

        # This is for future, can be passed multiple lists
        if len(args) > 1: raise print("There are to many lists")

        # for now the list always will be 1

        elif len(args) == 1: print(args[0])

        # if user didn't give any input af key_command
        else: print(">>> You didnt give any arguments!!")

    @rules.find
    @classmethod
    def find(self, *args, **kwargs):
        """
        Read
        :return:
        """
        print("Find records in the database")
        # This is for future, can be passed multiple lists
        if len(args) > 1: raise print("There are to many lists")

        # for now the list always will be 1
        elif len(args) == 1: print(args[0])

        # if user didn't give any input af key_command
        else: print(">>> You didnt give any arguments!!")

    @classmethod
    def edit(self, *args, **kwargs):
        """
        Update
        :return:
        """
        print("Edit record(s) from the database")
        print(args)

    @classmethod
    def remove(self, *args, **kwargs):
        """
        Delete
        :return:
        """
        print("Remove record(s) from the database")
        print(args)

    @classmethod
    def connect(self, *args, **kwargs):
        """
        Connect
        :return:
        """
        print("Connect to a given database")
        print(args)


def parser(func):
    """
    CliDl Decorative Parser Function
    :param func:
    :return:
    """
    # Main Key Commands
    keys = ["add", "find", "edit", "remove", "connect"]

    def inner(*args, **kwargs):
        """
        Decorative Inner Function
        """

        # Check all arguments in given list
        for arg in args[0]:

            # Check if arguments in list is equal to a key_command
            if arg in keys:

                # Check if given key_command is as first argument
                # otherwise raise error
                # If key_command is first argument, call function with a list a parameter
                # List is the rest of the given argument(s) minus key_command
                if args[0].index(arg) != 0: print("Please define first argument as 'command' or try `help`")
                else: getattr(functions, arg)(args[0][1:])
                break

            else:
                # print("##### {}".format(arg))
                continue

        return func(args, kwargs)

    return inner



@parser
def main(*args, **kwargs):
    try:
        print("Check Function")
    except Exception as e:
        print(e)


if __name__ == '__main__':

    c = CLiDL()

    # ent = input("press enter to do a test PUT request")
    # print(c.httpbin())
    # c.connect()

    print('''
    + ----------------------------------------------------- +
    |   CLiDL - Command Line Interface Database Language    |
    |   Version:    1.2                                     |
    |   Author:     Gokhan Kacan                            |
    + ----------------------------------------------------- +
    ''')

    while True: main(input(" > ").split())

    # command = input(" > ").split()
    # main(command)
