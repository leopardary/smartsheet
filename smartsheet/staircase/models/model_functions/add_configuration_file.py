from django.utils import timezone


def add_configuration_file(instance,filename):
    #define the location of the file to upload to for Chamber
    return f'{instance.chamberName}/{timezone.now().strftime("%Y-%m-%d")}/{filename}'