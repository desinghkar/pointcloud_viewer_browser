import numpy as np
from numpy.linalg import eig, inv
import optparse
parser = optparse.OptionParser()
parser.add_option('-p', '--path', action="store", dest="path", help="path string", default="/home/kar")
options, args = parser.parse_args()
import math

x = np.array([])
y = np.array([])
z = np.array([])
path_text = options.path+'/fitObject.pcd'
c = 0;
with open(path_text, 'r') as f:
    print "inside the file"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))

path_file = '/home/kar/workspace/my_git_repos/brown_robotics_kd/src/image_interaction/www/data/pcd.js'
fh = open(path_file, "w")

lines = ["pclouds = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}];"]
fh.writelines(lines)
fh.close()
#print x,"\n"
#print y,"\n"
'''


lines = [str(center[0]), " ", str(center[1])," ",  str(phi)," ",  str(axes[0]), " ", str(axes[1])]

fh.close()
'''
