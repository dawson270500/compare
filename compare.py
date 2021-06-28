##Written by Bailey Dawson. 28th June 2021. 
import sys
from datetime import datetime
import os.path

if sys.argv[1] == "-h":
	print("python comapre.py <first file> <second file> <output file: optional>\n\n")
	print("The output file is opened in append mode, so it will add onto the end of files. It will leave a top mark of the time and date and files compared.")
	exit()

if(len(sys.argv) < 3):
	print("Not enough arguements, '-h' for help")
	exit()
	
if(os.path.isfile(sys.argv[1])):
	f1 = open(sys.argv[1], "r") #First file to check
else:
	print("File 1 does not exist")
	exit()

if(os.path.isfile(sys.argv[2])):
	f2 = open(sys.argv[2], "r") #Second File
else:
	print("File 2 does not exist")
	exit()

if len(sys.argv) > 3:
	f3 = open(sys.argv[3], "a") #Output file, optional
else:
	f3 = False

print("Reading Files")

f1arr = []
f2arr = []
for line in f1:
	f1arr.append(line)

for line in f2:
	f2arr.append(line)

print("Files read")
f1.close()
f2.close()

if len(f1arr) != len(f2arr):
	print("File lenghts not the same, will base number of lines off first file.")

if f3 != False:
	f3.write("==="+datetime.now()+"==="+sys.argv[1]+" v "+sys.argv[2]+"===")

for i in range(len(f1arr)):
	if f1arr[i] != f2arr[i]:
		output = "Line " + str(i) + " File 1: " + f1arr[i].replace("\n", "") + " == VS == Line "+str(i)+" File 2: "+f2arr[i].replace("\n", "")
		if f3!=False:
			f3.write(output)
		print(output)

if f3 != False:
	f3.close()