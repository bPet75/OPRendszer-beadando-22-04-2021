#!/usr/bin/python3

import sys
import datetime
tomb = []
for i in range(len(sys.argv)):
	if(i == 73 or i == 74 or i == 103 or i == 104):
		tomb.append(str(sys.argv[i]))

tomb[1] = tomb[1][:-3]
tomb[3] = tomb[3][:-4]

tomb2 = []
tomb2.append(tomb[0] + ' ' + tomb[1])
tomb2.append(tomb[2] + ' ' + tomb[3])
sor = tomb2[1] + ';'+ tomb2[0]

aktual_ = tomb[0]
akttime = tomb[1].split(sep=":")
aktual_ = aktual_[:-1]
aktual_ = aktual_.split(sep=".")

aktual = datetime.datetime(int(aktual_[0]), int(aktual_[1]), int(aktual_[2]), int(akttime[0]), int(akttime[1]))

limit_ = tomb[2]
limtime = tomb[3].split(sep=":")
limit_ = limit_[:-1]
limit_ = limit_.split(sep=".")
limit = datetime.datetime(int(limit_[0]), int(limit_[1]), int(limit_[2]), int(limtime[0]), int(limtime[1]))

me = datetime.datetime(2021, 3, 25, 0, 0, 0)
me = me-aktual
delta = limit - aktual

if (sys.argv[-2] == "TIME"):
	if (sys.argv[-1] == "x"):
		print ('Kiszállítva:\t',aktual)
		print ('Frissítve:\t',limit)
	else:
		print ('Kiszállítva:\t',aktual.strftime(sys.argv[-1]))
		print ('Frissítve:\t',limit.strftime(sys.argv[-1]))

elif (sys.argv[-2] == "DIAG"):
	print ('Lemaradás(nap):\t',delta.days)
	print ("Napok 2021. 3. 25 -ig:\t",me.days)
else:
	if (sys.argv[-1] == "x"):
		print ('Kiszállítva:\t',aktual)
		print ('Frissítve:\t',limit)
	else:
		print ('Kiszállítva:\t',aktual.strftime(sys.argv[-1]))
		print ('Frissítve:\t',limit.strftime(sys.argv[-1]))
	print ('Lemaradás(nap):\t',delta.days)
	print ("Napok 2021. 3. 25 -ig:\t",me.days)

sor = sor+";"+str(delta.days)+"\n"

read = open('data', 'r')
last = read.readlines()[-1]
read.close

if(last != sor):
	out = open('data','a')
	out.write(sor)
	out.close
