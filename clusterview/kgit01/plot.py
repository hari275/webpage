import plotly.offline as py
import plotly.graph_objs as go
#import ipywidgets as widgets
import io
import requests
import time
import plotly.figure_factory as FF
import pandas as pd
from plotly import tools
from plotly import tools
from datetime import date
import io
import requests
#da=pd.read_excel('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/media/iris.xlsx')
'''dfe= pd.ExcelFile('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/media/iris.xlsx')
df=dfe.parse('Sheet1')
df.to_html('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/webapp/templates/webapp/include/sample-data-table.html')'''


#py.offline.init_notebook_mode(connected=True)
def sampleplot():
    startdate = (1, 1, 2005)
    startdate = str(startdate[0]) + '+' + str(startdate[1]) + '+' + str(startdate[2])
    enddate = time.strftime("%m+%d+%Y")
    stock_url = "http://www.google.com/finance/historical?q=" + 'AAPL' + \
                "&startdate=" + startdate + "&enddate=" + enddate + "&output=csv"
    raw_response = requests.get(stock_url).content
    stock_data = pd.read_csv(io.StringIO(raw_response.decode('utf-8')))
    sample_data_table = FF.create_table(stock_data)
    #py.plot(sample_data_table)
    trace_high = go.Scatter(x=stock_data.Date,
                        y=stock_data.High,
                        name='High',
                        line=dict(color='#33CFA5'))
    trace_high_avg = go.Scatter(x=stock_data.Date,
                            y=[stock_data.High.mean()]*len(stock_data.Date),
                            name='High Average',
                            visible=False,
                            line=dict(color='#33CFA5', dash='dash'))
    trace_low = go.Scatter(x=stock_data.Date,
                       y=stock_data.Low,
                       name='Low',
                       line=dict(color='#F06A6A'))
    trace_low_avg = go.Scatter(x=stock_data.Date,
                           y=[stock_data.Low.mean()]*len(stock_data.Date),
                           name='Low Average',
                           visible=False,
                           line=dict(color='#F06A6A', dash='dash'))
    #data=[trace_high, trace_high_avg, trace_low, trace_low_avg ]
    high_annotations=[dict(x=enddate,
                       y=stock_data.High.mean(),
                       xref='x', yref='y',
                       text='High Average:<br>'+str(stock_data.High.mean()),
                       ax=0, ay=-40),
                  dict(x=stock_data.High.idxmax(),
                       y=stock_data.High.max(),
                       xref='x', yref='y',
                       text='High Max:<br>'+str(stock_data.High.max()),
                       ax=0, ay=-40)]
    low_annotations=[dict(x=startdate,
                      y=stock_data.Low.mean(),
                      xref='x', yref='y',
                      text='Low Average:<br>'+str(stock_data.Low.mean()),
                      ax=0, ay=40),
                 dict(x=stock_data.High.idxmin(),
                      y=stock_data.Low.min(),
                      xref='x', yref='y',
                      text='Low Min:<br>'+str(stock_data.Low.min()),
                      ax=0, ay=40)]



    layout = dict(

    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        #type='date'
    ),
    updatemenus = list([
    dict(active=-1,
         buttons=list([
            dict(label = 'High',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': 'apple High',
                          'annotations': high_annotations}]),
            dict(label = 'Low',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                         {'title': 'apple Low',
                          'annotations': low_annotations}]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True, True, True, True]},
                         {'title': 'apple',
                          'annotations': high_annotations+low_annotations}]),
            dict(label = 'Reset',
                 method = 'update',
                 args = [{'visible': [True, False, True, False]},
                         {'title': 'apple',
                          'annotations': []}])
        ]),
    )
])


)



    '''layout = dict(title='apple', showlegend=True,
              updatemenus=updatemenus,layout=layout)'''

    fig = dict(data=[trace_high, trace_high_avg, trace_low, trace_low_avg], layout=layout)
    plot=py.plot(fig,auto_open=False, output_type='div')
    return plot



def histogramplot():
   da=pd.read_json('/home/hari275/clusterview/kgit01/templates/include/sample-data-table2.json')
   da[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]] = da[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]].astype(float)
   sample_data_table = FF.create_table(da.head())
   #table=py.plot(sample_data_table, filename='C:/Users/krish/Anaconda3/Scripts/kgit/mysite/webapp/templates/webapp/include/sample-data-table',auto_open=False)
   trace1=go.Histogram(x=da['SepalWidth'], y=da['SepalLength'],name='x sepalwidth')
   trace2=go.Histogram(x=da['PetalLength'],name='x petallength')
   trace3=go.Histogram(x=da['SepalWidth'],name='x petalwidth' )
   layout = go.Layout(title='Simple Plot from excel data',yaxis=dict( title='SepalLenght'),xaxis=dict( title='all other properties'),
   plot_bgcolor='rgb(230, 230,230)')
   fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
   plot=py.plot(fig,auto_open=False, output_type='div' )
   return plot
def subplot():
   '''dfe= pd.ExcelFile('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/media/iris.xlsx')
   df=dfe.parse('Sheet1')
   df.to_html('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/webapp/templates/webapp/include/sample-data-table.html')
   da=pd.read_html('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/webapp/templates/webapp/include/sample-data-table.html')[0]'''
   da=pd.read_json('/home/hari275/clusterview/kgit01/templates/include/sample-data-table2.json')
   sample_data_table = FF.create_table(da.head())
   '''da=pd.read_excel('C:/Users/krish/Anaconda3/Scripts/kgit/mysite/media/iris.xlsx')
   sample_data_table = FF.create_table(da.head())
   py.plot(sample_data_table, filename='C:/Users/krish/Anaconda3/Scripts/kgit/mysite/webapp/templates/webapp/include/sample-data-table',auto_open=False)'''
   trace1=go.Histogram(x=da['SepalWidth'], y=da['SepalLength'],name='x sepalwidth')
   trace2=go.Histogram(x=da['PetalLength'], y=da['SepalLength'],name='x petallength')
   trace3=go.Histogram(x=da['PetalWidth'], y=da['SepalLength'],name='x petalwidth' )
   fig=tools.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2},None]],subplot_titles=('Sepal.Length vs Sepal.Width', 'Sepal.Length vs petal.Width',
                                                          'Sepal.Length vs petal.Width'))
   fig.append_trace(trace1, 1, 1)
   fig.append_trace(trace2, 1, 2)
   fig.append_trace(trace3, 2, 1)
   fig['layout'].update(height=600, width=600, title='Multiple Subplots' +
                                                  ' with Titles')
   plot1=py.plot(fig,auto_open=False, output_type='div' )
   return plot1
   '''layout = go.Layout(title='Simple Plot from excel data',yaxis=dict( title='Sepal.Lenght'),xaxis=dict( title='all other properties'),
   plot_bgcolor='rgb(230, 230,230)')
   fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
   plot=py.plot(fig,auto_open=False, output_type='div' )
   return plot  '''
