__author__ = 'Skye'
from django import forms
import xlrd

class UploadFileForm(forms.Form):
    file = forms.FileField()
    file.label = "Upload file"
    TQMSID = "default"
    def readexcelFile(self):
        book = xlrd.open_workbook("myfile.xls")


class IssueForm(forms.Form):
    tqmsID = forms.CharField()
    tqmsID.label = "TQMS ID"
    rallyProjectName = forms.CharField()
    rallyProjectName.label = "Rally Project Name"
    ownerName = forms.CharField()
    ownerName.label = "Owner"
    releaseName = forms.CharField()
    releaseName.label = "Release"

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

    def validateData(self):
        isDataValidated = 0;
        if(self.validateOwner()):
            print("The owner is valid")
            isDataValidated = isDataValidated+1
        else:
            print("The owner is invalid")

        if(self.validateProject()):
            print("The project is valid")
            isDataValidated = isDataValidated+1
        else:
            print("The project is invalid")

        if(self.validateRelease()):
            print("The Releaes is valid")
            isDataValidated = isDataValidated+1
        else:
            print("The Release is invalid")

        if(self.validateTQMSID()):
            print("The TQMS ID is valid")
            isDataValidated = isDataValidated+1
        else:
            print("The TQMS ID is invalid")

        if(isDataValidated == 4):
            return True
        else:
            return False

    def validateTQMSID(self):
        #call com.microstrategy.rally.tools.rallyobjects.RallyDefect.validationDefectByTQMSID with id
        print(self.cleaned_data['tqmsID'])
        return True

    def validateProject(self):
        #call com.microstrategy.rally.tools.rallyobjects.RallyProject.queryProjectByName
        print(self.cleaned_data['rallyProjectName'])
        return True

    def validateOwner(self):
        print(self.cleaned_data['ownerName'])
        return True

    def validateRelease(self):
        print(self.cleaned_data['releaseName'])
        return  True


