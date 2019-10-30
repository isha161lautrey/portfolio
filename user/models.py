from django.db import models


class notice(models.Model):
    time = models.DateTimeField(auto_now=True)
    heading = models.TextField(max_length=1000, default="")
    content = models.TextField()
    notice_by = models.TextField(max_length=500, blank=True)
    is_important = models.BooleanField()
    
    def __str__(self):
        return self.content[:10] + ' - ' + self.notice_by

