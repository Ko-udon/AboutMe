from django.db import models

class PageView(models.Model):
    page_name = models.CharField(max_length=200)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.page_name