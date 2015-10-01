class Histogram(dict):
    """
    A Histogram is a dictionary used to keep track of the number of observed events
    """

    def __init__(self, arg):
        """
        Create a new histogram with bins labeled by strings in a list or tuple.
        """
        if isinstance(arg, (list, tuple)):
            dict.__init__( self, { x:0 for x in arg} )
        else:
            raise Exception("histogram labels must be defined by a sequence of strings")


    def count(self, x):
        """
        Add 1 to the count for bin x.
        """
        if x in self:
            # Can't use self[x] += 1 because __setitem__ is disabled
            n = dict.__getitem__(self, x)
            dict.__setitem__(self, x, n+1)
        else:
            raise Exception("no bin named " + str(x))


    def __setitem__(self, index, value):
        raise Exception("can't assign to histogram; use count to update a bin")


    def __delitem__(self, index):
        raise Exception("can't delete a bin from a histogram")
