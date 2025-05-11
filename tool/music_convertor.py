from .views import *

def convert_mp4_mp3(request ,video_file):
    video_data = video_file.read()
    audio = AudioSegment.from_file(io.BytesIO(video_data))
    mp3_data = io.BytesIO()
    audio.export(mp3_data, format="mp3")
    response = HttpResponse(mp3_data.getvalue(), content_type='audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename="output.mp3"'
    return response
