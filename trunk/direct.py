#
from math import cos,sin,atan2,sqrt
from frame import Frame
from matrices import Matrices
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

        if data['dof']:
            dof = data['dof']

        frames_prototype = data['frames']
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
    

    for i in range(0,6):
        frames[i].rotate_joint_z(angles[i])

    for i in range(0,6):
        final_position_m = Matrices.multiply(final_position_m,frames[i].position_m)

    p = final_position_m

    beta = atan2(sqrt( p[0][2]**2 + p[1][2]**2 ),p[2][2])
    sinBeta = sin(beta)
    cosBeta = cos(beta)

    if sinBeta == 0 and cosBeta == 1:
        alpha = atan2(p[1][0],p[0][0])
        gamma = 0
    elif sinBeta == 0 and cosBeta == -1:
        gamma = 0   
        alpha =  atan2(-p[1][0],-p[0][0])
    elif sinBeta > 0:
        alpha =  atan2(p[1][0],p[0][0])
        gamma =  atan2(p[2][1],-p[2][0])
    else:
        alpha =  atan2(-p[1][2],-p[0][2])
        gamma =  atan2(-p[2][1],p[2][0])      

    retval = {}
    retval['x'] = p[0][3]
    retval['y'] = p[1][3]
    retval['z'] = p[2][3]
    retval['alpha'] = alpha
    retval['beta'] = beta
    retval['gamma'] = gamma
    return retval

#Testing


a = direct_kinetics(0,0,0,0,0,0,0)
for i in a:
    print(i,a[i])
