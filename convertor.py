import pandas as pd
import pdfkit
from alpha_vantage.timeseries import TimeSeries
key = 'XTP4AMN2N5H9BL51'
#pandas File

ts = TimeSeries(key,output_format='pandas')
data,meta  = ts.get_intraday('GOOGL',interval='1min') 

#location to wkhtmltopdf 

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
data.to_html("MyCSV.html")  
pdfkit.from_url("MyCSV.html", "FinalOutput.pdf",configuration=config)
