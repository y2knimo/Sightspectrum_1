class Method:
    def __init__(self, argument):
        self.attribute = argument



class Method_2:
    def __init__(self, argument):
        self.attribute = argument


instance_1 = Method(" Attribute")
print(instance_1.attribute)
instance_2 = Method_2(" 27")
print(instance_2.attribute)

print(instance_2.attribute + instance_1.attribute)