from matplotlib import font_manager
import os

def add_fonts():
  font_dir = f"{os.path.dirname(__file__)}/../../fonts"
  print(font_dir)
  font_files = font_manager.findSystemFonts(fontpaths=[font_dir])
  for font_file in font_files:
    print(font_file)
    font_manager.fontManager.addfont(font_file)