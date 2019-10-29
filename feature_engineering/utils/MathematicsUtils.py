
class MathematicsUtils:

    def __init__(self):
        pass

    @classmethod
    def add(cls, args):
        return args[0] + args[1]

    @classmethod
    def subtract(cls, args):
        return args[0] - args[1]

    @classmethod
    def multiply(cls, args):
        return args[0] * args[1]

    @classmethod
    def divide(cls, args):
        return args[0] / args[1]

    @classmethod
    def length(cls, args):
        return len(args)

    @classmethod
    def set_value(cls, args):
        if args[3] == '>':
            if args[0] > args[1]:
                return args[2]
        if args[3] == '<':
            if args[0] < args[1]:
                return args[2]
