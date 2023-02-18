from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.id}'


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=1024)
    project_number = models.CharField(max_length=1024)
    acquisition_date = models.DateTimeField(null=True, blank=True)
    number_3l_code = models.CharField(max_length=1024)
    project_deal_type_id = models.CharField(max_length=1024)
    project_group_id = models.CharField(max_length=1024)
    project_status_id = models.CharField(max_length=1024)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.id}'


class WTG(models.Model):
    WTG_number = models.CharField(max_length=1024)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    WTG_Type_id = models.CharField(max_length=1024)
    Region_id = models.CharField(max_length=1024)
    kW = models.CharField(max_length=1024)
    hub = models.CharField(max_length=1024)
    rotor = models.CharField(max_length=1024)
    altitude = models.CharField(max_length=1024)
    COD = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=1024)
    WGS_84_north = models.CharField(max_length=1024)
    WGS_84_east = models.CharField(max_length=1024)
    gauss_krueger_zone = models.CharField(max_length=1024)
    gauss_krueger_north = models.CharField(max_length=1024)
    gauss_krueger_east = models.CharField(max_length=1024)
    town_id = models.CharField(max_length=1024)

    def __str__(self):
        return self.WTG_number
