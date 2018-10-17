#!/usr/bin/python36
import cv2
import subprocess as sp
import os

path="/code/security_udev/intruder_repo"
date=sp.getoutput("date")
cap = cv2.VideoCapture(0)
ret, image = cap.read()
cv2.imwrite(os.path.join(path,"{}.jpg".format(date)) ,image)
cv2.destroyAllWindows()
cap.release()
