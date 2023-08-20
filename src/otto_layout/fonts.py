from matplotlib import font_manager
import os

def add_fonts():
  local_font_dir = f"{os.path.dirname(__file__)}/../../fonts"
  package_font_dir = f"{os.path.dirname(__file__)}/../../../../src/otto_layout/fonts"
  print(package_font_dir)
  font_files = font_manager.findSystemFonts(fontpaths=[local_font_dir, package_font_dir])
  for font_file in font_files:
    print(font_file)
    font_manager.fontManager.addfont(font_file)