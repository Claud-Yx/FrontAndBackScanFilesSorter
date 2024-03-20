import tkinter as tk
from tkinter.ttk import *
from typing import Literal
from typing import Final


FittingModeLiteral = Literal["fit_width", "fit_height", "both", "fit_original", "none"]


def clamp(_source, _min, _max):
    return max(min(_source, _max), _min)
