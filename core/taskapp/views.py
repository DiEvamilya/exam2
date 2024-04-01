from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Category, Tasks


def redirect_view(request):
    return redirect('/start')


def start_view(request):
    tasks = Tasks.objects.all()
    catigories = Category.objects.all()

    if request.method == 'POST':
        if "Add" in request.POST:
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + " -- " + date + " " + category
            Task = Tasks(title=title, content=content, end_date=date, category=Category.objects.get(name=category))
            Task.save()
            return redirect('/start')
        if "Delete" in request.POST:
            checkedlist = request.POST.getlist('checkbox')
            for i in range(len(checkedlist)):
                task = Tasks.objects.filter(id=int(checkedlist[i]))
                task.delete()
    return render(request, 'start.html', {'tasks': tasks, 'categories': catigories})

def category_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        if "Add" in request.POST:
            name = request.POST['name']
            category = Category(title=name)
            category.save()
            return redirect('/start')
        if "Delete" in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                try:
                    categ = Category.objects.filter(id=int(check[i]))
                    categ.delete()
                except BaseException:
                    return HttpResponse('<h1>Сначала удалите карточки с этими категориями</h1>')
    return render(request, 'category.html', {'categories': categories})