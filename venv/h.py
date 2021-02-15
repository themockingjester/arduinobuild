# from kivy.lang import Builder
#
# from kivymd.app import MDApp
# from kivymd.uix.menu import MDDropdownMenu
#
# KV = '''
# Screen:
#
#     MDRaisedButton:
#         id: button
#         text: "PRESS ME"
#         pos_hint: {"center_x": .5, "center_y": .5}
#         on_release: app.menu.open()
# '''
#
#
# class Test(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.screen = Builder.load_string(KV)
#         menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
#         self.menu = MDDropdownMenu(
#             callback=self.clicked, items=menu_items, width_mult=4,caller=self.screen.ids.button
#         )
#



#     def build(self):
#         return self.screen
#     def clicked(self,instance):
#         print(instance.text)
#
#
#
# Test().run()



from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
Screen:

    MDRaisedButton:
        id: button
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
'''


class CustomDrop(MDDropdownMenu):
    def set_bg_color_items(self, instance_selected_item):
        if self.selected_color and not MDApp.get_running_app().submenu:
            for item in self.menu.ids.box.children:
                if item is not instance_selected_item:
                    item.bg_color = (0, 0, 0, 0)
                else:
                    instance_selected_item.bg_color = self.selected_color


class Test(MDApp):
    submenu = None

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "icon": "git",
                "text": f"Item {i}" if i != 3 else "Open submenu",
            }
            for i in range(5)
        ]
        self.menu = CustomDrop(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4,
            selected_color=self.theme_cls.bg_darkest
        )
        self.menu.bind(on_enter=self.check_item)

    def check_item(self, menu, item):
        if item.text == "Open submenu" and not self.submenu:
            menu_items = [{"text": f"Item {i}"} for i in range(5)]
            self.submenu = MDDropdownMenu(
                caller=item,
                items=menu_items,
                width_mult=4,
                selected_color=self.theme_cls.bg_darkest,
            )
            self.submenu.bind(on_dismiss=self.set_state_submenu)
            self.submenu.open()

    def set_state_submenu(self, *args):
        self.submenu = None

    def build(self):
        return self.screen


Test().run()