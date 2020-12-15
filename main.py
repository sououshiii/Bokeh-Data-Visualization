from bokeh.io import output_file, show
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import row, column
import pandas_datareader as pdr
import datetime

start_date = datetime.datetime(2019, 11, 1)
end_date = datetime.datetime(2020, 11, 30)

bmw_df = pdr.DataReader(name="BMW.DE", data_source="yahoo", start=start_date, end=end_date)

plot = figure(x_axis_type="datetime", plot_width=1000, title="BMW")
time = 12*60*60*1000

plot.segment(bmw_df.index, bmw_df.High, bmw_df.index, bmw_df.Low, color="black")

inc = bmw_df.Close > bmw_df.Open
dec = bmw_df.Open > bmw_df.Close

plot.vbar(bmw_df.index[inc], time, bmw_df.Open[inc], bmw_df.Close[inc], fill_color="green", line_color="black")
plot.vbar(bmw_df.index[dec], time, bmw_df.Open[dec], bmw_df.Close[dec], fill_color="red", line_color="black")

output_file("BMW.html")
show(plot)
