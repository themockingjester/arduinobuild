from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button
from image_processing import ImageProcessing
from read_write import SaveContent,Open_Saved_File
#from open_file import Open_Saved_File

from kivy.core.audio import SoundLoader
from pynput import keyboard
from kivy.metrics import sp
from kivy.uix.behaviors import DragBehavior
from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout, BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import Image
from kivymd.uix.behaviors import TouchBehavior
from kivy.uix.widget import Widget
from kivy.uix.colorpicker import ColorPicker




class ImageButtonWithDoubleTouch(Image, TouchBehavior):
    pass


class UpperUtilityTray(BoxLayout):
    extend_wire = ObjectProperty(None)


class PencilSizeChanger(BoxLayout):
    pass


class StraightWireHorizontal(Widget):
    pass


class StraightWireVertical(Widget):
    pass


class CShapedWireTop(Widget):
    pass


class CShapedWireBottom(Widget):
    pass


class CShapedWireLeft(Widget):
    pass


class CShapedWireRight(Widget):
    pass


class ElbowShapedUpperRightWire(Widget):
    pass


class ElbowShapedUpperLeftWire(Widget):
    pass


class ElbowShapedLowerLeftWire(Widget):
    pass


class ElbowShapedLowerRightWire(Widget):
    clr = ObjectProperty(None)


class TouchableWire(BoxLayout, TouchBehavior):
    pass


class DraggableWire(DragBehavior, TouchableWire):
    wire = ObjectProperty(None)

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
            if uiApp.dragcounter == True:  # my logic only this line
                print("f")
                self.parent.parent.x += touch.dx
                self.parent.parent.y += touch.dy

        return True

    ############################## end #############################
    def on_long_touch(self, touch, *args):

        if uiApp.dragcounter == False:
            sound = SoundLoader.load('sounds/button.wav')
            if sound:
                sound.play()

            uiApp.current_selected_widget = self
            print(uiApp.current_selected_widget)


class WireBase(BoxLayout):
    cwire = ObjectProperty(None)
    external_container = ObjectProperty(None)


