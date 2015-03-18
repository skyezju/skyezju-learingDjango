from django.views import generic
from upload.models import viewNavigation,uploadfromfile,uploadfromtext
from django.shortcuts import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from upload.forms import IssueForm, UploadFileForm, IssueValidationForm


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'upload/index.html'
    context_object_name = 'latest_view_list'
    def get_queryset(self):
        return viewNavigation.objects.order_by('-viewID')


def upload(request):
    insertStatus = "No issue is uploaded"
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
                #upload the data
            if form.insertIssue():
                insertStatus = "Issue uploading is successful"
            else:
                 insertStatus = "Issue uploading is failed"
                #clean the form
            return render_to_response('upload/upload.html', {'form': form, 'Status': insertStatus},context_instance = RequestContext(request))
        else:
            return render_to_response('upload/upload.html', {'form': form, 'Status': insertStatus},context_instance = RequestContext(request))
    else:
        form = IssueForm()
    # form = IssueForm()
    return render_to_response('upload/upload.html', {'form': form, 'Status': insertStatus}, context_instance = RequestContext(request))


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

def validation(request):
    form = IssueForm(request.POST)
    print(form)
    validation_dic = form.validateDataAll()
    info_dic = form.toData()
    print validation_dic
    result = "<br>"
    if(validation_dic['tqmsID']):
        result = result + "TQMS Issue: (" + info_dic['tqmsID'] + ")  is validate"+ "<br>"
    else:
        result = result + "TQMS Issue: (" + info_dic['tqmsID'] + ") is invalidate"+ "<br>"

    if(validation_dic['rallyProjectName']):
        result = result + "Rally Project Name: (" + info_dic['rallyProjectName'] + ") is validate"+ "<br>"
    else:
        result = result + "Rally Project Name: (" + info_dic['rallyProjectName'] + ") is invalidate"+ "<br>"

    if(validation_dic['ownerName']):
        result = result + "Owner: (" + info_dic['ownerName'] + ") is validate"+ "<br>"
    else:
        result = result + "Owner: (" + info_dic['ownerName'] + ") is invalidate"+ "<br>"

    if(validation_dic['releaseName']):
        result = result + "Release: (" + info_dic['releaseName'] + ") is validate"+ "<br>"
    else:
        result = result + "Release: (" + info_dic['releaseName'] + ") is invalidate"+ "<br>"
    return HttpResponse(result)