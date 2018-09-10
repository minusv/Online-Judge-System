import os, uuid
from django.db import models
from judge.models import question
from django.core.validators import FileExtensionValidator

def random_source_code_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('submission/source_code', filename)

def random_op_file_name():
    ext = "txt"
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('submission/output', filename)

def random_error_file_name():
    ext = "txt"
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('submission/error', filename)

class status(models.Model):
    quesid=models.ForeignKey(question, on_delete=models.CASCADE)
    username=models.CharField(max_length=100, default=" ")
    language=models.IntegerField(null=True, blank=True)
    submissiontime=models.DateTimeField(auto_now=True)
    time=models.DecimalField(max_digits=5,decimal_places=2)
    result=models.CharField(max_length=10, default=" ")
    source_code=models.FileField(upload_to=random_source_code_name, 
        validators=[FileExtensionValidator(allowed_extensions=['py'],
        message="Please upload '.py' files only.")], 
        null=True, blank=True)
    op_file=models.FileField(default=random_op_file_name())
    error_file=models.FileField(default=random_error_file_name())
    
    def __str__(self):
        return str(self.quesid)