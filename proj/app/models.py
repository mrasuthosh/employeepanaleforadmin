from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    first_name = models.CharField(max_length=250,blank=True,null=True)
    last_name = models.CharField(max_length=250,blank=True,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)    
    phome = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return '%s %s %s' %(self.first_name,self.last_name,self.phome)





