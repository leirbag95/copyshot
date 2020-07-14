import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from modules.ocr.models import OCRManager as ocr
import numpy as np
from PIL import Image
import pyautogui
import pyperclip


class ScreenManager:
    """
    class: FIXME
    description: Take screenshot of the screen's full size and show it from
                 matplotlib graph.
    """
    @classmethod
    def screenshot(self):
        """ return screenshot"""
        self.screen = pyautogui.screenshot()
        return self.screen

    @classmethod
    def line_select_callback(self, eclick, erelease):
        """eclick and erelease are the press and release events"""
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
        print(" The button you used were: %s %s" % (eclick.button, erelease.button))
        im = self.screen.crop((x1,y1,x2,y2))
        im.save('.tmp/screen.png')
        text = ocr.run_ocr()
        print(text)
        pyperclip.copy(text)
        
    
    def toggle_selector(self, event):
        """ de/active rectangle selector """
        print(' Key pressed.')
        if event.key in ['Q', 'q'] and self.toggle_selector.RS.active:
            print(' RectangleSelector deactivated.')
            self.toggle_selector.RS.set_active(False)
        if event.key in ['A', 'a'] and not self.toggle_selector.RS.active:
            print(' RectangleSelector activated.')
            self.toggle_selector.RS.set_active(True)
    
    @classmethod
    def show_and_select(self):
        """ show the screenshot and allow user to select area """
        _, current_ax = plt.subplots()                 # make a new plotting range
        plt.imshow(self.screenshot())
        print("\n      click  -->  release")
        # drawtype is 'box' or 'line' or 'none'
        self.toggle_selector.RS = RectangleSelector(current_ax, self.line_select_callback,
                                        drawtype='box', useblit=True,
                                        button=[1, 3],  # don't use middle button
                                        minspanx=5, minspany=5,
                                        spancoords='pixels',
                                        interactive=True)
        plt.connect('key_press_event', self.toggle_selector)
        plt.show()
