import pickle
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