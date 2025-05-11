from django.db import models
from django.conf import settings

# Create your models here.

TOOL = [
    ('JPG to PDF', 'JPG to PDF'),
    ('HEIC to JPG', 'HEIC to JPG'),
    ('Image to PDF', 'Image to PDF'),
    ('PNG TO JPG', 'PNG TO JPG'),
    ('MP3 Converter', 'MP3 Converter'),
    ('MP4 to MP3', 'MP4 to MP3'),
    ('Video to MP3', 'Video to MP3'),
    ('Image to Word', 'Image to Word')
]


class Header(models.Model):
    pass

class TranslationHeader(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    url = models.ForeignKey('Url', on_delete=models.SET_NULL, null=True, blank=True)
    lng = models.CharField(max_length=10, choices=settings.LANGUAGES, null=True)

    def __str__(self):
        return self.title
    
    def is_subheader(self):
        check = SubHeader.objects.filter(translation_header_id=self.id).exists()
        return check
    def get_subheader(self):
        check = SubHeader.objects.filter(translation_header_id=self.id)
        return check
        

class SubHeader(models.Model):

    translation_header = models.ForeignKey(TranslationHeader, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=100, null=True)
    url = models.ForeignKey('Url', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    



class Footer(models.Model):
    pass

class TranslationFooter(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    lng = models.CharField(max_length=10, choices=settings.LANGUAGES, null=True)

    def __str__(self):
        return self.title
    
    def is_subfooter(self):
        check = SubFooter.objects.filter(translation_footer_id=self.id).exists()
        return check
    def get_subfooter(self):
        check = SubFooter.objects.filter(translation_footer_id=self.id)
        return check
        

class SubFooter(models.Model):
    translation_footer = models.ForeignKey(TranslationFooter, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    url = models.ForeignKey('Url', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    
class Url(models.Model):
    url = models.CharField(max_length=100, help_text="Url", null=True)

    def __str__(self) -> str:
        return self.url
