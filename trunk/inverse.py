from axis import Axis
import json
from frame import Frame
from utils import Utils
from math import atan2,cos,sin,acos,sqrt,acos, asin
from tree import Tree
import random
#constan values
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
    T[0].append(x)
    T[1].append(y)
    T[2].append(z)
    T.append([0,0,0,1])

    result = Tree(0)
#compute teta1
    result.add_child('teta1_a',atan2( -pos[0],pos[1] ))
    result.add_child('teta1_b',atan2( pos[0],-pos[1] ))

#compute teta2,teta3
#rotate plane around z to zy for each teta1

    for branch, teta1 in result.childs.items():
        ang = teta1.value
        p = [pos]

        #rotate plane to zy
        np = Utils.multiply_matrix(p,[[cos(ang),-sin(ang),0],
                                      [sin(ang), cos(ang), 0],
                                      [0,        0,        1]])
        
        new_p = [np[0][0],np[0][1],np[0][2] - 99]

        #we got a plane
        p_mag = Utils.magnitude(new_p)
        #intersect circunference with radius c centered in new_p
        #with one centered in [0,99] (due to the displacement from frame 1 to frame 2 )
        #and with radius of 120

        c = 155
        p2 = Utils.intersect_circunference(new_p[1],new_p[2],c,0,0,120)

        teta2_a = atan2(-p2[0][0],p2[0][1])
        teta2_b = atan2(-p2[1][0],p2[1][1])

        teta1.add_child('teta2_a',teta2_a)
        teta1.add_child('teta2_b',teta2_b)

        i = 0
        for branch2, teta2 in  teta1.childs.items():    
            p2_mag = Utils.magnitude(p2[i])

            cosalpha = -(p_mag**2 - c**2 - p2_mag**2) / (2*c*p2_mag)

            alpha = acos(cosalpha)
  
            if i == 0:
                teta3 = alpha -  pi/2
            else:
                teta3 = alpha + pi/2 -2 *pi

            
            t3_branch = teta2.add_child('teta3',teta3)
            i+=1

            frames[0].rotate_joint_z(teta1.value)
            frames[1].rotate_joint_z(teta2.value)
            frames[2].rotate_joint_z(teta3)

            T03 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

            for frame in frames[0:3]:
                T03 = Utils.multiply_matrix(T03,frame.position_m)

            T30 = Utils.inv_4x4_matrix(T03)


            T36 = Utils.multiply_matrix(T30,T)

            costeta5 = T36[1][2]

            #two possible teta5 values
            teta5 = [0,0]

            teta5[0] = acos(costeta5)
            teta5[1]= -teta5[0]

            enum = ['a','b']
            j = 0
            for t5 in teta5:
                if round(sin(t5),4) == 0:
                    t3_branch.add_child('error','Configuration singularity sin(teta5) = 0')
                    continue
                else:
                    sinTeta6 = round(- T36[1][1] / sin(t5),4)
                    cosTeta6 = round(T36[1][0] / sin(t5),4)
                    cosTeta4 = round(- T36[0][2] / sin(t5),4)
                    sinTeta4 = round(- T36[2][2] / sin(t5),4)
                    
                    teta4 = acos(cosTeta4)
                    if sinTeta4 < 0:
                        teta4 = - teta4

                    teta6 = acos(cosTeta6)
                    if sinTeta6 < 0 :
                        teta6 = - teta6

                    t4_branch = t3_branch.add_child('teta4' + enum[j],teta4)
                    t5_branch = t4_branch.add_child('teta5',t5)
                    t5_branch.add_child('teta6',teta6)
                    j+=1

    return result

#res = inverse_kinematics(145,10,10,0,0,0)
ret = inverse_kinematics(-181.6216,104.8593,243.04,2.3907,1.6308,2.5366)
ret.print_deep()