import argparse
import cv2
from modules.ocr import FILENAME
import os
from PIL import Image
import pytesseract


class OCRManager:

    @classmethod
    def to_grayscale(self, image):
        """ load the example image and convert it to grayscale """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    @classmethod
    def preprocess(self, t_preprocess, gray_image):
        """ check to see if we should apply thresholding to preprocess the image"""
        gray=gray_image
        if t_preprocess == "thresh":
            gray = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        elif t_preprocess == "blur":
            gray = cv2.medianBlur(gray_image, 3)
        return gray
    
    @classmethod
    def run_ocr(self):
        """ load the screenshot and apply OCR to it"""
        tmp_screen=cv2.imread(FILENAME)
        gray_screen = self.to_grayscale(tmp_screen)
        gray_screen = self.preprocess("thresh", gray_screen)
        text = pytesseract.image_to_string(gray_screen)
        return text
        
        