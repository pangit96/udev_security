#!/usr/bin/python36
import cv2
import subprocess as sp
import os

cmd1="tar -cvf intruder.tar intruder_repo"
cmd2="ping -c 5 8.8.8.8"
cmd3=("ansible-playbook mail.yml --vault-password-file=/code/security_udev/key.txt")

path="/code/security_udev/intruder_repo"
date=sp.getoutput("date")
cap = cv2.VideoCapture(0)
ret, image = cap.read()
cv2.imwrite(os.path.join(path,"{}.jpg".format(date)) ,image)
cv2.destroyAllWindows()
cap.release()



status=sp.getstatusoutput(cmd2)

if status[0]==0:
	sp.getoutput(cmd1)
	sp.getoutput("rm -rf /code/security_udev/intruder_repo/*.jpg")
	sp.getoutput(cmd3)
	
