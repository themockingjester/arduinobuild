from PIL import Image as Im
import time

class ImageProcessing():

    def __init__(self,Img_Obj,degree):
        self.Img_Obj = Img_Obj
        self.degree = degree
    def bydefaultrotation(self):                 # this fuction was added very late
        img = Im.open(self.Img_Obj.image)
        img.save("temp/usr/application/temp.png")

        color_image = Im.open("temp/usr/application/temp.png")
        transposed = color_image.rotate(int(self.degree), expand = 1)
        transposed.save("temp/usr/application/temp.png")

        self.Img_Obj.source = "temp/usr/application/temp.png"

        self.Img_Obj.reload()

        self.Img_Obj.angle = self.degree
        # print("sensor image angle is " + str(self.Img_Obj.angle))
    def rotate_left(self):

        color_image = Im.open("temp/usr/application/temp.png")
        self.Img_Obj.angle = self.Img_Obj.angle - self.degree
        if self.Img_Obj.angle == -360:
            self.Img_Obj.angle = 0
        transposed = color_image.rotate(-1*self.degree)
        transposed.save("temp/usr/application/temp.png")
        self.Img_Obj.source = "temp/usr/application/temp.png"
        self.Img_Obj.reload()
        print("sensor image angle is "+str(self.Img_Obj.angle))



    def rotate_right(self):
        color_image = Im.open("temp/usr/application/temp.png")
        self.Img_Obj.angle = self.Img_Obj.angle + self.degree
        if self.Img_Obj.angle == 360:
            self.Img_Obj.angle = 0
        transposed = color_image.rotate(1 * self.degree)
        transposed.save("temp/usr/application/temp.png")
        self.Img_Obj.source = "temp/usr/application/temp.png"
        self.Img_Obj.reload()
        print("sensor image angle is " + str(self.Img_Obj.angle))