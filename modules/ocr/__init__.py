import cv2
from PIL import Image
import pytesseract
import platform


# -----------------
# -- Main config --
# -----------------

if platform.system() == 'Windows':
    TESS_PATH='venv/Lib/appdata/local/Tesseract-OCR/tesseract.exe' # TODO: change path
    pytesseract.pytesseract.tesseract_cmd = TESS_PATH
FILENAME='.tmp/screen.png'


