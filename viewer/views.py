from django.shortcuts import render, redirect
from .models import Manga, Page
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


def index(request):
    mangas = Manga.objects.all()
    return render(request, 'viewer/index.html', {'mangas': mangas})

def manga_detail(request, manga_id, page_number):
    manga = get_object_or_404(Manga, id=manga_id)
    page = get_object_or_404(Page, manga=manga, order=page_number)
    
    # Отправляем мангу и страницу в шаблон
    return render(request, 'viewer/manga_detail.html', {
        'manga': manga,
        'page': page,
    })
