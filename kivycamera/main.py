# -*- coding: utf-8 -*-
"""
Created on Tue May 10 22:03:46 2022

@author: s_bio
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

import time

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        background_color: (0.2,0.2,0.2,1) if self.state == 'normal' else (1,0,1,1)
        text: 'Correr'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        background_color: (1,0,0,1) if self.state == 'normal' else (0,1,0,0.8)
        text: 'Capturar'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Función para capturar las imágenes y darles los nombres
        de acuerdo a la fecha y hora
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Capturada" + " IMG_{}.png".format(timestr))


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()