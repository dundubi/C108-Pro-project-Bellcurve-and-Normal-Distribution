import plotly.figure_factory as ff
import pandas as pd

reader = pd.read_csv("data.csv")
plot = ff.create_distplot([reader["Avg Rating"].tolist()], ["Average Rating"], show_hist = False)
plot.show()