from .views import *
from .music_convertor import convert_mp4_mp3

@api_view(['POST'])
def convert(request):
    if request.method == 'POST':
        target_format = request.POST.get('format')
        uploaded_file = request.FILES.get('file')
        if target_format == 'mp3':
            res = convert_mp4_mp3(request, uploaded_file)
            return res
        else:
            if target_format == 'jpg':
                target_format = 'JPEG'
            image = Image.open(uploaded_file)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            output_buffer = io.BytesIO()
            image.save(output_buffer, format=target_format)
            response = HttpResponse(output_buffer.getvalue(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename="converted_image.jpeg"'
            return response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)