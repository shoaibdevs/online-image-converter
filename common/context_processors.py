from django.shortcuts import render
from .models import *
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your views here.

BUTTONS = [
    {
        'code': 'en',
        'login': _('Login'),
        'register': _('Register'),
        'pricing': _('Pricing'),
        'contact': _('Contact'),
        'home': _('Home'),
        'logout': _('Logout')
    },
    {
        'code': 'fr',
        'login': _('Connexion'),
        'register': _('S\'inscrire'),
        'pricing': _('Tarification'),
        'contact': _('Contact'),
        'home': _('Accueil'),
        'logout': _('Déconnexion')
    },
    {
        'code': 'es',
        'login': _('Iniciar sesión'),
        'register': _('Registrarse'),
        'pricing': _('Precios'),
        'contact': _('Contacto'),
        'home': _('Inicio'),
        'logout': _('Cerrar sesión')
    },
    {
        'code': 'de',
        'login': _('Anmeldung'),
        'register': _('Registrieren'),
        'pricing': _('Preisgestaltung'),
        'contact': _('Kontakt'),
        'home': _('Startseite'),
        'logout': _('Abmelden')
    },
    {
        'code': 'ja',
        'login': _('ログイン'),
        'register': _('登録'),
        'pricing': _('価格設定'),
        'contact': _('お問い合わせ'),
        'home': _('ホーム'),
        'logout': _('ログアウト')
    },
    {
        'code': 'pt',
        'login': _('Login'),
        'register': _('Registrar'),
        'pricing': _('Preços'),
        'contact': _('Contato'),
        'home': _('Início'),
        'logout': _('Sair')
    },
    {
        'code': 'nl',
        'login': _('Inloggen'),
        'register': _('Registreren'),
        'pricing': _('Prijzen'),
        'contact': _('Contact'),
        'home': _('Home'),
        'logout': _('Uitloggen')
    },
    {
        'code': 'it',
        'login': _('Accesso'),
        'register': _('Registrati'),
        'pricing': _('Prezzi'),
        'contact': _('Contatto'),
        'home': _('Home'),
        'logout': _('Esci')
    },
]



def get_header_footer(request):
    try:

        request_path = request.get_full_path()
        for lang_code, _ in settings.LANGUAGES:
            if request_path.startswith('/' + lang_code + '/'):
                lng = lang_code
                break
        else:
            lng = request.session['lng_code']
        buttons = [button for button in BUTTONS if button['code'] == lng][0]
        matching_buttons = [button for button in BUTTONS if button['code'] == lng]
        if matching_buttons:
            buttons = matching_buttons[0]
        else:
            buttons = None
        return {
            'headers': TranslationHeader.objects.filter(lng=lng),
            'footers': TranslationFooter.objects.filter(lng=lng),
            'common_urls': Url.objects.all(), 
            'check_user': request.user.is_authenticated,
            'lng_code': request.session.get('lng_code', 'en'),
            'languages_list' : [{'code': code, 'name': name} for code, name in settings.LANGUAGES],
            'selected_lng': lng,
            'button' : buttons
        }
    except:
        return {}