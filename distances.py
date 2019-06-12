import os
import numpy
import sys

def calculate_distance(coords1,coords2):
    """
    Documentation string.
    This function accepts coords of 2 atoms, and calculates distance between atoms.
    """
    dx2=(coords1[0]-coords2[0])**2
    dy2=(coords1[1]-coords2[1])**2
    dz2=(coords1[2]-coords2[2])**2
    dr=(dx2+dy2+dz2)**0.5
    return dr

def bondcheck(distance):
    if 0<distance<1.5:
        return True
    else:
        return False
#argv 0 is program, argv 1 is the argument. argv1 needs to be the whole path of the file that you want as the argument.
file_location=sys.argv[1]
print(file_location)
xyz_file=numpy.genfromtxt(file_location, skip_header=2, dtype='unicode')
print(xyz_file)
symbols=xyz_file[:,0]
print(symbols)
coordinates=xyz_file[:,1:4]
coordinates=coordinates.astype(numpy.float)
print(coordinates)
howmany=len(symbols)
for i in range(0,howmany):
    for k in range(1,howmany-i):
        howfar=calculate_distance(coordinates[i],coordinates[i+k])
        if bondcheck(howfar) is True:
            print(F'The bond between {symbols[i]} to {symbols[i+k]} has a distance of {howfar}')
        else:
            print(F'There is no bond between {symbols[i]} to {symbols[i+k]}. The distance between the two atoms is {howfar}')
