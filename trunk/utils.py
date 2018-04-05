from math import sqrt

class Utils:

    @staticmethod                
    def multiply_matrix(m1,m2):
        retval = []

        for i in range(len(m1)):
            temp_row = []
            for j in range(len(m2[0])):
                temp = 0
                for k in range(len(m2)):
                    temp += m1[i][k] * m2[k][j]
                temp_row.append(temp)
            retval.append(temp_row)
            
        return retval

    @staticmethod
    def intersect_circunference(x1,y1,r1,x2,y2,r2):
        centerdx = x1 - x2
        centerdy = y1 - y2
        R = sqrt(centerdx * centerdx + centerdy * centerdy)
        if (not abs(r1 - r2) <= R ) or not  (R <= r1 + r2):
            raise Exception('Invalid displacement vector')

        R2 = R*R
        R4 = R2*R2
        a = (r1*r1 - r2*r2) / (2 * R2)
        r2r2 = (r1*r1 - r2*r2)
        c = sqrt(2 * (r1*r1 + r2*r2) / R2 - (r2r2 * r2r2) / R4 - 1)

        fx = (x1+x2) / 2 + a * (x2 - x1)
        gx = c * (y2 - y1) / 2
        ix1 = fx + gx
        ix2 = fx - gx

        fy = (y1+y2) / 2 + a * (y2 - y1)
        gy = c * (x1 - x2) / 2
        iy1 = fy + gy
        iy2 = fy - gy

        return [[ix1, iy1], [ix2, iy2]]

    @staticmethod
    def magnitude(p):
        summ = 0
        for i in range(len(p)):
            summ += p[i]**2
        return sqrt(summ)


#This piece of code was translated from C
#and adapted to this project
#Original code here:
#https://stackoverflow.com/questions/1148309/inverting-a-4x4-matrix

    @staticmethod
    def inv_4x4_matrix(q):
        if len(q) != 4:
            raise Exception('Matrix is not 4x4')
        for i in q:
            if len(i) != 4:
                raise Exception('Matrix is not 4x4')
        
        m = []
        for i in range(0,4):
            for j in range(0,4):
                m.append(q[i][j])

        inv = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]

        inv[0]=m[5]*m[10]*m[15]-m[5]*m[11]*m[14]-m[9]*m[6]*m[15]+m[9]*m[7]*m[14]+m[13]*m[6]*m[11]-m[13]*m[7]*m[10]

        inv[4]=-m[4]*m[10]*m[15]+m[4]*m[11]*m[14]+m[8]*m[6]*m[15]-m[8]*m[7]*m[14]-m[12]*m[6]*m[11]+m[12]*m[7]*m[10]

        inv[8]=m[4]*m[9]*m[15]-m[4]*m[11]*m[13]-m[8]*m[5]*m[15]+m[8]*m[7]*m[13]+m[12]*m[5]*m[11]-m[12]*m[7]*m[9]

        inv[12]=-m[4]*m[9]*m[14]+m[4]*m[10]*m[13]+m[8]*m[5]*m[14]-m[8]*m[6]*m[13]-m[12]*m[5]*m[10]+m[12]*m[6]*m[9]

        inv[1]=-m[1]*m[10]*m[15]+m[1]*m[11]*m[14]+m[9]*m[2]*m[15]-m[9]*m[3]*m[14]-m[13]*m[2]*m[11]+m[13]*m[3]*m[10]

        inv[5]=m[0]*m[10]*m[15]-m[0]*m[11]*m[14]-m[8]*m[2]*m[15]+m[8]*m[3]*m[14]+m[12]*m[2]*m[11]-m[12]*m[3]*m[10]

        inv[9]=-m[0]*m[9]*m[15]+m[0]*m[11]*m[13]+m[8]*m[1]*m[15]-m[8]*m[3]*m[13]-m[12]*m[1]*m[11]+m[12]*m[3]*m[9]

        inv[13]=m[0]*m[9]*m[14]-m[0]*m[10]*m[13]-m[8]*m[1]*m[14]+m[8]*m[2]*m[13]+m[12]*m[1]*m[10]-m[12]*m[2]*m[9]

        inv[2]=m[1]*m[6]*m[15]-m[1]*m[7]*m[14]-m[5]*m[2]*m[15]+m[5]*m[3]*m[14]+m[13]*m[2]*m[7]-m[13]*m[3]*m[6]

        inv[6]=-m[0]*m[6]*m[15]+m[0]*m[7]*m[14]+m[4]*m[2]*m[15]-m[4]*m[3]*m[14]-m[12]*m[2]*m[7]+m[12]*m[3]*m[6]

        inv[10]=m[0]*m[5]*m[15]-m[0]*m[7]*m[13]-m[4]*m[1]*m[15]+m[4]*m[3]*m[13]+m[12]*m[1]*m[7]-m[12]*m[3]*m[5]

        inv[14]=-m[0]*m[5]*m[14]+m[0]*m[6]*m[13]+m[4]*m[1]*m[14]-m[4]*m[2]*m[13]-m[12]*m[1]*m[6]+m[12]*m[2]*m[5]

        inv[3]=-m[1]*m[6]*m[11]+m[1]*m[7]*m[10]+m[5]*m[2]*m[11]-m[5]*m[3]*m[10]-m[9]*m[2]*m[7]+m[9]*m[3]*m[6]

        inv[7]=m[0]*m[6]*m[11]-m[0]*m[7]*m[10]-m[4]*m[2]*m[11]+m[4]*m[3]*m[10]+m[8]*m[2]*m[7]-m[8]*m[3]*m[6]

        inv[11]=-m[0]*m[5]*m[11]+m[0]*m[7]*m[9]+m[4]*m[1]*m[11]-m[4]*m[3]*m[9]-m[8]*m[1]*m[7]+m[8]*m[3]*m[5]

        inv[15]=m[0]*m[5]*m[10]-m[0]*m[6]*m[9]-m[4]*m[1]*m[10]+m[4]*m[2]*m[9]+m[8]*m[1]*m[6]-m[8]*m[2]*m[5]

        det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12]

        if det == 0:
            raise Exception('Non-invertible matrix')

        det = 1 / det

        retval = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        for i in range(0,4):
            for j in range(0,4):
                retval[i][j] = inv[i*4 + j] * det

        return retval
