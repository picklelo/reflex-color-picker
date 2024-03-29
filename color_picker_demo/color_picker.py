"""Reflex custom component ColorPicker."""
import reflex as rx

from typing import Any


class ColorPickerComp(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda e: [e]]


class ColorPicker(rx.ComponentState):
    color: str

    def set_color(self, color):
        if self.on_change:
            print(self.on_change)
            self.on_change(color)
        self.color = color

    @classmethod
    def create(cls, on_change=None, **props):
        cls.on_change = on_change
        return super().create(**props)

    @classmethod
    def get_component(cls, **props) -> Any:
        return ColorPickerComp(color=cls.color, on_change=cls.set_color, **props)
    

color_picker = ColorPicker.create
