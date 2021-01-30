from PIL import Image as Im
import time
class ImageProcessing():

    def __init__(self,Img_Obj,degree):
        self.Img_Obj = Img_Obj
        self.degree = degree
    def rotate_left(self):

        color_image = Im.open("temp/usr/application/temp.png")
        transposed = color_image.rotate(-1*self.degree)
        transposed.save("temp/usr/application/temp.png")
        self.Img_Obj.source = "temp/usr/application/temp.png"
        self.Img_Obj.reload()



    def rotate_right(self):
        color_image = Im.open("temp/usr/application/temp.png")
        transposed = color_image.rotate(1 * self.degree)
        transposed.save("temp/usr/application/temp.png")
        self.Img_Obj.source = "temp/usr/application/temp.png"
        self.Img_Obj.reload()
