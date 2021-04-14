import tkinter as tk
from tkinter import INSERT,END
from tkinter import simpledialog
from PIL import Image,ImageDraw
import joblib
import numpy as np
import cv2
import sklearn
import matplotlib.pyplot as plt
class ImageGenerator:
    def __init__(self,parent,posx,posy,*kwargs):
        self.parent = parent
        self.posx = posx
        self.posy = posy
        self.sizex = 200
        self.sizey = 200
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.drawing_area=tk.Canvas(self.parent,width=self.sizex,height=self.sizey,bg = "white")
        self.drawing_area.place(x=self.posx,y=self.posy)
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.b1down)
        self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
        self.button=tk.Button(self.parent,text="Predict!",width=10,bg='white',command=self.save_and_predict)
        self.button2=tk.Button(self.parent,text="predict_from_image!",width=20,bg='white',command=self.predict_from_image)
        self.button.place(x=self.sizex/7,y=self.sizey+20)
        self.button2.place(x=self.sizex/7,y=self.sizey+50)
        self.button1=tk.Button(self.parent,text="Clear!",width=10,bg='white',command=self.clear)
        self.button1.place(x=(self.sizex/7)+80,y=self.sizey+20)

        self.image=Image.new("RGB",(200,200),(0,0,0))
        self.draw=ImageDraw.Draw(self.image)
        self.model = joblib.load("./res/svm_4label_linear")
        #self.text = tk.Text(self.parent, height=20,width=20,bd=3,padx=0,pady=0)


    def save_and_predict(self):
        filename = "./res/temp.jpg"
        self.image.save(filename)
        im = cv2.imread(filename)
        roi = cv2.resize(im, (28, 28))
        roi = np.mean(roi,axis=2)
        roi = np.array(roi)
        roi = roi.reshape(784,)
        predictions = self.model.predict([roi])
        predictions = "Prediction: " + str(predictions[0]) + "\n"
        text.insert(INSERT,predictions)
        text.pack()
    
    def predict_from_image(self):
        img_location = simpledialog.askstring(title="location", prompt="enter image location:")
        #filename = "./res/temp.jpg"
        filename = img_location
        #self.image.save(filename)
        im = cv2.imread(filename)
        #size=(28,28)
        roi = cv2.resize(im, (28,28))
        # grid_data = roi

        # grid_data = [] 
        # for i in im:
        #     grid_data.append(i.reshape(28,28))

        # grid_data = X_train.values[0].reshape(28,28)
        # print(len(X_train))
        # plt.imshow(grid_data,interpolation=None,cmap="gray")
        # plt.title(Y_train.values[40])
        # plt.show()
        roi = np.mean(roi,axis=2)
        roi = np.array(roi)
        roi = roi.reshape(784,)
        predictions = self.model.predict([roi])
        predictions = "Prediction: " + str(predictions[0]) + "\n"
        text.insert(INSERT,predictions)
        text.pack()
        #plt.imshow(roi)
        #plt.show()


    def clear(self):
        self.drawing_area.delete("all")
        self.image=Image.new("RGB",(200,200),(0,0,0))
        self.draw=ImageDraw.Draw(self.image)
        text.delete(1.0,END)

    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='true',width=18,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(255,255,255),width=6)

        self.xold = event.x
        self.yold = event.y

#if __name__ == "__main__":
root=tk.Tk()
root.wm_geometry("%dx%d+%d+%d" % (600,400, 10, 10))
root.config(bg='white')
root.resizable(width=False, height=False)
text = tk.Text(root, height=20,width=20,bd=3,padx=0,pady=0)
ImageGenerator(root,10,10)
root.mainloop()