class DraggableImageButtonWithDoubleTouch(DragBehavior, ImageButtonWithDoubleTouch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        self.image = self.source

    def on_double_tap(self, instance, *args):
        pass

    def on_long_touch(self, touch, *args):
        print(isinstance(self, DraggableImageButtonWithDoubleTouch))
        if uiApp.dragcounter == False:
            sound = SoundLoader.load('sounds/button.wav')
            if sound:
                sound.play()
            self.export_to_png("temp/usr/application/temp.png")
            uiApp.current_selected_widget = self
            print(self.angle)

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
            if uiApp.dragcounter == True:  # my logic only this line

                self.x += touch.dx
                self.y += touch.dy

        return True
    ############################## end #############################


class BuilderWindow(MDBoxLayout):
    openbutton = ObjectProperty(None)
    upperutilitytray = ObjectProperty(None)
    sensorsbutton = ObjectProperty(None)
    basiceqbutton = ObjectProperty(None)
    container = ObjectProperty(None)
    savebutton = ObjectProperty(None)
    addwiresbutton = ObjectProperty(None)
    commonid = ObjectProperty(None)


class uiApp(MDApp):
    dialog = None

    wireinitialheight = 40
    wireinitialwidth = 100
    need_to_draw_with_pencil = False
    current_selected_widget = None
    left_tray_color = ObjectProperty(rgba("#282828"))
    bar_color = ObjectProperty(rgba("#282828"))
    dragcounter = False
    upper_utilitytray_color = ObjectProperty(rgba("#282828"))
    workspace_boundary_color = ObjectProperty(rgba("#30475e"))

    def page_size_increaser(self, instance):

        h = instance.parent.parent.parent.parent.parent.parent.parent.parent.container
        height = h.height
        h.size = (h.parent.width, height + h.parent.height)

    def wire_shrinker_vertically(self):
        currentheight = uiApp.current_selected_widget.parent.parent.height
        currentheight -= 5

        uiApp.current_selected_widget.parent.parent.height = currentheight

    def wire_extender_vertically(self):
        if 1 == 1:
            currentheight = uiApp.current_selected_widget.parent.parent.height
            currentheight += 5

            uiApp.current_selected_widget.parent.parent.height = currentheight

    def wire_shrinker_horizontally(self):
        currentwidth = uiApp.current_selected_widget.parent.parent.width
        currentwidth -= 50

        uiApp.current_selected_widget.parent.parent.width = currentwidth

    def wire_extender_horizontally(self):

        if 1 == 1:
            currentwidth = uiApp.current_selected_widget.parent.parent.width
            currentwidth += 50

            uiApp.current_selected_widget.parent.parent.width = currentwidth

    def application_look_settings(self, instance):
        pencil_button_color_values = ["#70af85", "#70af85"]
        delete_button_color_values = ["#f05454", "#f05454"]
        workspace_boundary_color_values = ["#30475e", "#D6ED17FF"]
        left_tray_buttons_color_values = ["#00bcd4", "#f88f01"]
        left_tray_color_values = ["#282828", "#00af91"]
        bar_color_values = ["#282828", "#D6ED17FF"]
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
            self.upper_utilitytray_color = rgba(
                upper_utility_tray_boundary_color_values[self.mode])  # correct here allso
            try:
                instance.theme_text_color = "Custom"
                instance.text_color = self.upper_utilitytray_color
            except:
                pass
        self.pencil_button_color = pencil_button_color_values[self.mode]
        self.delete_button_color = delete_button_color_values[self.mode]

        self.buildersccreen.openbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.savebutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.addwiresbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.sensorsbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.buildersccreen.basiceqbutton.md_bg_color = rgba(left_tray_buttons_color_values[self.mode])
        self.left_tray_color = rgba(left_tray_color_values[self.mode])
        self.bar_color = rgba(bar_color_values[self.mode])
        self.upper_utilitytray_color = rgba(upper_utility_tray_boundary_color_values[self.mode])  # correctt here
        self.workspace_boundary_color = rgba(workspace_boundary_color_values[self.mode])

    def dragfunctionality(self, instance):
        if uiApp.dragcounter == False:
            uiApp.dragcounter = True
            instance.theme_text_color = "Custom"
            instance.text_color = self.upper_utilitytray_color
        else:
            instance.theme_text_color = "Primary"
            uiApp.dragcounter = False

    def convert_to_png(self, instance):
        self.buildersccreen.container.export_to_png("yash.png")

    def rotation_enabler(self, instance):
        if self.allow_image_rotation == False:
            self.allow_image_rotation = True
            instance.theme_text_color = "Custom"
            instance.text_color = self.upper_utilitytray_color
        else:
            instance.theme_text_color = "Primary"
            self.allow_image_rotation = False

    def rotate_image_left(self):
        if uiApp.current_selected_widget != None:
            if isinstance(uiApp.current_selected_widget, DraggableImageButtonWithDoubleTouch):
                if self.allow_image_rotation == True:
                    obj = ImageProcessing(uiApp.current_selected_widget, 90)
                    obj.rotate_left()
                else:
                    if uiApp.current_selected_widget != None:
                        uiApp.current_selected_widget = None
            else:
                pass
        else:
            toast("you havn't selected object")

    def rotate_image_right(self):
        if uiApp.current_selected_widget != None:
            if isinstance(uiApp.current_selected_widget, DraggableImageButtonWithDoubleTouch):
                if self.allow_image_rotation == True:
                    obj = ImageProcessing(uiApp.current_selected_widget, 90)
                    obj.rotate_right()
                else:
                    if uiApp.current_selected_widget != None:
                        uiApp.current_selected_widget = None
            else:
                pass
        else:
            toast("you havn't selected object")

    def pencil_drawing_enabler(self):
        if uiApp.need_to_draw_with_pencil == False:
            uiApp.need_to_draw_with_pencil = True
        else:
            uiApp.need_to_draw_with_pencil = False

    def key_tracker(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        uiApp.current_key = key
        print(key)

    def build(self):

        self.mode = 1  # 0 for light annd 1 for dark
        self.allow_image_rotation = False

        # keyboard_thread = threading.Thread(target=self.key_tracker)
        # keyboard_thread.start()
        self.screen_manager = ScreenManager()

        self.buildersccreen = BuilderWindow()
        screen = Screen(name='builderscreen')
        screen.add_widget(self.buildersccreen)
        self.screen_manager.add_widget(screen)
        self.application_look_settings(None)

        sensors_menu_items = [{"text": "arduino"}, {"text": "HC-SR04-Ultrasonic-Sensor"}, {"text": "ir_sensor"},
                              {"text": "microphone_sensor"}
            , {"text": "MQ2-gas-sensor"}, {"text": "passive_buzzer"}, {"text": "rain_detection_sensor"},
                              {"text": "vibration-sensor-module-sw-420"}]
        self.sensors_menu = MDDropdownMenu(
            callback=self.sensor_adder, items=sensors_menu_items, width_mult=4,
            caller=self.buildersccreen.sensorsbutton
        )
        wires_menu_items = [{"text": "vertical straight wire"},
                            {"text": "horizontal straight wire"},
                            {"text": "L shaped wire lower left"},
                            {"text": "L shaped wire lower right"},
                            {"text": "L shaped wire upper left"},
                            {"text": "L shaped wire upper right"},
                            {"text": "C shaped wire left"},
                            {"text": "C shaped wire right"},
                            {"text": "C shaped wire top"},
                            {"text": "C shaped wire bottom"}
                            ]
        self.wires_menu = MDDropdownMenu(
            callback=self.wire_adder, items=wires_menu_items, width_mult=5,
            caller=self.buildersccreen.addwiresbutton
        )
        basic_equipments_menu_items = [{"text": "breadboard"}]
        self.basic_equipments_menu = MDDropdownMenu(
            callback=self.basic_equipments_adder, items=basic_equipments_menu_items, width_mult=4,
            caller=self.buildersccreen.basiceqbutton
        )
        return self.screen_manager

    def basic_equipments_adder(self, instance):
        selected_equipment = instance.text
        selected_equipment_path = "images/sensors/" + selected_equipment + ".png"
        img = DraggableImageButtonWithDoubleTouch(source=selected_equipment_path, width=400, size_hint_y=None,
                                                  size_hint_x=None, height=400)

        self.buildersccreen.container.add_widget(img, 1)

    def sensor_adder(self, instance):
        selected_sensor = instance.text
        selected_sensor_path = "images/sensors/" + selected_sensor + ".png"
        img = DraggableImageButtonWithDoubleTouch(source=selected_sensor_path, width=400, size_hint_y=None,
                                                  size_hint_x=None, height=400)

        self.buildersccreen.container.add_widget(img, -1)

    def wire_adder(self, instance):
        item = instance.text
        k = WireBase()
        if item == "vertical straight wire":
            tobeadded = StraightWireVertical()
            k.external_container.add_widget(tobeadded)
        elif item == "horizontal straight wire":
            tobeadded = StraightWireHorizontal()
            k.external_container.add_widget(tobeadded)
        elif item == "L shaped wire lower left":
            tobeadded = ElbowShapedLowerLeftWire()
            k.external_container.add_widget(tobeadded)
        elif item == "L shaped wire lower right":
            tobeadded = ElbowShapedLowerRightWire()
            k.external_container.add_widget(tobeadded)
        elif item == "L shaped wire upper left":
            tobeadded = ElbowShapedUpperLeftWire()
            k.external_container.add_widget(tobeadded)
        elif item == "L shaped wire upper right":
            tobeadded = ElbowShapedUpperRightWire()
            k.external_container.add_widget(tobeadded)
        elif item == "C shaped wire left":
            tobeadded = CShapedWireLeft()
            k.external_container.add_widget(tobeadded)
        elif item == "C shaped wire right":
            tobeadded = CShapedWireRight()
            k.external_container.add_widget(tobeadded)
        elif item == "C shaped wire top":
            tobeadded = CShapedWireTop()
            k.external_container.add_widget(tobeadded)
        elif item == "C shaped wire bottom":
            tobeadded = CShapedWireBottom()
            k.external_container.add_widget(tobeadded)

        self.buildersccreen.container.add_widget(k, 0)

        # uiApp.kl = wimg

    def remove_selected_widget(self):
        print("hi")
        if isinstance(uiApp.current_selected_widget, DraggableWire):

            self.buildersccreen.container.remove_widget(
                uiApp.current_selected_widget.parent.parent.parent.parent.parent)  # <<<<--- referring to wirebase class
        else:
            self.buildersccreen.container.remove_widget(uiApp.current_selected_widget)

    def yes_clear_page(self):
        print("gkj")
        self.buildersccreen.container.clear_widgets()

    def show_alert_dialog(self, title, message):
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,

                text=message,
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_release=self.yes_clear_page
                    ),
                ],
            )
        self.dialog.open()

    def save_data(self):
        o = SaveContent(self.buildersccreen.container, DraggableImageButtonWithDoubleTouch)

    def color_chooser(self):
        content = Button(text='Close me!', size_hint_y=0.1)
        popup = Popup(title="Theme color")

        box = BoxLayout(orientation='vertical')
        clr_picker = ColorPicker()

        def on_color(instance, value):
            # self.current_selected_widget.clr.color=instance.color
            print(instance.color)
            for i in (self.current_selected_widget.parent.parent).children:
                for j in i.children:
                    if isinstance(j, DraggableWire):
                        child = j.children[0]
                        child.canvas.before.children[0].rgba = instance.color
            # child = self.current_selected_widget.children[0]
            # child.canvas.before.children[0].rgba = instance.color

        clr_picker.bind(color=on_color)
        box.add_widget(clr_picker)
        content.bind(on_press=popup.dismiss)
        box.add_widget(content)
        popup.add_widget(box)
        popup.open()

    def open_saved_file(self):
        self.yes_clear_page()
        o = Open_Saved_File(DraggableImageButtonWithDoubleTouch,self.buildersccreen)
        o.open_from_file("myfile.pickle")


LabelBase.register(name='pacifico', fn_regular='fonts/Pacifico/Pacifico-Regular.ttf')

uiApp().run()
