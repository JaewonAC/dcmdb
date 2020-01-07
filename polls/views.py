import os
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    resultdata = os.listdir('/resultdata')
    return render(request, 'polls/index.html', {'resultdata': resultdata})


def to_paraviewweb(request, datestudy):
    filenames = ['dataset.vti', 'teeth_mesh.stl', 'maxilla_mesh.stl', 'mandibular_mesh.stl']
    path = '/resultdata/' + datestudy + '/'
    files = []
    for filename in filenames:
        with open(path + filename, 'rb') as file:
            files.append(('files[]', (filename, file.read())))

    print('files are loaded.')
    return requests.get('http://jac-dt:4000/glance/', files=files)

