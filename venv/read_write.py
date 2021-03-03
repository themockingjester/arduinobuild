import pickle
from image_processing import ImageProcessing
class Open_Saved_File():
    def __init__(self,base,where_to_add,wires,WireBase,DraggableWire):
        self.DraggableWire = DraggableWire
        self.base = base
        self.where_to_add = where_to_add
        self.dic = {}
        for i in wires:                     # adding each wire into a dictionary
            self.dic[i.__name__]=i
        self.wirebase = WireBase
    def open_from_file(self,file_name):
        with open(file_name, 'rb') as handle:
            b = pickle.load(handle)


        for i in range(len(b)):
            data = b[i]
            print(data)

            if isinstance(data[0],str):            # means image
                pos = data[2][1:-1]
                pos = pos.split(",")
                x = pos[0].strip()
                x= x
                y = pos[1].strip()
                y = y

                img = self.base(source=data[0],width=400, size_hint_y=None,size_hint_x=None, height=400, pos=(x,y))
                o = ImageProcessing(img,data[1])

                o.bydefaultrotation()
                self.where_to_add.container.add_widget(img, -1)



            else:                                       # means wire

                #print(data)
                item = data[3]
                k = self.wirebase()
                if 1==1:
                    tobeadded = self.dic[item]()

                    tobeadded.topmost.width = data[0]
                    tobeadded.topmost.height = data[1]

                    pos = data[4][1:-1]
                    pos = pos.split(",")
                    x = pos[0].strip()
                    x = x
                    y = pos[1].strip()
                    y = y
                    print("dekho")
                    for j in tobeadded.topmost.children:
                        for u in j.children:
                            if isinstance(u, self.DraggableWire):
                                # u.actualwire.canvas.before.children[0].rgba = data[2]
                                u.children[0].canvas.before.children[0].rgba=data[2]



                    tobeadded.topmost.pos = (x,y)

                    k.external_container.add_widget(tobeadded)

                self.where_to_add.container.add_widget(k, 0)

class SaveContent():
    def __init__(self,obj1,DraggableImageButtonWithDoubleTouch,DraggableWire):        #getting class frrom main.py
        self.parentobj = obj1
        widgets_counter = 0
        dic = {}
        toplayer_content = self.parentobj.children
        if len(toplayer_content)!= 0:
            for i in toplayer_content:
                #print(i)
                if isinstance(i,DraggableImageButtonWithDoubleTouch):       #checking wheather object was a image

                    dic[widgets_counter] = [i.image,i.angle,str(i.pos),"Image"]

                    widgets_counter+=1


                else:
                    flag = False
                    for k in i.children:
                        for m in k.children:
                            width_of_container=m.topmost.width
                            height_of_container = m.topmost.height
                            pos_of_container = m.topmost.pos
                            for j in m.topmost.children:
                                for u in j.children:
                                    if isinstance(u,DraggableWire):
                                        color=u.children[0].canvas.before.children[0].rgba
                                        print("hi")
                                        dic[widgets_counter] = [width_of_container,height_of_container,color,str(type(j.parent.parent).__name__),str(pos_of_container)]             #j.parent.parent means which type of wire wheather straight wire elbowshapedwire etc
                                        flag = True
                                        break
                                if flag == True:
                                    break
                            if flag==True:
                                break
                        if flag==True:
                            break

                    widgets_counter += 1

            with open('myfile.ab', 'wb') as handle:
                pickle.dump(dic, handle, protocol=pickle.HIGHEST_PROTOCOL)
            with open('myfile.ab', 'rb') as handle:
                b = pickle.load(handle)

                # print(b)