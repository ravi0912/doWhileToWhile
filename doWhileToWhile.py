#
#   Created by Ravi Kumar
#
#   Date Mar 22,2017
#

#!/usr/bin/python
import sys
import os
import re
import string
from sys import getsizeof
from sets import Set
from pythonds.basic.stack import Stack

#-----------------Read file and parse it to CVC4-----------------#
def doWhileToWhile(fo,file):
	in_file = []

	with fo as f:
		in_file = f.readlines()

	out_file = []

	exist_while = 1
	lookupDo = "do{"
	lookupWhile = "}while"
	lookupReturn = "return"
	z=0
	while exist_while :
		out_file=[]
		print str(z)+"dsds"
		z = z+1
		start = ""
		end = ""
		start_index = -1
		end_index = -1
		st = Stack()
		st_index = Stack()
		i = 0
		for i in range(len(in_file)):
			print in_file[i]
			if lookupReturn in in_file[i]:
				continue
			if lookupDo in in_file[i]:
				st.push(in_file[i])
				print st.size()+10000000
				st_index.push(i)
			elif lookupWhile in in_file[i]:
				if st.size() == 1:
					start = st.peek()
					start_index = st_index.peek()
					print in_file[i]
					st.pop()
					st_index.pop()
					end = in_file[i]
					end_index = i
					break
				else:
					st.pop()
					st_index.pop()

		if start_index == end_index or start_index == -1 or end_index == -1 :
			if not st.isEmpty():
				print "The code given as input is wrong. Please, check and try again.\n Line No:"+st.top()
			break

		end = end.replace("}while", "while")
		end = end.replace(";", "")
		end = end+"{\n"
		
		print str(end_index)+"ss"+str(start_index)
		for i in range(len(in_file)):
			if i != start_index and i < end_index:
				out_file.append(in_file[i])
			
		for i in range(len(in_file)):
			if i == start_index:
				out_file.append(end)
			elif i == end_index:
				out_file.append("}\n")
			elif i > start_index:
				out_file.append(in_file[i])		
		
		in_file = []
		in_file = out_file
	

	print in_file
	with file as f:
		f.writelines(in_file)	
	return

# Open a file 1
p = sys.argv
fo = open(p[-1], "r")

#naming file name
name=fo.name
name = name[:-2]
extension="RK.c"
name=name+extension

print name

#creating file for smt2
try:
    os.remove(name)
except OSError:
    pass

file=open(name,'w')

doWhileToWhile(fo,file)

print "Conversion has been done successfully..\nThank you for using it!!\n Done by RK"
sys.exit()

