from django.db import models
from tinymce.models import HTMLField
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
TOOL = [
    ('Home', 'Home'),
    ('HEIC to JPG', 'HEIC to JPG'),
    ('PNG TO JPG', 'PNG TO JPG'),
    ('JPG TO PNG', 'JPG TO PNG'),
    ('MP4 to MP3', 'MP4 to MP3'),
    ('Video to MP3', 'Video to MP3'),
    ('Image to Word', 'Image to Word'),
    ('MP3 Convertor', 'MP3 Convertor'),
    ('Audio Convertor', 'Audio Convertor'),
    ('About Us', 'About Us'),
    ('Contact Us', 'Contact Us'),
]

from django.db import models
from django.utils.translation import gettext_lazy as _
class ToolPage(models.Model):
    tool = models.CharField(max_length=100, unique=True, choices=TOOL, null=True)
    custom_url = models.CharField(max_length=100, unique=True, null=True, blank=True)  # New field for custom URL

    def __str__(self):
        return self.tool

    def get_translation(self, language_code):
        return self.translations.filter(language=language_code).first()

class ToolPageTranslation(models.Model):
    tool_page = models.ForeignKey('ToolPage', related_name='translations', on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=10, choices=settings.LANGUAGES, null=True)
    short_desc = models.TextField(max_length=100, null=True)
    title = models.CharField(max_length=500, null=True)
    description = HTMLField()
    url=models.ForeignKey('common.Url', on_delete=models.SET_NULL, null=True)


    # Meta Tags
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)

    # Open Graph Tags
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.CharField(max_length=255, null=True, blank=True)
    og_image = models.URLField(null=True, blank=True)
    og_url = models.URLField(null=True, blank=True)
    og_type = models.CharField(max_length=50, null=True, blank=True, default='website')

    # Twitter Card Tags
    twitter_card = models.CharField(max_length=50, null=True, blank=True, default='summary')
    twitter_title = models.CharField(max_length=255, null=True, blank=True)
    twitter_description = models.CharField(max_length=255, null=True, blank=True)
    twitter_image = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = (('tool_page', 'language'),)

    def __str__(self):
        return f"{self.tool_page.tool} -- {self.title} ({self.language})"

