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
