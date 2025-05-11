from django.shortcuts import render, redirect
from common.views import get_header_footer
# Create your views here.
from django.shortcuts import get_object_or_404

from django.template import RequestContext
from tool.models import *
from common.models import Url

def base_home(request):
    print("insidecase")
    lng = request.session.get('lng_code', 'en')
    print(lng)
    return redirect('/'+lng+'/')

# def home(request, lng=None):
#     # try:
#         tool_page = ToolPage.objects.get(tool='Home')
#         if lng is None:
#             lng = request.session.get('lng_code', 'en')
#         else:
#             request.session['lng_code'] = lng
#         print('hello')
#         context = {
#             'page_data': get_object_or_404(ToolPageTranslation, tool_page_id=tool_page.id, language=lng)
#         }
#         return render(request, 'home.html', context)
    # except:
    #     print(lng)
    #     return redirect('/en/')
def home(request, lng=None):
    tool_page = ToolPage.objects.get(tool='Home')

    if lng is None:
        lng = request.session.get('lng_code', 'en')
    else:
        request.session['lng_code'] = lng
    print('hello')
    context = {
        'page_data': get_object_or_404(ToolPageTranslation, tool_page_id=tool_page.id, language=lng)
    }
    return render(request, 'home.html', context)


def return_html_page(request, slug):
    return render(request, slug+'.html')


def dynamic_page(request, lng=None, custom_url=None):
    print("In dynamic_page view")
    print(f"Received lng={lng}, custom_url={custom_url}")

    # Ensure we have the correct custom_url format
    if not custom_url:
        return render(request, '404.html', {"error": "Invalid URL"})

    # Construct the full URL for fetching the translation
    full_url = f"{lng}/pages/{custom_url}"
    print(f"Constructed full URL: {full_url}")

    # Fetch the Url instance based on the full_url
    try:
        url_instance = get_object_or_404(Url, url=full_url)
        print(f"Found Url: {url_instance}")
    except Url.DoesNotExist:
        print(f"Url with url='{full_url}' not found")
        return render(request, '404.html', {"error": "Url not found"})

    # Fetch the ToolPageTranslation based on the Url instance and language
    try:
        page_data = get_object_or_404(ToolPageTranslation, url=url_instance, language=lng)
        print(f"Found ToolPageTranslation: {page_data}")
    except ToolPageTranslation.DoesNotExist:
        print(f"ToolPageTranslation with url='{url_instance}' and language={lng} not found")
        return render(request, '404.html', {"error": "ToolPageTranslation not found"})

    # Render the template with the fetched data
    context = {
        'page_data': page_data
    }
    return render(request, 'dynamic_page.html', context)
