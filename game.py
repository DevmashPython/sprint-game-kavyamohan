import  msvcrt
import time
finish=10
count=0
a=0
print"press enter key to get started"
raw_input()
s_time=time.time()
while(1):
	key=msvcrt.getch()

	if key=='d':
		count=count+1
		print"-->",
	

		if count==finish:
			break
print"go down"
		
finish=10
count=0
while(1):
	key=msvcrt.getch()

	if key=='s':
		count=count+1
		print"\t\t\t\t\t|"
		if count==finish:
			break
print"\t\t\t\t\tgo right"

finish=10
count=0
while(1):
	key=msvcrt.getch()

	if key=='d':
		count=count+1
		if a==0:
			print"\t\t\t\t\t",
			a=1
		print"-->",

		if count==finish:
			break
time_elasped=time.time()-s_time

print"\ncongrats you hav finished" 
print "\nthe time taken %s"%str(time_elasped)
