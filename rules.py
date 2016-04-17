__author__ = 'nimbus'

def find(func):

    def inner(*args, **kwargs):

        print("Printing Rules for the Find function")
        print("*"*50)

        # Rule 1: check if argument passed multiple lists
        if len(args) > 1: raise print("There are to many lists")

        # for now the list always will be 1
        elif len(args) == 1:


            # Rule 2: has to have  arguments
            if args[0] != 0:

                # Rule 3: arguments are being check for key:value
                # filter_key_value(args[0])
                # print(list(map(filter_key_value, args[0])))
                print(list(filter(filter_key_value, args[0])))

            '''
            while args[0] != 0:

                ######
                for arguments in args[0]:
                    print(arguments)
                break
            '''

        # Rule 4: no argument end with a , (comma)

        return args

    return inner



def filter_key_value(*args, **kwargs):
    import re

    for i in args:
        # check for only the first : after key and before value
        if re.search(":", i):
            return i
        else: print("No Key:Value Found :: ERROR")