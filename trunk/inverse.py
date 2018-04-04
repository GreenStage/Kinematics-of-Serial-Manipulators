from axis import Axis
import json
from frame import Frame
from matrices import Matrices
from math import atan2,cos,sin,acos,sqrt

pi = 3.14159265358979323846264338

def inverse_kinematics(x,y,z,alpha,beta,gamma,**frame_file):
    angles = {}
    frames = []
    pos = [x,y,z]
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
  
    T = Axis.invert_zyz(alpha,beta,gamma)

#compute teta1
    angles['teta1'] = []
    angles['teta1'].append( {
        'value' : atan2( pos[1],pos[0] ),
        'teta2' : [],
        'teta3' : []
    } )
    
    angles['teta1'].append( {
        'value' : atan2( -pos[1],-pos[0] ),
        'teta2' : [],
        'teta3' : []
    } )

#compute teta2,teta3
#rotate plane around z to zy for each teta1
    for a in angles['teta1']:
        ang = pi/2 - a['value']
        p = [pos]
        np = Matrices.multiply(p,[[cos(ang),-sin(ang),0],
                                      [sin(ang), cos(ang), 0],
                                      [0,        0,        1]])
        new_p = np[0]
        #subtract the displacement created by frame 4 - 155
        d1 = sum(frames[2].displacement)
        d2 = sum(frames[4].displacement) - sum(frames[3].displacement)
        d0 = sqrt(new_p[1]**2 + new_p[2]**2)

        a0 = atan2(new_p[1],new_p[2])
        a1 = acos( (d1**2 + d0**2 - d2**2) / (2*d1*d0) )
        a2 = acos( (d1**2 + d2**2 - d0**2) / (2*d1*d2) )

        a['teta2'].append({'value': a0 + a2})
        a['teta2'].append({'value': a0 - a2})
        a['teta3'].append({'value': a1})
        a['teta3'].append({'value': 2*pi - a1})    

    print(angles)

inverse_kinematics(170,0,150,1.3,1.2,1.4)