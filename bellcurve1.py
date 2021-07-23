import pandas as pd
import csv
import plotly.figure_factory as px

qwe=pd.read_csv("weight.csv") 
fig=px.create_distplot([qwe["Height(Inches)"].tolist()],["Height"], show_hist=False)
fig.show()