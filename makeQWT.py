#Daryl W. Bennett --kd8bny@gmail.com
#Allow the edit of QT Designer files for QWT support
#TODO: Custom UI input

#V1 R1
import string, os

def makeQWT():
	edit = '#Edited By: #Daryl W. Bennett --kd8bny@gmail.com \n#QWT5 support added using makeQWT V1 R1 \n\n'
	QWT = 'from PyQt4.Qwt5 import * \n'
	print "\nmakeQWT V1 loading QT file\n"
	temp = open('libs/main.py', 'r+')
	lines = temp.readlines()
	lines.insert(9,edit)
	lines.insert(11,QWT)
	temp.seek(0)
	temp.writelines(lines)
	print "\nWriting QWT5 import line\n"
	# Remove old crap
	end = len(lines)-14
	temp.seek(end)
	del lines[end:end+4]
	temp.seek(0)
	temp.writelines(lines)
	temp.close()

if __name__ == "__main__":
	do = makeQWT()
	