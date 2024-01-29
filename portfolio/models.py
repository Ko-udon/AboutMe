from django.db import models

class PageView(models.Model):
    page_name = models.CharField(max_length=200)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.page_name

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('Web Project', '웹 개발'),
        ('Game Project', '게임 개발'),
        ('Data Project', '데이터'),
        # 필요한 카테고리를 추가하시면 됩니다.
    )

    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    git_url = models.URLField(null=True, blank=True)
    deploy_url = models.URLField(null=True, blank=True)
    tech_stack = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image1 = models.ImageField(upload_to='assets/projects/', default='')
    image2 = models.ImageField(upload_to='assets/projects/', default='')
    image3 = models.ImageField(upload_to='assets/projects/', default='')

    def __str__(self):
        return self.title