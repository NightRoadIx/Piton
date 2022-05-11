# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:28:23 2022

@author: s_bio
"""

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"

    def add_item(self, text):
        new_list_item = OneLineIconListItem(text=text)
        new_list_item.add_widget( IconLeftWidget( icon = "language-python") )
        self.root.ids.listcontainer.add_widget(new_list_item)
        self.root.ids.listinput.text = ''


if __name__ == "__main__":
    app = MainApp()
    app.run()
    
    