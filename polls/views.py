import os
from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    resultdata = os.listdir('/resultdata')
    return render(request, 'polls/index.html', {'resultdata': resultdata})


def to_paraviewweb(request, datestudy):
    glance_address = 'http://60.197.149.172:8080/glance/'
    data_address = 'http://60.197.149.172:8080/data/'
    filenames = ['dataset.vti', 'teeth_mesh.stl', 'maxilla_mesh.stl', 'mandibular_mesh.stl']
    redirect_url = glance_address + '?name=['

    for filename in filenames:
        redirect_url += filename + ','
    redirect_url = redirect_url[:-1] + ']&url=['

    for filename in filenames:
        redirect_url += data_address + datestudy + '/' + filename + ','
    redirect_url = redirect_url[:-1] + ']'

    return redirect(redirect_url)

