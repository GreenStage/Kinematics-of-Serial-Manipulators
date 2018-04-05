
from frame import Frame
from axis import Axis
from utils import Utils
import warnings
import json


pi = 3.14159265358979323846264338


def direct_kinetics (*angles,**frame_file):
    frames = []
    dof = 6
    final_position_m =  [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    filename =  frame_file.pop('input', 'serial_manipulator_6.json')

    with open(filename) as input:
        data = json.load(input)

        dof = data.pop('dof',6) #6 dof by default

        frames_prototype = data['frames']

        if not frames_prototype:
            raise Exception('No frames in file')

        convention = data.pop('convention','xyz')

        for prototype in frames_prototype:
            frames.append(Frame(prototype['displacement'],prototype['previous_relation']))
    
    if len(angles) > dof:
        warn = "The Number of angles passed is less than the DoF in the imported file,"+repr(len(angles) - dof)+" angles will be ignored."
        warnings.warn(warn)
        angles = angles[:dof]
    if dof < len(frames):
        warn = "Degrees of freedom are less than the DoF in the imported file,"+repr(len(angles) - dof)+" angles will be ignored."
        warnings.warn(warn)
        frames = frames[:dof]
    
    if len(angles) < dof:
        raise Exception('insuficient angles')

    for i in range(0,6):
        frames[i].rotate_joint_z(angles[i])

    for i in range(0,6):
        final_position_m = Utils.multiply_matrix(final_position_m,frames[i].position_m)

    p = final_position_m

    if(convention == "zyz"):
        print("Getting euler angles for moving axis rotations Z-Y-Z")
        retval = Axis.angles_zyz(p)
    elif(convention == "xyz"):
        print("Getting fixed angles for fixed rotations X-Y-Z")
        retval = Axis.angles_xyz(p)
    else:
        print("Invalid convention: " + convention + ", using zyz")
        print("Getting euler angles for moving axis rotations Z-Y-Z")
        retval = Axis.angles_zyz(p)

    retval['x'] = p[0][3]
    retval['y'] = p[1][3]
    retval['z'] = p[2][3]

    for i in retval:
        print(i,round(retval[i],4))
    return retval

#Testing
a = direct_kinetics(pi,0.0323*pi,0,0,0,0)


