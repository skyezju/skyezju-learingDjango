from django.db import models

# Create your models here.
class viewNavigation(models.Model):
    viewNavigation_text = models.CharField(max_length=200)
    viewID = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.viewNavigation_text



class Issue2Insert(models.Model):
    tqmsID = models.CharField(max_length=200,default="no issue yet")
    rallyProjectName = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    releaseName = models.CharField(max_length=200)

    def insert2TQMS(self):
        #call the jar "UploadTQMS2RallyFromDB" with this
        print(self.tqmsID)

    def validateTQMSID(self):
        #call com.microstrategy.rally.tools.rallyobjects.RallyDefect.validationDefectByTQMSID with id
        print(self.tqmsID)

    def validateProject(self):
        #call com.microstrategy.rally.tools.rallyobjects.RallyProject.queryProjectByName
        print(self.tqmsID)

class uploadfromfile(Issue2Insert):
    uploadfromfile_text = "Upload issue from xls files"

    def __unicode__(self):              # __unicode__ on Python 2
        return self.uploadfromfile_text

class uploadfromtext(Issue2Insert):
    uploadfromtext_text = "Upload issue from your type in words"

    def __unicode__(self):              # __unicode__ on Python 2
        return self.uploadfromtext_text