"""
Created by Gabriel ELFASSI
"""
from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt
from modules.screenmanager.models import ScreenManager as SM
from modules.ocr.models import OCRManager as ocr
import numpy as np

if __name__ == "__main__":
    SM.show_and_select()
