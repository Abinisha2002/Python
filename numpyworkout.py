import numpy as np
i=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in i:
    for y in x:
        for j in y:
            print(j)

    