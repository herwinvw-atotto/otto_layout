from plotnine.themes import theme, theme_bw, element_rect, element_text
from otto_layout.fonts import add_fonts
from otto_layout.colors import *

add_fonts()

def theme_otto():
    return theme_bw() + theme(text=element_text(family=["OTTO Sans"]), legend_key=element_rect(color='white', fill='white'),\
               strip_background_y=element_text(color = dynamisch['deep_navy']),\
               strip_background_x=element_text(color = dynamisch['deep_navy']),\
               strip_text_y=element_text(color='white'), strip_text_x=element_text(color='white'))