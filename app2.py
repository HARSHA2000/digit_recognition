from subprocess import call
from tkinter import *

class CallPy(object):

	def __init__(self, camerapath = "./res/project_tkinter_cam.py", canvaspath = "./res/draw.py"):
		self.camerapath = camerapath
		self.canvaspath = canvaspath

	def call_camera_py(self):
		call(["python","{}".format(self.camerapath)])

	def call_canvas_py(self):
		call(["python","{}".format(self.canvaspath)])

def predictfromcanvas():
    canvas = CallPy()
    canvas.call_canvas_py()
    return True

def predictfromcamera():
    camera = CallPy()
    camera.call_camera_py()
    return True

root = Tk()
root.configure(bg='lightgreen')
#text = Text(root, state=DISABLED)
root.geometry("300x300")
root.resizable(width=False, height=False)
root.title("DIGIT RECOGNISER")
Label(root,text="Digit Recogniser",font=("times new roman",15,"bold"),bg="orange",fg="black").pack()
Label(root,text="Press this button to detect from canvas(by drawing)",font=("times new roman",10,"bold"),anchor="w",bg="lightgreen",fg="black").pack()
btn = Button(root, text="predict from canvas", command=predictfromcanvas)
btn.pack(padx=20, pady=30)
Label(root,text="Press this button to detect from camera",font=("times new roman",10,"bold"),anchor="w",bg="lightgreen",fg="black").pack()
btn1 = Button(root, text="predictfromcamera", command=predictfromcamera)
btn1.pack(padx=20, pady=30)

root.mainloop()