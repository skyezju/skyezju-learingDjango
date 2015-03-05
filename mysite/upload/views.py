from django.views import generic
from upload.models import viewNavigation,uploadfromfile,uploadfromtext
from django.shortcuts import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from upload.forms import IssueForm, UploadFileForm



# Create your views here.
class IndexView(generic.ListView):
    template_name = 'upload/index.html'
    context_object_name = 'latest_view_list'
    def get_queryset(self):
        return viewNavigation.objects.order_by('-viewID')


def upload(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            if form.validateDataAll():
                #upload the data

                #clean the form
                return render_to_response('upload/upload.html', {'form': form},context_instance = RequestContext(request))
            else:
                return HttpResponseRedirect('result.html')
    else:
        form = IssueForm()
    return render_to_response('upload/upload.html', {'form': form},context_instance = RequestContext(request))


def handle_uploaded_file(f):
    f_path='./upload/uploadedfile/InputFile.xls'
    with open(f_path, 'wb+') as info:
        print f.name
        for chunk in f.chunks():
            info.write(chunk)
    return f

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            form.readexcelFile()
            return render_to_response('upload/file.html', {'form': form},context_instance = RequestContext(request))
    else:
        form = UploadFileForm()
    return render_to_response('upload/file.html', {'form': form},context_instance = RequestContext(request))