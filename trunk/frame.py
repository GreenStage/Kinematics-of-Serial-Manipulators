from math import cos,sin
from utils import Utils

class Frame:

    def __init__(self,displacement,parent_relation_m = [[1,0,0],[0,1,0],[0,0,1]]):

        if (not isinstance(displacement,list)) or (not len(displacement) == 3):
            raise Exception('Invalid displacement vector')

        self._displacement = displacement
        self._angle = 0
        self._position_m = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

        self._position_m[0][3] = self._displacement[0]
        self._position_m[1][3] = self._displacement[1]
        self._position_m[2][3] = self._displacement[2]

        self._parent_relation_m = parent_relation_m

    def rotate_joint_z(self,ang):
        self._angle = self._angle + ang

        rotate_z_matrix = [[cos(self._angle ),-sin(self._angle ),0],
            [sin(self._angle ),cos(self._angle ),0],
            [0,0,1]]

        self._position_m = Utils.multiply_matrix(self._parent_relation_m,rotate_z_matrix)
        self._position_m[0].append(self._displacement[0])
        self._position_m[1].append(self._displacement[1])
        self._position_m[2].append(self._displacement[2])
        self._position_m.append([0,0,0,1])

    @property
    def parent_relation_m(self):
        return self._parent_relation_m

    @property
    def displacement(self):
        return self._displacement

    @property
    def position_m(self):
        return self._position_m