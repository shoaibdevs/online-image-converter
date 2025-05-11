from django.shortcuts import render, HttpResponse
from .models import *
from common.models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from PIL import Image
import io
import base64
from pillow_heif import register_heif_opener
from PIL import Image
from pillow_heif import register_heif_opener
from pydub import AudioSegment
import io


import json

# Create your views here.

register_heif_opener()
def tool(request, lng,  slug):
    page_data = get_object_or_404(ToolPageTranslation, url__url=lng+'/'+"tool"+'/'+slug)
    selected_tool = page_data.tool_page.tool
    if selected_tool == 'HEIC to JPG':
        file_format = '.heic'
        target_format = 'jpg'
    elif selected_tool == 'PNG TO JPG':
        file_format = '.png'
        target_format = 'jpg'
    elif selected_tool == 'JPG TO PNG':
        file_format = '.jpg'
        target_format = 'png'
    elif selected_tool == 'MP4 to MP3':
        file_format = '.mp4'
        target_format = 'mp3'
    elif selected_tool == 'Video to MP3':
        file_format = 'video/*'
        target_format = 'mp3'
    elif selected_tool == 'Image to Word':
        file_format = 'image/*, image/heic, image/heif'
        target_format = 'text'
    elif selected_tool == 'MP3 Convertor' or selected_tool == 'Audio Convertor':
        file_format = 'audio/*'
        target_format = 'mp3'
    else:
        file_format = '*'
        target_format = '*'
    context = {
        'page_data': page_data,
        'target_format': target_format,
        'file_format' : file_format,
        'meta_title': page_data.meta_title,
        'meta_description': page_data.meta_description,
        'meta_keywords': page_data.meta_keywords,
        'og_title': page_data.og_title,
        'og_description': page_data.og_description,
        'og_image': page_data.og_image,
        'twitter_title': page_data.twitter_title,
        'twitter_description': page_data.twitter_description,
        'twitter_image': page_data.twitter_image,
    }
    return render(request, 'tool.html', context)
# def tool(request, lng, tool, slug):
#     languages = ['en', 'de', 'es', 'fr', 'ja', 'pt', 'nl', 'it']
#     page_data = None
#     new_url = None
#     for language in languages:
#         try:
#             page_data = ToolPage.objects.get(**{'url__{}'.format(language): tool+'/'+slug})
#             break
#         except ToolPage.DoesNotExist:
#             pass
#     if page_data is None:
#         return JsonResponse({'error': 'Page not found'}, status=404)
#     else:
#         new_url = [
#             {
#                 'lng': 'en',
#                 'url': str(page_data.url.en)
#             },
#             {
#                 'lng': 'de',
#                 'url': str(page_data.url.de)
#             },
#             {
#                 'lng': 'es',
#                 'url': str(page_data.url.es)
#             },
#             {
#                 'lng': 'fr',
#                 'url': str(page_data.url.fr)
#             },
#             {
#                 'lng': 'ja',
#                 'url': str(page_data.url.ja)
#             },
#             {
#                 'lng': 'pt',
#                 'url': str(page_data.url.pt)
#             },
#             {
#                 'lng': 'nl',
#                 'url': str(page_data.url.nl)
#             },
#             {
#                 'lng': 'it',
#                 'url': str(page_data.url.it)
#             },
#         ]


#     context = {
#         'page_data': page_data,
#         'target_format': '',
#         'file_format' : '',
#         'new_url': json.dumps(new_url)
#     }
#     return render(request, 'tool.html', context)

# @api_view(['POST'])
# def convert(request):
#     if request.method == 'POST':
#         target_format = request.POST.get('format')
#         uploaded_file = request.FILES.get('file')
#         if target_format == 'mp3':
#             # res = convert_mp4_mp3(request, uploaded_file)
#             # return res
#             pass
#         else:
#             if target_format == 'jpg':
#                 target_format = 'JPEG'
#             image = Image.open(uploaded_file)
#             if image.mode != 'RGB':
#                 image = image.convert('RGB')
#             output_buffer = io.BytesIO()
#             image.save(output_buffer, format=target_format)
#             response = HttpResponse(output_buffer.getvalue(), content_type='image/jpeg')
#             response['Content-Disposition'] = 'attachment; filename="converted_image.jpeg"'
#             return response
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)

