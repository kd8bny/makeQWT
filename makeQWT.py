#Daryl W. Bennett --kd8bny@gmail.com
#Allow the edit of QT Designer files for QWT support
#Custom UI input

#V1 R0
import string, os

def makeQWT():
	edit = '#Edited By: #Daryl W. Bennett --kd8bny@gmail.com \n#QWT5 support added using makeQWT V1 R0 \n\n'
	QWT = 'from PyQt4.Qwt5 import * \n'
	temp = open('main.py', 'r+')
	lines = temp.readlines()
	lines.insert(9,edit)
	lines.insert(11,QWT)
	temp.seek(0)
	temp.writelines(lines)
	temp.close()

if __name__ == "__main__":
	do = makeQWT()
