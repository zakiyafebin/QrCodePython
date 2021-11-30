import qrcode

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


import random
import sys
import os


#QR Code Generator
def qrCode_Generator():    
    # Link for website
    input_data = input("Enter your URL: ")
    #Creating an instance of qrcode
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    randomNo = random.randint(0,100000)
    print("Your QR code is in D:\qrCode\  ")
    print("With a filename: "+"qrcode"+str(randomNo)+".png")
    flag = 0
    #print(os.listdir("D:\\"))
    
    if 'qrCode' in os.listdir("D:\\"):
         img.save('D:\qrCode\qrcode'+str(randomNo)+'.png')
         flag = 1
         #print("inside for",flag)
         
    #print(flag)
    if  flag == 0:
        os.mkdir('D:\qrCode')
        img.save('D:\qrCode\qrcode'+str(randomNo)+'.png')
        
        

    

#QR code Reader from image
def qrcode_Reader_Image():
    imagePath = input("Enter the path to your image: ");
    decodedData = decode(Image.open(imagePath))
    print((decodedData[0][0]))
    print(decodedData[0][1])


    
#QR Code Reader
def qrCode_Reader():

    font = cv2.FONT_ITALIC                 
    video_capture = cv2.VideoCapture(0)

    while True:
        if  video_capture.isOpened():
            #raise Exception("Could not open video device")
            # Set properties. Each returns === True on success (i.e. correct resolution)
            video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
            video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
            # Read picture. ret === True on success
            _, frame = video_capture.read()
            
        decodedData = pyzbar.decode(frame)
        for i in decodedData:#print each letters and digits
            #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
            cv2.putText(frame, str(i .data),(30,100),font,2,(400,50,10),5)
            print(i.data)
        cv2.imshow("Window", frame)

        key = cv2.waitKey(1)
        if key == 32 or cv2.getWindowProperty("Window", cv2.WND_PROP_VISIBLE) <1:
            #breaks  when u enter space bar or X button of the  frame
            break
        if decodedData != []:
            break
        
    video_capture.release()
    cv2.destroyAllWindows()



#Main

while(True):
    print("MENU");
    print("1.QR code Generator")
    print("2.QR Code Reader")
    opt = int (input("Enter your option : (1 or 2) "))
    if opt == 1:
        qrCode_Generator()
    elif opt ==2:
        print("1. QR Code reader from video capture")
        print("2. QR Code reader from an image")
        optionReader = int (input("Enter your option:(1 or 2) "))
        if optionReader == 1:
            print("QR code is :")
            qrCode_Reader()
        elif optionReader == 2:
            qrcode_Reader_Image()
        else:
            print("Wrong Option")
                            
    else:
        print("Wrong Input")
    sys.exit()
