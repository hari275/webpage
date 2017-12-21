from django.shortcuts import render , render_to_response
from django.http import HttpResponse
#from webapp.forms import upload
#from webapp.models import file
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import plot
from django.views.generic import TemplateView
from django.utils.datastructures import MultiValueDictKeyError
import os
import pandas as pd
def table():
   dfe= pd.ExcelFile('/home/hari275/clusterview/media/iris.xlsx')
   df=dfe.parse('Sheet1')
   df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]] = df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]].astype(str)
   df.index.name = "recid"
   #df.reset_index().to_json('/home/hari275/clusterview/kgit01/templates/include/sample-data-table2.json',orient='records')
   da=df.reset_index()
   da=da[['recid', 'Species','SepalLength','SepalWidth','PetalLength','PetalWidth']]
   json1=da.loc[da['Species'] == 'setosa'].to_json(orient='records')
   json2=da.loc[da['Species'] == 'versicolor'].to_json(orient='records')
   json3=da.loc[da['Species'] == 'virginica'].to_json(orient='records')
   return({'df':json1,'df2':json2,'df3':json3})


'''def upload1(request):


   if request.method == 'POST' and request.FILES['myfile']:
       try:
          myfile = request.FILES['myfile']
          fs = FileSystemStorage()
          if os.path.splitext(myfile.name)[1] == ".xlsx":
             filename = fs.save(myfile.name, myfile)
             uploaded_file_url = fs.url(filename)
             return render(request, 'success.html',{'content':['upload success']})

          else:
             return render(request,'success.html',{'content':['upload failed']})
       except MultiValueDictKeyError:
          return render(request, 'success.html',{'content':['upload failed']})





   return render(request,table(),'home.html')'''



def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
       try:
          myfile = request.FILES['myfile']
          fs = FileSystemStorage()
          if os.path.splitext(myfile.name)[1] == ".xlsx":
             filename = fs.save(myfile.name, myfile)
             uploaded_file_url = fs.url(filename)
             return render(request, 'success.html',{'content':['upload success']})

          else:
             return render(request,'success.html',{'content':['upload failed']})
       except MultiValueDictKeyError:
          return render(request, 'success.html',{'content':['upload failed']})

    return render (request,'home.html',table() )
   #return render(request, 'home.html')
def page1(request):
    return render(request, 'home.html')
def debug2(request):
    return render(request, 'home.html')
def json(request):
    return render(request, 'sample-data-table.json')






class Graph(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        #hm=home(request)
        dfe= pd.ExcelFile('/home/hari275/clusterview/media/iris.xlsx')
        df=dfe.parse('Sheet1')
        df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]] = df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]].astype(str)
        df.index.name = "recid"
        #df.reset_index().to_json('/home/hari275/clusterview/kgit01/templates/include/sample-data-table2.json',orient='records')
        da=df.reset_index()
        da=da[['recid', 'Species','SepalLength','SepalWidth','PetalLength','PetalWidth']]
        json1=da.loc[da['Species'] == 'setosa'].to_json(orient='records')
        json2=da.loc[da['Species'] == 'versicolor'].to_json(orient='records')
        json3=da.loc[da['Species'] == 'virginica'].to_json(orient='records')
        #return self.render(request,{'df':json1,'df2':json2,'df3':json3})
        context ={'df':json1,'df2':json2,'df3':json3,'graph':plot.sampleplot()}

        return context
class Graph2(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(Graph2, self).get_context_data(**kwargs)
        dfe= pd.ExcelFile('/home/hari275/clusterview/media/iris.xlsx')
        df=dfe.parse('Sheet1')
        df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]] = df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]].astype(str)
        df.index.name = "recid"
        #df.reset_index().to_json('/home/hari275/clusterview/kgit01/templates/include/sample-data-table2.json',orient='records')
        da=df.reset_index()
        da=da[['recid', 'Species','SepalLength','SepalWidth','PetalLength','PetalWidth']]
        json1=da.loc[da['Species'] == 'setosa'].to_json(orient='records')
        json2=da.loc[da['Species'] == 'versicolor'].to_json(orient='records')
        json3=da.loc[da['Species'] == 'virginica'].to_json(orient='records')
        context ={'graph':plot.histogramplot(),'df':json1,'df2':json2,'df3':json3}
        return context
class Graph3(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(Graph3, self).get_context_data(**kwargs)
        dfe= pd.ExcelFile('/home/hari275/clusterview/media/iris.xlsx')
        df=dfe.parse('Sheet1')
        df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]] = df[["SepalLength", "SepalWidth","PetalLength","PetalWidth"]].astype(str)
        df.index.name = "recid"
        #df.reset_index().to_json('/home/hari275/clusterview/kgit01/templates/include/sample-data-table2.json',orient='records')
        da=df.reset_index()
        da=da[['recid', 'Species','SepalLength','SepalWidth','PetalLength','PetalWidth']]
        json1=da.loc[da['Species'] == 'setosa'].to_json(orient='records')
        json2=da.loc[da['Species'] == 'versicolor'].to_json(orient='records')
        json3=da.loc[da['Species'] == 'virginica'].to_json(orient='records')
        context ={'graph':plot.subplot(),'df':json1,'df2':json2,'df3':json3}
        return context
        '''context['graph'] = div

        return context'''

# Create your views here.
