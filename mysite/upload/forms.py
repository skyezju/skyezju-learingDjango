__author__ = 'Skye'
from django import forms
import xlrd
import os
import time
import jpype
import os.path

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
            validateData(info_dic)
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


def validateData(info_dic):
    isDataValidated = 0;
    if(validateOwner(info_dic['ownerName'])):
        print("The owner is valid")
        isDataValidated = isDataValidated+1
    else:
        print("The owner is invalid")

    if(validateProject(info_dic['rallyProjectName'])):
        print("The project is valid")
        isDataValidated = isDataValidated+1
    else:
        print("The project is invalid")

    if(validateRelease(info_dic['releaseName'])):
        print("The Releaes is valid")
        isDataValidated = isDataValidated+1
    else:
        print("The Release is invalid")

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
    #call com.microstrategy.rally.tools.rallyobjects.RallyDefect.validationDefectByTQMSID with id
    #/Users/Skye/Documents/DevOps/djangoTry/mysite/upload
    jvmPath = jpype.getDefaultJVMPath()

    ext_classpath ="/Users/Skye/Documents/DevOps/djangoTry/mysite/upload/Rally.jar"
    #ext_classpath ="/Users/Skye/Documents/DevOps/djangoTry/mysite/upload/Rally/com/microstrategy/rally/tools"
    jvmArg = "-Djava.class.path=%s" % (ext_classpath)
    if not jpype.isJVMStarted():
        #jpype.startJVM(jvmPath, jvmArg)
        jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m",jvmArg)
    JDClass =  jpype.JClass("com.microstrategy.rally.tools.UploadTQMS2RallyFromDB")
    #JDClass =  jpype.JClass("UploadTQMS2RallyFromDB")
    jd = JDClass()
    jprint = jpype.java.lang.System.out.println
    jprint(jd.validateTQMSID(tqmsID))
    jpype.shutdownJVM()
    print(tqmsID)
    return True

def validateProject(rallyProjectName):
    #call com.microstrategy.rally.tools.rallyobjects.RallyProject.queryProjectByName
    print(rallyProjectName)
    return True

def validateOwner(ownerName):
    print(ownerName)
    return True

def validateRelease(releaseName):
    print(releaseName)
    return  True


