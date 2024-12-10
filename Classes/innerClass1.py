# create a Geeksforgeeks class
class Geeksforgeeks:

    # constructor method

    def __init__(self):

        # object attributes
        self.course = "Campus preparation"
        self.duration = "2 months"

        # define a show method
        # for printing the content

    def show(self):

        print("Course:", self.course)
        print("Duration:", self.duration)


# create Geeksforgeeks
# class object
outer = Geeksforgeeks()

# method calling
outer.show()

########################

class Color:

    # constructor method

    def __init__(self):

        # object attributes

        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print('Name:', self.name)


    # create Inner Lightgreen class

    class Lightgreen:

        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)

# create Color class object
outer = Color()


# method calling
outer.show()

# create a Lightgreen
# inner class object

g = outer.lg

# inner class method calling

g.display()