# create an outer class
class Geeksforgeeks:

    def __init__(self):
        # create an inner class object
        self.inner = self.Inner()

    def show(self):
        print('This is an outer class')

    # create a 1st inner class

    class Inner:
        def __init__(self):
            # create an inner class of inner class object
            self.innerclassofinner = self.Innerclassofinner()

        def show(self):
            print('This is the inner class')

        # create an inner class of inner

        class Innerclassofinner:
            def show(self):
                print('This is an inner class of inner class')


# create an outer class object
# i.e.Geeksforgeeks class object
outer = Geeksforgeeks()
outer.show()
print()

# create an inner class object
gfg1 = outer.inner
gfg1.show()
print()

# create an inner class of inner class object
gfg2 = outer.inner.innerclassofinner
gfg2.show()