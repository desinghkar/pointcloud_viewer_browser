import numpy as np
from numpy.linalg import eig, inv
import optparse
parser = optparse.OptionParser()
parser.add_option('-p', '--path', action="store", dest="path", help="path string", default="/home/kar")
options, args = parser.parse_args()
import math


path_text1 = options.path+'/object.pcd' #red
path_text2 = options.path+'/profile_boundary.pcd' #green
path_text3 = options.path+'/profile.pcd' #yello
path_text4 = options.path+'/axis_start.pcd' #blue
path_text5 = options.path+'/o_cues.pcd' #blue
path_text6 = options.path+'/s_cues.pcd' #white
path_file = '/home/kar/workspace/my_git_repos/brown_robotics_kd/src/image_interaction/www/data/cuesClouds.js'

fh = open(path_file, "w")
#############Object pcd
c = 0;
x = np.array([])
y = np.array([])
z = np.array([])
with open(path_text1, 'r') as f:
    print "inside the file object.pcd"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))


lines = ["pclouds1 = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}]; \n"]
fh.writelines(lines)

#############Profile boundary

c = 0;
x = np.array([])
y = np.array([])
z = np.array([])
with open(path_text2, 'r') as f:
    print "inside the file"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))


lines = ["pclouds2 = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}]; \n"]
fh.writelines(lines)
#############Profile

c = 0;
x = np.array([])
y = np.array([])
z = np.array([])
with open(path_text3, 'r') as f:
    print "inside the file"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))


lines = ["pclouds3 = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}]; \n"]
fh.writelines(lines)
#############Axis start 

c = 0;
x = np.array([])
y = np.array([])
z = np.array([])
with open(path_text4, 'r') as f:
    print "inside the file"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))


lines = ["pclouds4 = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}]; \n"]
fh.writelines(lines)
#############O cues

c = 0;
x = np.array([])
y = np.array([])
z = np.array([])
with open(path_text5, 'r') as f:
    print "inside the file"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))


lines = ["pclouds5 = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}]; \n"]
fh.writelines(lines)
#############S cues

c = 0;
x = np.array([])
y = np.array([])
z = np.array([])
with open(path_text6, 'r') as f:
    print "inside the file"
    data = f.readlines()

    for line in data:
    	c = c+1

    	if c > 11:
       		words = line.split(" ")
       		x = np.append(x, float (words[0]))
       		y = np.append(y, float (words[1]))
       		z = np.append(z, float (words[2]))


lines = ["pclouds6 = [{\"pcloud\":["]
fh.writelines(lines)
for i in range(x.size):
	lines = ["[\"", str(x[i]), "\", \"", str(y[i]), "\", \"", str(z[i]), "\"], "]
	fh.writelines(lines)
lines = ["]}]; \n"]
fh.writelines(lines)
fh.close()
