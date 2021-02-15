from kivy.uix.behaviors import DragBehavior
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.metrics import sp

from main import uiApp,DraggableImageButtonWithDoubleTouch
class DragClass(DragBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def provide_object_here(self,obj):
        self.obj = obj

    def on_long_touch(self, touch, *args):
        print(isinstance(self.obj, DraggableImageButtonWithDoubleTouch))
        if uiApp.dragcounter == False:
            sound=SoundLoader.load('sounds/button.wav')
            if sound:
                sound.play()
            self.obj.export_to_png("temp/usr/application/temp.png")
            uiApp.current_selected_image = self.obj

    def on_touch_move(self, touch):

        #####################################  Predefined code for event ##################

        if self.obj._get_uid('svavoid') in touch.ud or \
                self.obj._drag_touch is not touch:
            return super(DragBehavior, self.obj).on_touch_move(touch) or \
                   self.obj._get_uid() in touch.ud

        if touch.grab_current is not self:
            return True

        uid = self.obj._get_uid()
        ud = touch.ud[uid]
        mode = ud['mode']
        if mode == 'unknown':
            ud['dx'] += abs(touch.dx)
            ud['dy'] += abs(touch.dy)
            if ud['dx'] > sp(self.obj.drag_distance):
                mode = 'drag'
            if ud['dy'] > sp(self.drag_distance):
                mode = 'drag'
            ud['mode'] = mode
        if mode == 'drag':
            if uiApp.dragcounter == True: #my logic only this line

                self.obj.x += touch.dx
                self.obj.y += touch.dy

        return True
    ############################## end #############################

