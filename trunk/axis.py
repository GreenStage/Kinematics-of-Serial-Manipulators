from math import cos,sin,atan2,sqrt
class Axis:
    #Euler ZYZ
    @staticmethod    
    def angles_zyz(p):
        beta = atan2(sqrt( p[0][2]**2 + p[1][2]**2 ),p[2][2])
        sinBeta = sin(beta)
        cosBeta = cos(beta)

        if round(sinBeta,4) == 0 and round(cosBeta,4) > 0:
            alpha = atan2(p[1][0],p[0][0])
            gamma = 0
        elif round(sinBeta,4) == 0 and round(cosBeta,4) < 0:
            gamma = 0
            alpha =  atan2(-p[1][0],-p[0][0])
        elif round(sinBeta,4) > 0:
            alpha =  atan2(p[1][2],p[0][2])
            gamma =  atan2(p[2][1],-p[2][0])
        else:
            alpha =  atan2(-p[1][2],-p[0][2])
            gamma =  atan2(-p[2][1],p[2][0])
        return {
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma
        }

    @staticmethod
    def invert_zyz(alpha,beta,gamma):
        retval = [[0,0,0],[0,0,0],[0,0,0]]
        retval[0][0] = cos(gamma) * cos(alpha) * cos(alpha) - sin(alpha) * sin(gamma)
        retval[0][1] = - sin(gamma) * cos(alpha) * cos(alpha) - sin(alpha) * cos(gamma)
        retval[0][2] = cos(gamma) * sin(beta)
        retval[1][0] = sin(alpha) * cos(beta) * cos(gamma) + cos(alpha) * sin(gamma)
        retval[1][1] = -sin(alpha) * cos(beta) * sin(gamma) + cos(alpha) * cos(gamma)
        retval[1][2] = sin(alpha) * sin(beta)
        retval[2][0] = -sin(beta) * cos(gamma)
        retval[2][1] = sin(beta) * sin(gamma)
        retval[2][2] = cos(beta)
        return retval

    #Fixed XYZ
    @staticmethod
    def angles_xyz(p):
        beta = atan2(-p[2][0],sqrt( p[0][0]**2 + p[1][0]**2 ))
        sinBeta = sin(beta)
        cosBeta = cos(beta)

        if round(cosBeta,4) == 0 and round(sinBeta,4) > 0:
            #beta == pi/2
            alpha = 0
            gamma = atan2(p[0][1],p[1][1])
        elif round(cosBeta,4) == 0 and round(sinBeta,4) < 0:
            print("oi")
            alpha = 0
            gamma =  -atan2(p[0][1],p[1][1])
        else:
            alpha =  atan2(p[1][0]/cosBeta,p[0][0]/cosBeta)
            gamma =  atan2(p[2][1]/cosBeta,p[2][2]/cosBeta)
        return {
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma
        }