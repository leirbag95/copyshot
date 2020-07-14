import cv2
from PIL import Image
import pytesseract

# -----------------
# -- Main config --
# -----------------

TESS_PATH='venv/Lib/appdata/local/Tesseract-OCR/tesseract.exe' # TODO: change path
pytesseract.pytesseract.tesseract_cmd = TESS_PATH
FILENAME='.tmp/screen.png'


