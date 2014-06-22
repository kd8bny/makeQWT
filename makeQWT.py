#Daryl W. Bennett --kd8bny@gmail.com
#Allow the edit of QT Designer files for QWT support
#TODO: Custom UI input

#V1
import string, os, shutil

def makeQWT():
	edit = '#Edited By: #Daryl W. Bennett --kd8bny@gmail.com \n#QWT5 support added using makeQWT V1 R1 \n\n'
	QWT = 'from PyQt4.Qwt5 import * \n'
	print "\nmakeQWT V1 loading QT file\n"
	shutil.copyfile('../libs/main.py','../libs/main_old.py')
	temp = open('../libs/main_old.py', 'r+')
	lines = temp.readlines()
	lines.insert(9,edit)
	lines.insert(11,QWT)
	print "\nWriting QWT5 import line\n"
	# Remove old crap
	end = len(lines)
	del lines[end-13:end-10]
	temp.close()

	temp = open('../libs/main.py', 'r+')
	temp.writelines(lines)
	temp.close()

if __name__ == "__main__":
	do = makeQWT()
	