import cv2
import numpy as np
from tkinter import *
import time
import keras
import PIL
from PIL import Image,ImageTk


def image_capture(img1):
	image = Image.fromarray(img1)
	name = "./res/test_im.png"
	image.save(name)
	time.sleep(0.1)

def predictions():
	model = keras.models.load_model('./res/cnnhdr.h5')
	filename = "./res/test_im.png"
	im = cv2.imread(filename)
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)
	im_invert = cv2.bitwise_not(im_gray)

	roi = cv2.resize(im_gray, (28,28))
	roi = roi.reshape(1, 28, 28, 1)

	predictions = model.predict([roi])
	predictions = np.argmax(predictions, axis=1)
	output = str(predictions[0])
	#text.insert(INSERT,predictions)
	#text.pack()
	#op = Text(root, width=60, height=20)

	#time.sleep(3)
	print(output)
	return output
	
if __name__ == '__main__':
	root = Tk()
	root.geometry("500x500")
	root.configure(bg="lightgreen")
	root.resizable(width=False, height=False)
	Label(root,text="Digit Recogniser",font=("times new roman",15,"bold"),bg="lightgreen",fg="black").pack()
	#Label(root,text=predictions ,font=("times new roman",20,"bold"),bg="gray",fg="yellow").pack()
	text = Text(root,height=15,width=100,font=("times new roman",15,"bold"),bg="lightgreen",fg="black")
	f1 = LabelFrame(root,bg="lightgreen")
	f1.pack()
	L1 = Label(f1,bg="blue",height=300,width=500)
	L1.pack()
	cam = cv2.VideoCapture(0)
	a = 0
	while True:
		a = a + 1
		img = cam.read()[1]
		img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		#img = ImageTk.PhotoImage(Image.fromarray(img1))
		img = ImageTk.PhotoImage(image=PIL.Image.fromarray(img1))
		image_capture(img1)
		L1['image'] = img
		output = predictions()
		output = str(output)+","
		#l1 = Label(root,text = output ,font=("times new roman",20,"bold"),bg="gray",fg="yellow").pack()
		#text.insert(INSERT,"predictions: \n")
		text.insert(INSERT,output)
		text.pack()

		print(a)
		

		root.update()
		if(a==40):
			a = 0
			text.delete(1.0,END)

