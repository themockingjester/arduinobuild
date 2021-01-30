from kivy.core.text import LabelBase


from kivymd.toast import toast
from image_processing import ImageProcessing
from kivy.core.audio import SoundLoader
from pynput import keyboard
from kivy.metrics import sp
import threading
from kivy.uix.behaviors import DragBehavior
from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout, BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import Image
from kivymd.uix.behaviors import TouchBehavior


class ImageButtonWithDoubleTouch(Image, TouchBehavior):
    pass

class UpperUtilityTray(BoxLayout):
    pass


class PencilSizeChanger(BoxLayout):
    pass


class DraggableImageButtonWithDoubleTouch(DragBehavior, ImageButtonWithDoubleTouch):
    def on_double_tap(self, instance, *args):
        pass
    def on_long_touch(self, touch, *args):

        if uiApp.dragcounter == False:
            sound=SoundLoader.load('sounds/button.wav')
            if sound:
                sound.play()
            self.export_to_png("temp/usr/application/temp.png")
            uiApp.current_selected_image = self

    def on_touch_move(self, touch):
        #####################################  Predefined code for event ##################
        if self._get_uid('svavoid') in touch.ud or \
                self._drag_touch is not touch:
            return super(DragBehavior, self).on_touch_move(touch) or \
                   self._get_uid() in touch.ud
        if touch.grab_current is not self:
            return True

        uid = self._get_uid()
        ud = touch.ud[uid]
        mode = ud['mode']
        if mode == 'unknown':
            ud['dx'] += abs(touch.dx)
            ud['dy'] += abs(touch.dy)
            if ud['dx'] > sp(self.drag_distance):
                mode = 'drag'
            if ud['dy'] > sp(self.drag_distance):
                mode = 'drag'
            ud['mode'] = mode
        if mode == 'drag':
            if uiApp.dragcounter == True: #my logic only this line

                self.x += touch.dx
                self.y += touch.dy

        return True
    ############################## end #############################


class BuilderWindow(MDBoxLayout):
    openbutton = ObjectProperty(None)
    sensorsbutton = ObjectProperty(None)
    basiceqbutton = ObjectProperty(None)
    container = ObjectProperty(None)
    savebutton = ObjectProperty(None)
    additionalmodulesbutton = ObjectProperty(None)
    commonid = ObjectProperty(None)
class uiApp(MDApp):

    current_selected_image = None
    left_tray_color = ObjectProperty(rgba("#282828"))
    bar_color = ObjectProperty(rgba("#282828"))
    dragcounter = False
    upper_utilitytray_color = ObjectProperty(rgba("#282828"))
    workspace_boundary_color = ObjectProperty(rgba("#30475e"))
    def page_size_increaser(self,instance):
        h = instance.parent.parent.parent.parent.parent.parent.parent.parent.container
        height = h.height
        h.size=(h.parent.width,height+h.parent.height)

    def application_look_settings(self,instance):
        pencil_button_color_values = ["#70af85", "#70af85"]
        delete_button_color_values = ["#f05454", "#f05454"]
        workspace_boundary_color_values = ["#30475e", "#D6ED17FF"]
        left_tray_buttons_color_values = ["#00bcd4", "#f88f01"]
        left_tray_color_values = ["#282828","#00af91"]
        bar_color_values = ["#282828","#D6ED17FF"]
        upper_utility_tray_boundary_color_values = ["#00af91", "#D6ED17FF"]
        if self.mode == 0:
            self.mode += 1
        else:
            self.mode -= 1
        if self.mode == 0:
            self.theme_cls.theme_style = "Light"
            try:
                instance.theme_text_color = "Primary"
            except:
                pass
        else:
            self.theme_cls.theme_style = "Dark"
            self.upper_utilitytray_color = rgba(upper_utility_tray_boundary_color_values[self.mode])                #correct here allso
            try:
                instance.theme_text_color = "Custom"
                instance.text_color= self.upper_utilitytray_color
            except:
                pass
        self.pencil_button_color = pencil_button_color_values[self.mode]
        self.delete_button_color = delete_button_color_values[self.mode]


        self.buildersccreen.openbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.savebutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.additionalmodulesbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.sensorsbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.basiceqbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.left_tray_color = rgba(left_tray_color_values[self.mode])
        self.bar_color = rgba(bar_color_values[self.mode])
        self.upper_utilitytray_color = rgba(upper_utility_tray_boundary_color_values[self.mode])            #correctt here
        self.workspace_boundary_color = rgba(workspace_boundary_color_values[self.mode])

    def dragfunctionality(self,instance):
        if uiApp.dragcounter == False:
            uiApp.dragcounter = True
            instance.theme_text_color = "Custom"
            instance.text_color= self.upper_utilitytray_color
        else:
            instance.theme_text_color = "Primary"
            uiApp.dragcounter = False

    def convert_to_png(self,instance):
        self.buildersccreen.container.export_to_png("yash.png")

    def rotation_enabler(self,instance):
        if self.allow_image_rotation == False:
            self.allow_image_rotation = True
            instance.theme_text_color = "Custom"
            instance.text_color = self.upper_utilitytray_color
        else:
            instance.theme_text_color = "Primary"
            self.allow_image_rotation = False

    def rotate_image_left(self):
        if self.allow_image_rotation == True and uiApp.current_selected_image != None:
            obj = ImageProcessing(uiApp.current_selected_image,90)
            obj.rotate_left()
        else:
            if uiApp.current_selected_image != None:
                uiApp.current_selected_image = None

            toast(text="Either you havn't selected any image or you haven't enabled the image rotation feature!!")
    def rotate_image_right(self):
        if self.allow_image_rotation == True and uiApp.current_selected_image != None:
            obj = ImageProcessing(uiApp.current_selected_image, 90)
            obj.rotate_right()
        else:
            if uiApp.current_selected_image != None:
                uiApp.current_selected_image = None

            toast(text="Either you havn't selected any image or you haven't enabled the image rotation feature!!")




    def key_tracker(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
    def on_press(self,key):
        uiApp.current_key = key
        print(key)
    def build(self):
        self.mode = 1  # 0 for light annd 1 for dark
        self.allow_image_rotation = False


        #keyboard_thread = threading.Thread(target=self.key_tracker)
        #keyboard_thread.start()
        self.screen_manager = ScreenManager()

        self.buildersccreen = BuilderWindow()
        screen = Screen(name='builderscreen')
        screen.add_widget(self.buildersccreen)
        self.screen_manager.add_widget(screen)
        self.application_look_settings(None)
        return self.screen_manager

    def image_adder(self):

        wimg = DraggableImageButtonWithDoubleTouch(source='images/sensors/arduino.png', width=400, size_hint_y=None,
                                                   size_hint_x=None, height=400)
        self.buildersccreen.container.add_widget(wimg)




LabelBase.register(name='pacifico', fn_regular='fonts/Pacifico/Pacifico-Regular.ttf')

uiApp().run()
