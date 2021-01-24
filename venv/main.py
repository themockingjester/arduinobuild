from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout,BoxLayout
from kivymd.uix.menu import MDDropdownMenu

class BuilderWindow(MDBoxLayout):
    button = ObjectProperty(None)
    button1 = ObjectProperty(None)

class uiApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        self.buildersccreen = BuilderWindow()
        screen = Screen(name='builderscreen')
        screen.add_widget(self.buildersccreen)
        self.screen_manager.add_widget(screen)



        menu_items = [{"text": f"Item {i}"} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.buildersccreen.ids.button1,
            items=menu_items,
            width_mult=4,
        )
        self.menu.bind(on_release=self.menu_callback)
        return self.screen_manager

    def menu_callback(self, instance_menu, instance_menu_item):
        print(instance_menu, instance_menu_item)
LabelBase.register(name='pacifico',fn_regular='fonts/Pacifico/Pacifico-Regular.ttf')
uiApp().run()
