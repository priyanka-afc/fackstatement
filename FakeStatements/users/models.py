from django.db import models
#from datetime import datetime
#from django.utils import timezone
import datetime

# Create your models here.

class UserRegisterModel(models.Model):
    id = models.AutoField(primary_key=True)
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    username =models.CharField(max_length=100)
    mobile =models.CharField(max_length=100)
    dob =models.DateField()
    gender =models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    status =models.CharField(max_length=100)

    def __str__(self):
        return self.id
    class Meta:
        db_table = "registrations"

class StatementsModels(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    statement = models.CharField(max_length=500)
    label = models.CharField(max_length=50)
    probscore = models.FloatField()
    logisticregression = models.CharField(max_length=50)
    naivebayes  = models.CharField(max_length=50)
    randomforrest   = models.CharField(max_length=50)
    svm = models.CharField(max_length=50)
    deepneural = models.CharField(max_length=50)
    lgbinary = models.CharField(max_length=50)
    naivebinary = models.CharField(max_length=50)
    rfbinary = models.CharField(max_length=50)
    svmbinary = models.CharField(max_length=50)
    deepneuralbinary = models.CharField(max_length=50)
    #cdate  = models.DateTimeField(auto_now_add=True, blank=True)
    cdate = models.DateField(default=datetime.date.today)

    def __str__self(self):
        return self.id
    class Meta:
        db_table = "statementresults"
