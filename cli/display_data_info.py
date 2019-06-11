import questionary
import loading_files

# Data science imports
import pandas as pd
import numpy as np

from bokeh.plotting import figure, output_file, show


def get_file_information():
    filename = loading_files.browse_file_search()
    filetype = loading_files.select_file_type()
    return loading_files.read_file(filetype, filename)

def get_column_names(df):
    return df.columns

def get_first_five_lines(df):
    return df.head()


#df = get_file_information()

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

output_file("lines.html")

p = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")
p.line(x,y, legend="Temp.", line_width=2)
show(p)