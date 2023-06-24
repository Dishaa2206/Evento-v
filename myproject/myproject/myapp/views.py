from django.http import JsonResponse
from .models import Word

def get_word(request):
    word = Word.objects.first()
    data = {'word': "TEST"}
    return JsonResponse(data)
