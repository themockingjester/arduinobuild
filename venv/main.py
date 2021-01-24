from kivy.core.text import LabelBase
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout,BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivy.utils import get_color_from_hex as C

class BuilderWindow(MDBoxLayout):
    button = ObjectProperty(None)


class uiApp(MDApp):







    def set_item(self):
        print("gy")

    def build(self):
        self.screen_manager = ScreenManager()

        self.buildersccreen = BuilderWindow()
        screen = Screen(name='builderscreen')
        screen.add_widget(self.buildersccreen)
        self.screen_manager.add_widget(screen)

        menu_items = [{"text": f"Item {i}"} for i in range(5)]
        self.menuk = MDDropdownMenu(
            caller=self.buildersccreen.ids.button,
            items=menu_items,
            width_mult=4,
        )
        self.menuk.bind(on_press=self.set_item)
        return self.screen_manager


LabelBase.register(name='pacifico',fn_regular='fonts/Pacifico/Pacifico-Regular.ttf')
uiApp().run()

