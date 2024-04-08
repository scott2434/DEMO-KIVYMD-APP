from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix import navigationdrawer
from kivymd.uix import boxlayout
#from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.list import MDList
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
import requests
import json
from kivy.uix.button import Button


Window.size = (300, 500)


screen_helper = """

ScreenManager:
    LoginScreen:
    MenuScreen:
    NewScreen:


<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: "vertical"
       
        MDToolbar:
            title: "Menu"
            left_action_items: [["menu",lambda x:nav_drawer.set_state('toggle')]]
            elevation: 10
        Widget
       
        Image:
            source: 'COS-Logo.png'
            pos_hint:{"center_x":0.5,"center_y":.9}
            size_hint:(1, 1)
        #Widget
            #MDLabel:
                #text: 'An FNL Project'
                #pos_hint:{"center_x": 0.5,"center_y": 0.5}
                #halign: 'center'
                #font_style: 'H6'
                #bold:True
           
        MDFillRoundFlatButton:
            text:"Find Your Spot"
            pos_hint:{"center_x":0.5,"center_y":0.45}
            #size_hint:(0.17,0.07)
            font_size:20
            on_press:
                root.manager.current = 'login'
                app.create_get()
                our_label.text = str(app.create_get())

        MDLabel:
            id: our_label
            text: ""
            pos_hint: {'center_x': .75, 'center_y': .95}
            font_size:45
            bold: True
        Widget
       
<MenuScreen>:
    name: 'map'
 
    BoxLayout:
        orientation: "vertical"

        Image:
            source :'cos_lot_map1.png'
            allow_stretch: True
            keep_ratio: True
        MDLabel:
            text:"Hello there1"
            halign: "center"                

        MDToolbar:
            title: "Lot A"
            MDBottomNavigation:
                MDBottomNavigationItem:
                    name: 'screen 1'
                    text: 'menu'
                    icon: 'car'
                    #MDLabel:
                        #text: "Hello there2"
                        #halign: "center"
        Image:
            source:'x_resize2.png'
            pos: 45, 110
   

       

<NewScreen>:
    name: "nav"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Map"
                        left_action_items: [["menu",lambda x:nav_drawer.set_state('toggle')]]
                        elevation: 10
                       
                    Widget  

                   
           
        MDNavigationDrawer:
            id: nav_drawer
"""



class LoginScreen(Screen):
    pass


class MenuScreen(Screen,BoxLayout):
    pass

class NewScreen(Screen,BoxLayout):
   pass



#screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))
sm = ScreenManager(transition=SlideTransition())






class DemoApp(MDApp):
    firebase_url = "https://fir-4805d-default-rtdb.firebaseio.com/.json"
   
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        screen = Builder.load_string(screen_helper)
        button = Button(text="try This")
        button.bind(on_press=self.create_get)#+3/26
        #self.add_widget(button)+3/26
        # screen1 = Builder.load_string(screen1)+3/26
        return screen
        return button

    def create_get(self):
        #print("button pressed1")
        res = requests.get(url=self.firebase_url)
        spotText=(res.json())
        print(spotText)
        #label = Label(text=spotText)+3/26
        #self.data_label.text = spotText+3/26
        R = spotText['empty']['row']
        print(R)
        S = spotText['empty']['spot']
        Vac =(f"Row: {R} \nSpot: {S}")
        #return S
        #return spotText
        return Vac
    #words=spotText
   

DemoApp().run()


