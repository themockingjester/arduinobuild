
from main import DraggableImageButtonWithDoubleTouch
import pickle
class Open_Saved_File:
    def open_from_file(file_name):
        with open(file_name, 'rb') as handle:
            b = pickle.load(handle)
        for i in range(len(b)):
            data = b[i]
            print(data)
            # selected_sensor_path = data[0]
            # selected_sensor_angle = data[1]
            # selected_sensor_pos = list(data[2])
            # img = DraggableImageButtonWithDoubleTouch(source=selected_sensor_path, width=400, size_hint_y=None,
            #                                           size_hint_x=None, height=400)
            #
            # self.where_to_add.add_widget(img, -1)






