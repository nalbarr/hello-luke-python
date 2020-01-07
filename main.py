import datetime
import random
from some_module import Item, BaseItem

def iterateScalars1DWithIndexes():
    ### 1D as array, list or linear algebra vector of scalars
    print("*** iterateScalars1DWithIndexes")

    I_MAX = 5
    for i  in range (0, I_MAX):
        print("id: {}".format(i))

def iterateScalars1DWithCollections():
    ### 1D as array, list or linear algebra vector of scalars
    print("")
    print("*** iterateScalars1DWithCollections")

    some_ints = [1, 2, 3, 4, 5]
    for i in some_ints:
        print("id: {}".format(i))

def simpleOOP():
    print("")
    print("*** simpleOOP")

    items = []

    items.append(Item('one', 1))
    items.append(BaseItem('two', 2))
    items.append(Item('three', 2))

    for i, obj in enumerate(items):
        try:
            print("i: {}; type(item): {}; item.name: {}, item.value: {}".format(i, type(obj), obj.name, obj.value))
            # NOTE: calling base class will throw NotImplementedError exception
            obj.do_something()
        except NotImplementedError:
            print("Need to override base class and implement do_something()")

def iterateObjects1DWithIndexes():
    ### 1D as array, list or linear algebra vector of <Object>
    print("")
    print("*** iterateObjects1DWithIndexes")

    some_items = []
    some_items.append(Item('one', 1))
    some_items.append(Item('two', 2))
    some_items.append(Item('three', 3))
    some_items.append(Item('four', 4))
    some_items.append(Item('five', 5))

    for i, item in enumerate(some_items):
        print("i: {}; item.name: {}, item.value: {}".format(i, item.name, item.value))

def iterateInterfaces1DWithCollections():
    # 1D as collection of interfaces
    print("")
    print("*** iterateInterfaces1DWithCollections")

    # NOTE: NAA.  Python is dynamically type thus does not support static types or Java/C# interfaces
    # NOTE: NAA.  However, can design and abstract base class with explicit method that is forced to be overriden
    # NOTE: NAA.  See implementation of BaseItem, Item
    pass

def iterateInterface1DWithSpecificTypeCasts():
    # 1D as collection of interfaces with type casting
    print("")
    print("*** iterateInterface1DWithSpecificTypeCasts")

    # NOTE: NAA.  Python is dynamically type thus does not support static types or Java/C# interfaces
    # NOTE: NAA. No need to support generics
    pass
		
def collectionsComplexity():
    ### 1D as different collection types for different operations (e.g., get)
    print("")
    print("*** collectionsComplexity")

    # CONCEPTS:
    #- List
    # - NOTE: populating each collection with 10 million integers and attempting to get an integer stored at a random index. 
    # - Why does calling get(<index>) result in different duration times to complete (performance)?
    # - Hpw would this influence your design of a program?

    # MAX_SIZE = 10000000
    MAX_SIZE = 1000000
    ints = []
    for i in range(1, MAX_SIZE):
        ints.append(random.randint(1, 100))
    
    ints2 = []
    for i in range(1, MAX_SIZE):
        ints2.append(random.randint(1, 100))
		
    start = 0.
    stop = 0.
    duration = 0.

    # random index for entire set
    index = random.randint(0, MAX_SIZE - 1)
    print("random index: {}".format(index))

    start = datetime.datetime.now()
    some_int = ints[index]
    stop = datetime.datetime.now()
    duration = stop - start
    print("ints[{}]: {} took {} milliseconds".format(index, some_int, duration))
		
 
    # random index for entire set
    index2 = random.randint(0, MAX_SIZE - 1)
    print("random index 2: {}".format(index2))

    start = datetime.datetime.now()
    some_int2 = ints[index2]
    stop = datetime.datetime.now()
    duration = stop - start
    print("ints[{}]: {} took {} milliseconds".format(index, some_int2, duration))


def main():
    iterateScalars1DWithIndexes()
    iterateScalars1DWithCollections()
    simpleOOP()
    iterateObjects1DWithIndexes()
    # iterateInterfaces1DWithCollections()
    # iterateInterface1DWithSpecificTypeCasts()
    collectionsComplexity()


if __name__ == '__main__':
    main()