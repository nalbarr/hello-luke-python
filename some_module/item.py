class BaseItem(object):
    name = None
    value = None

    # name = property(set_name, get_name)
    # value = property(set_value, get_value)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


    def do_something(self):
        raise NotImplementedError("The method not implemented")

class Item(BaseItem):
    def __init__(self, name, value):
        # NOTE: Python 2 to 3?
        # super(Item, self).__init__(name, value)
        super().__init__(name, value)
    
    def do_something(self):
        print("do something.")

    def __str__(self):
        s = "name: {}, value: {}".format(self.name, self.value)