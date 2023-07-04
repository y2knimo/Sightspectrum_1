class ContextManager():
    def __init__(self):
        print('HII')

    def __enter__(self):
        print('This is ')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('My')


with ContextManager() as manager:
    print('Program')
