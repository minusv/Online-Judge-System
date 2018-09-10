import os, uuid
from django.db import models
from django.core.validators import FileExtensionValidator


def random_ip_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('questions/input', filename)

def random_op_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('questions/output', filename)

class question(models.Model):
    quescode = models.CharField(max_length=100)
    timelimit = models.DecimalField(max_digits=5,decimal_places=2)
    ip_file = models.FileField(upload_to=random_ip_file_name, 
        validators=[FileExtensionValidator(allowed_extensions=['txt'],
        message="Please upload '.txt' files only.")], 
        null=True, blank=True)
    op_file = models.FileField(upload_to=random_op_file_name, 
        validators=[FileExtensionValidator(allowed_extensions=['txt'],
        message="Please upload '.txt' files only.")], 
        null=True, blank=True)
    
    def __str__(self):
        return self.quescode

