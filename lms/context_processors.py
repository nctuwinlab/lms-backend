from django.conf import settings

def variables(request):
    print(settings.SETTINGS_MODULE)
    return settings.VARIABLES
