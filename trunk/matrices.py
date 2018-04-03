class Matrices:

    @staticmethod                
    def multiply(m1,m2):
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
