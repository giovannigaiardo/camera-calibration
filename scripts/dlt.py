import numpy as np

def DLT(world_points: np.array, img_points: np.array) -> np.array:
    A = []
    for i in range(len(world_points)):
        x, y, z = world_points[i]
        u, v = img_points[i]
        A.append([x,y,z,1,0,0,0,0,-u*x,-u*y,-u*z,-u])
        A.append([0,0,0,0,x,y,z,1,-v*x,-v*y,-v*z,-v])

    A = np.asarray(A)

    U, S, Vh = np.linalg.svd(A)
    m = Vh[-1,:]
    return m.reshape(3,4)