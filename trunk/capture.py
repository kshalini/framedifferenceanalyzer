import os,time

numFrames=100
waitTime=.1


fifoFileName = 'myFifo.tmp'
os.system('rm shot*.png')
os.system('mkfifo ' + fifoFileName)
os.system('mplayer -slave -input file=myFifo.tmp -vf screenshot tv:// -tv driver=v4l2 &')

time.sleep(2)

for x in range(1,numFrames):
	fileName = 'shot%04d.png'%(x)
	os.system('echo "screenshot 0" >> ' +fifoFileName)
	time.sleep(waitTime)
	
	
	
	

		
# very bad way to exit
os.system('killall mplayer')
exit(1)
