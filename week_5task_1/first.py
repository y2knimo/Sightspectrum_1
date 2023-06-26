class Method(object):
    def __new__(cls):
        print("Creating an instance __new__ method")
        return super(Method, cls).__new__(cls)

    def __init__(self):
        print("Init method")


Method()