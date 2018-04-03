from axis import Axis
from matrices import Matrices

def inverse_kinematics(x,y,z,alpha,beta,gamma,**frame_file):
    angles = []
    displ = [x,y,z]
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
  
    T = Axis.invert_zyz(alpha,beta,gamma):

    for i in range(len(frames) - 1,-1,-1):
        #Remove displacement
        disp = Matrices.multiply(frames[i].displacement,frames[i].parent_relation_m)
        
        

