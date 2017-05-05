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


no_arr = 0

#---------------------------------------support function---------------------------------------#

def dataType(x):
    return {
        'int': 'INT',
        'char': 'CHAR',
        'bool': 'BOOLEAN',
    }[x]

#-----------------Strip left and right-----------------#
def bothSideStrip(stat):
	stat = stat.lstrip()
	stat = stat.rstrip()
	return stat

#-----------------For condtion symbol-----------------#
def findCond(cond):
	if cond.find("==") >= 0:
		return "="
	if cond.find("<=") >= 0:
		return "<="
	if cond.find(">=") >= 0:
		return ">="
	if cond.find("<") >= 0:
		return "<"
	if cond.find(">") >= 0:
		return ">"

#-----------------Extract between two substring-----------------#
def find_between( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

#-----------------Define Array Data Structure-----------------#
def defineArray(array_d,dt,number_arr):
	print array_d
	number_arr = number_arr + 1
	no_arr = str(number_arr)

	if array_d.count('[')==1 :
		i = find_between(array_d,"[","]")
		s = array_d.split('[')
		file.write(s[0]+"_A"+no_arr+": TYPE = ARRAY INT OF REAL;\n")
		file.write(s[0]+": "+s[0]+"_A"+no_arr+";\n")
		file.write(s[0]+"_array"+no_arr+": INT = "+i+";\n")
		file.write(s[0]+"_elem"+no_arr+": REAL = "+s[0]+"["+s[0]+"_array"+no_arr+"]")
	else:
		k = array_d.split('][')
		s = k[0].split('[')[0]
		i1 = k[0].split('[')[1]
		i2 = k[1].split(']')[0]
		file.write(s+"_A"+no_arr+": TYPE = ARRAY INT OF REAL;\n")
		file.write(s+":A"+no_arr+";\n")
		file.write(s+"_array1"+no_arr+": INT = "+i1+";\n")
		file.write(s+"_array2"+no_arr+": INT = "+i2+";\n")
		file.write(s+"_elem"+no_arr+": REAL = "+s+"["+s+"_array1"+no_arr+"]["+s+"_array2"+no_arr+"]")
	return

#-----------------Data Type Declaration-----------------#
def defDataType( string ,file,no_arr):
    string = string[:-1]
    dt = dataType(string.split(' ', 1)[0])
    if '[' in string.split(' ', 1)[1]:
		defineArray(string.split(' ', 1)[1],dt,no_arr)
		return no_arr+1
    file.write(string.split(' ', 1)[1] + " : " + dt)
    return no_arr

#-----------------For loop condition extraction-----------------#
def for_cond_init(cond,init):
	init = bothSideStrip(init)
	cond = bothSideStrip(cond)
	init = init.replace("int","")
	init = bothSideStrip(init)
	v = init.split("=")
	var = bothSideStrip(v[0])
	i1 = bothSideStrip(v[1])
	c2 = findCond(cond)
	g = cond.split(c2)
	i2 = bothSideStrip(g[1])
	c1 = "<="
	return i1,i2,c1,c2,var;
	

#-----------------Read file and parse it to CVC4-----------------#
def cToCvc4(name,fo,file,no_arr):

	#search for main function
	lookup = 'main'
	start=-1;

	for num, line in enumerate(fo, 1):
	    if lookup in line:
	        start = num
	        break

	#abort if main function not found
	if start == -1 :
	    sys.exit("Aborting!!!\nError : main() function is missing")
	

	fo.seek(0)

	l = fo.readlines()

	st = Stack()

	st_assert = 0

	for i in range(start,len(l)):
		l[i] = bothSideStrip(l[i])
		if not l[i] or l[i].startswith('{'):
			continue
		l[i] = l[i].replace("==", " = ")
		l[i] = l[i].replace("&&", " AND ")
		l[i] = l[i].replace("&", " AND ")
		l[i] = l[i].replace("false", " FALSE ")
		l[i] = l[i].replace("true", " TRUE ")
		l[i] = l[i].replace("or", " OR ")
		l[i] = l[i].replace("^", " OR ")
		print l[i]
		if l[i].startswith('int') or l[i].startswith('char') or l[i].startswith('bool'):
			no_arr = defDataType(l[i],file,no_arr)
		elif l[i].startswith('if'):
			cond = find_between(l[i],"(",")")
			st.push('i')
			if st_assert == 0 :
				file.write("ASSERT ")
				st_assert = 1
			file.write("IF "+ cond +" THEN\n")
			continue
		elif l[i].startswith('for'):
			f = find_between(l[i],"(",")")
			f1 = f.split(";")
			init = f1[0]
			cond = f1[1]
			bool_cond = ""
			var="x"
			print "c "+ cond
			if "<" in cond or ">" in cond or "=" in cond :
				print cond + "dk"
				i1,i2,c1,c2,var = for_cond_init(cond,init)
				bool_cond = i1+" "+c1+" "+var+" AND "+cond
			else :
				bool_cond = cond
			st.push('f')
			if st_assert == 0 :
				file.write("ASSERT ")
				st_assert = 1
			file.write("FORALL ( "+var+" : INT) : "+bool_cond+" =>\n")
			continue
		elif l[i].startswith('while'):
			cond = find_between(l[i],"(",")")
			st.push('f')
			var="x"
			if st_assert == 0 :
				file.write("ASSERT ")
				st_assert = 1
			file.write("FORALL ( "+var+" : INT) : "+cond+" =>\n")
			continue
		elif l[i].startswith('}else'):
			st.pop()
			file.write(" ELSE\n")
			st.push('e')
			continue
		elif l[i].startswith('}'):
			if not st.isEmpty():
				if st.peek() == 'f' :
					st.pop()
					l[i+1] = bothSideStrip(l[i+1])
					if not st.isEmpty():
						if (not l[i+1].startswith('}') ) and (st.peek() == 'f' or st.peek() == 'i' or st.peek() == 'e') :
							print st.peek()
							sys.exit("This is not supported by this Parser")

						if l[i+1].startswith('}') and (st.peek() == 'f' or st.peek() == 'i' or st.peek() == 'e') :
							continue

			if not st.isEmpty():
				if st.peek() == 'e' :
					st.pop()
					file.write(" ENDIF")

		elif l[i].startswith('return'):
			break;
		else :
			if st_assert == 0 :
				file.write("ASSERT ")
			file.write(l[i][:-1])
		print st.size()
		if st.isEmpty():
			file.write(" ;\n\n")
			st_assert = 0
		else :
			l[i+1] = bothSideStrip(l[i+1])
			if l[i+1].startswith('}else') or l[i+1].startswith('}') :
				print 'w'
				continue
			else :
				file.write(" AND\n")
		print i
	return no_arr
#---------------------------------------main function---------------------------------------#

# Open a file 1
p = sys.argv
fo = open(p[-3], "r")
fo1 = open(p[-2], "r")
v = p[-1]

#naming file name
name=fo.name
name = name[:-1]
extension="cvc4"
name=name+extension

print name

#creating file for smt2
try:
    os.remove(name)
except OSError:
    pass

file=open(name,'a')
no_arr = 0
no_arr = cToCvc4(name,fo,file,no_arr)
no_arr = cToCvc4(name,fo1,file,no_arr)

for i in range(0,int(v)):
	x = raw_input("Enter first variable to proof sat : ")
	y = raw_input("Enter second variable to proof sat : ")
	file.write("CHECKSAT NOT "+x+" = "+y+" ;\n")

print "Parser is completed it's work.. Done by RK"
sys.exit()

