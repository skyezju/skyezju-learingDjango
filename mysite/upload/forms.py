__author__ = 'Skye'
from django import forms
import xlrd
import os
import time
import subprocess
import os.path
#define the jar path
jarPath = "/Users/Skye/Documents/DevOps/djangoTry/mysite/upload/"

class UploadFileForm(forms.Form):
    file = forms.FileField()
    file.label = "Upload file"
    TQMSID = "default"
    def readexcelFile(self):
        book = xlrd.open_workbook("./upload/uploadedfile/InputFile.xls")
        table = book.sheets()[0]
        nrows = table.nrows
        for i in range(1,nrows):
            row_value = table.row_values(i)
            info_dic = {'tqmsID': row_value[0],
                'rallyProjectName': row_value[2],
                'ownerName':row_value[1],
                'releaseName':row_value[3]}
            if validateData(info_dic):
                insertIssue(info_dic)
            else:
                print("The info of "+info_dic['tqmsID']+" is no valid")
        # rename the readed file with time name to backup it.
        os.rename("./upload/uploadedfile/InputFile.xls",
                  "./upload/uploadedfile/InputFile"+"_"+ time.strftime('%Y-%m-%d %X',time.localtime())+"_"+".xls")


class IssueForm(forms.Form):
    tqmsID = forms.CharField()
    tqmsID.label = "TQMS ID"
    rallyProjectName = forms.CharField()
    rallyProjectName.label = "Rally Project Name"
    ownerName = forms.CharField()
    ownerName.label = "Owner"
    releaseName = forms.CharField()
    releaseName.label = "Release"
    def validateDataAll(self):
        info_dic = {'tqmsID': self.cleaned_data['tqmsID'],
                'rallyProjectName': self.cleaned_data['rallyProjectName'],
                'ownerName':self.cleaned_data['ownerName'],
                'releaseName':self.cleaned_data['releaseName']}
        if validateData(info_dic):
            return True
        else:
            return False
    def insertIssue(self):
        info_dic = {'tqmsID': self.cleaned_data['tqmsID'],
                'rallyProjectName': self.cleaned_data['rallyProjectName'],
                'ownerName':self.cleaned_data['ownerName'],
                'releaseName':self.cleaned_data['releaseName']}
        if insertIssue(info_dic):
            return True
        return False


def validateData(info_dic):
    isDataValidated = 0;
    if(validateOwner(info_dic['ownerName'],info_dic['rallyProjectName'])):
        print("The owner is valid")
        isDataValidated = isDataValidated+1
    else:
        print("The owner is invalid")

    if(validateProject(info_dic['rallyProjectName'])):
        print("The project is valid")
        isDataValidated = isDataValidated+1
        if(validateRelease(info_dic['releaseName'],info_dic['rallyProjectName'])):
            print("The Releaes is valid")
            isDataValidated = isDataValidated+1
        else:
            print("The Release is invalid")
    else:
        print("The project is invalid")

    if(validateTQMSID(info_dic['tqmsID'])):
        print("The TQMS ID is valid")
        isDataValidated = isDataValidated+1
    else:
        print("The TQMS ID is invalid")

    if(isDataValidated == 4):
        return True
    else:
        return False

def validateTQMSID(tqmsID):
    javacmd = "java -jar "+jarPath+"rallytool.jar -id "+tqmsID+" -action validateID"
    print(javacmd)
    output = subprocess.check_output(javacmd,shell=True)
    print(output)

    if output.find("true") > 0:
        print("The issue "+tqmsID+" is invalid" )
        return False
    elif output.find("false") >0:
        print("The issue "+tqmsID+" is valid" )
        return True
    else:
        print("TQMS issue Validation is failed")
        return False

def validateProject(rallyProjectName):
    javacmd = "java -jar "+jarPath+"rallytool.jar -project "+rallyProjectName+" -action validateProject"
    print(javacmd)
    output = subprocess.check_output(javacmd,shell=True)
    print(output)

    if output.find("true") > 0:
        print("The project "+rallyProjectName+" is valid" )
        return True
    elif output.find("false") >0:
        print("The project "+rallyProjectName+" is invalid" )
        return False
    else:
        print("rallyProjectName Validation is failed")
        return False

def validateOwner(ownerName,rallyProjectName):
    javacmd = "java -jar "+jarPath+"rallytool.jar -project "+rallyProjectName+" -owner "+ownerName+" -action validateOwner"
    print(javacmd)
    output = subprocess.check_output(javacmd,shell=True)
    print(output)

    if output.find("true") > 0:
        print("The owner "+ownerName+" is valid" )
        return True
    elif output.find("false") >0:
        print("The owner "+ownerName+" is invalid" )
        return False
    else:
        print("ownerName Validation is failed")
        return False

def validateRelease(releaseName,rallyProjectName):
    javacmd = "java -jar "+jarPath+"rallytool.jar -project "+rallyProjectName+" -release "+releaseName+" -action validateRelease"
    print(javacmd)
    output = subprocess.check_output(javacmd,shell=True)
    print(output)

    if output.find("true") > 0:
        print("The release "+releaseName+" is valid" )
        return True
    elif output.find("false") >0:
        print("The release "+releaseName+" is invalid" )
        return False
    else:
        print("releaseName Validation is failed")
        return False


def insertIssue(info_dic):
        tqmsID = info_dic['tqmsID']
        rallyProjectName = info_dic['rallyProjectName']
        releaseName = info_dic['ownerName']
        ownerName = info_dic['releaseName']
        javacmd = "java -jar "+jarPath+"rallytool.jar " \
                                       "-id "+tqmsID+\
                                        "-project "+rallyProjectName+\
                                        " -release "+releaseName+\
                                        " -owner "+ownerName+\
                                        " -action insert"
        print(javacmd)
        output = subprocess.check_output(javacmd,shell=True)
        print(output)

        if output.find("true") > 0:
            print("Issue "+tqmsID+" is uploaded to rally successfully" )
            return True
        elif output.find("false") >0:
            print("Issue "+tqmsID+" uploading to rally is failed" )
            return False
        else:
            print("Issue "+tqmsID+" uploading to rally is failed" )
            return False
