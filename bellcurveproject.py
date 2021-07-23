import plotly.figure_factory as px
import pandas as pd
import csv


qwe=pd.read_csv("./amazon.csv") 
#fig=px.create_distplot([qwe["Avg Rating"].tolist()],["average ratings"],show_hist=False)
fig=px.create_distplot(qwe["Avg Rating"],["Average ratings"])
fig.show()