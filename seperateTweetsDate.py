# !/usr/bin/python
import os, sys

startdate=str(sys.argv[1])
enddate=str(sys.argv[2])
file=open("NewsTweetsSorted.txt",'r')
out=open("NEWSDATESEPARATED.txt",'w')
data=file.readlines()
startit=0
outputarr=[]
for line in data:
	endday=int(enddate[0:(len(enddate)-7)])
	endmonth=enddate[(len(enddate)-7):(len(enddate)-4)]
	endyear=enddate[(len(enddate)-4):(len(enddate))]
	line=line.replace('\n',"")
	linesplitdata=line.split('\t')
	date=linesplitdata[2]
	datesplit=date.split(" ")
	actualdate=datesplit[0]+datesplit[1]+datesplit[2]
	datetoend=str(endday+1)+endmonth+endyear
#	print actualdate
#	print startdate
	if actualdate==startdate:
		startit=1
	if actualdate==datetoend:
		startit=0
	if startit>0:
		outputarr.append(line)
	elif startit==0:
		continue

out.write("\n".join(outputarr))
#	print currmonth+" "+str(counter)+line.split('\t')[0]
	