import pickle
from image_processing import ImageProcessing
class Open_Saved_File():
    def __init__(self,base,where_to_add):
        self.base = base
        self.where_to_add = where_to_add
    def open_from_file(self,file_name):
        with open(file_name, 'rb') as handle:
            b = pickle.load(handle)
        for i in range(len(b)):
            data = b[i]

            if data[0].endswith(".png"):            # means image
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
                print(False)
            # selected_sensor_path = data[0]
            # selected_sensor_angle = data[1]
            # selected_sensor_pos = list(data[2])
            # img = DraggableImageButtonWithDoubleTouch(source=selected_sensor_path, width=400, size_hint_y=None,
            #                                           size_hint_x=None, height=400)
            #
            # self.where_to_add.add_widget(img, -1)

class SaveContent():
    def __init__(self,obj1,DraggableImageButtonWithDoubleTouch):        #getting class frrom main.py
        self.parentobj = obj1
        widgets_counter = 0
        dic = {}
        toplayer_content = self.parentobj.children
        if len(toplayer_content)!= 0:
            for i in toplayer_content:
                #print(i)
                if isinstance(i,DraggableImageButtonWithDoubleTouch):       #checking wheather object was a image
                    print(i.source)
                    print(i.angle)
                    print(i.pos)
                    print(type(i))
                    dic[widgets_counter] = [i.image,i.angle,str(i.pos)]
                    print(dic)
                    widgets_counter+=1
                    with open('myfile.pickle','wb') as handle:
                        pickle.dump(dic,handle,protocol=pickle.HIGHEST_PROTOCOL)
                    with open('myfile.pickle','rb') as handle:
                        b = pickle.load(handle)
                        print(b)
                        #print(dic==b)
                else:
                   print("no")