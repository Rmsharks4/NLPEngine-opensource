class MathematicsUtils:

    def __init__(self):
        pass

    @classmethod
    def length(cls, args):
        return len(args)

    @classmethod
    def count(cls, args):
        return args[0].count(args[1])

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
