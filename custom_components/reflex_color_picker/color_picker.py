"""Reflex custom component ColorPicker."""
import reflex as rx

from reflex.vars import Var
from typing import Any


class ColorPickerComp(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
    on_change: rx.EventHandler[lambda e: [e]]


class ColorPicker(rx.ComponentState):
    color: Var[str] = Var("#f00")
    on_change: rx.EventHandler[lambda e: [e]]

    @classmethod
    def get_component(cls, **props) -> Any:
        return ColorPickerComp(color=cls.color, on_change=cls.set_color, **props)
    

color_picker = ColorPicker.create
