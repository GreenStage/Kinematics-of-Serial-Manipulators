#constan values
pi = 3.14159265358979323846264338

class Tree:
    def __init__(self,data):
        self._data = data
        self._children = {}

    def add_child(self,childname,childdata):
        self._children[childname] = Tree(childdata)
        return self._children[childname]

 
    def remove_child(self,childname):
        del self._children[childname]

    def print_deep(self,it = 0):

        for key,child in self._children.items():
            for i in range(it):
                print('\t',end='')

            val = child.value / pi
            if val > 1.0:
                val = val - 2
            val = round(val,4)
            print(key + ": value = " + str(val) +"π")
            child.print_deep(it+1)

    @property
    def childs(self):
        return self._children

    @property
    def child(self,childname):
        return self._children[childname]

    @property
    def value(self):
        return self._data