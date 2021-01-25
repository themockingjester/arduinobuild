from kivy.core.text import LabelBase
from kivy.config import Config

from kivy.uix.behaviors import DragBehavior
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout,BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import Image
from kivymd.uix.behaviors import TouchBehavior



class ImageButtonWithDoubleTouch(Image,TouchBehavior):
    def on_double_tap(self,instance,*args):
        print(self.source)
class DraggableImageButtonWithDoubleTouch(DragBehavior, ImageButtonWithDoubleTouch):
    pass
class PencilSizeChanger(BoxLayout):
    pass
class BuilderWindow(MDBoxLayout):
    button = ObjectProperty(None)
    container = ObjectProperty(None)

class uiApp(MDApp):

    def selected(self):
        print(self)
    def build(self):
        self.screen_manager = ScreenManager()

        self.buildersccreen = BuilderWindow()
        screen = Screen(name='builderscreen')
        screen.add_widget(self.buildersccreen)
        self.screen_manager.add_widget(screen)

        menu_items = [{"icon": "git",
                       "text": f"Item {i}",
                       "callback": self.selected} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.buildersccreen.button,
            items=menu_items,
            width_mult=3,
        )
        self.menu.bind(on_release=self.menu_callback)


        return self.screen_manager
    def image_adder(self):
        wimg = DraggableImageButtonWithDoubleTouch(source='images/sensors/arduino.png', width=400,size_hint_y= None,size_hint_x= None, height=400)
        self.buildersccreen.container.add_widget(wimg)

    def menu_callback(self, instance_menu, instance_menu_item):
        print("hilk")
        print(instance_menu, instance_menu_item)



LabelBase.register(name='pacifico',fn_regular='fonts/Pacifico/Pacifico-Regular.ttf')
uiApp().run()
