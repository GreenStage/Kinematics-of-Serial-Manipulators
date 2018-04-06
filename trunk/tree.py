#constant values
pi = 3.14159265358979323846264338
from copy import deepcopy
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

            if key == 'error':
                print(key + ": "+ child.value)
                continue
            val = child.value / pi
            if val > 1.0:
                val = val - 2
            val = round(val,4)
            print("└ " + key + ": value = " + str(val) +"π")
            child.print_deep(it+1)

    def to_array(self,retval = [[],[],[],[],[],[],[],[]],a = 0):
        i = 0
        retval[a].append(self._data)
        for key,child in self._children.items():
  
            if i != 0:
                print("oi")
                a+= 1
                retval[a] = deepcopy(retval[a-1])
                retval = child.to_array(retval,a)
            else:
                retval = child.to_array(retval,a)

            i+=1

        return retval
            
    
    @property
    def childs(self):
        return self._children

    @property
    def child(self,childname):
        return self._children[childname]

    @property
    def value(self):
        return self._data

    