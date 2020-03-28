from django.shortcuts import render

from django.shortcuts import render,redirect

from .models import Notes, Category

def index(request):

    todos = Notes.objects.all()

    categories = Category.objects.all()

    if request.method == "POST":

        if "taskAdd" in request.POST:

            title = request.POST["description"]

            date = str(request.POST["date"])

            category = request.POST["category_select"]

#            tag = request.POST["tag"]

            content = title + " -- " + date + " " + category

            Todo = Notes(title=title, content=content, due_date=date, category=Category.objects.get(name=category))

            Todo.save()

            return redirect("/")

        if "taskDelete" in request.POST:

            checkedlist = request.POST["checkedbox"]

            for todo_id in checkedlist:

                todo = Notes.objects.get(id=int(todo_id))

                todo.delete()

    return render(request, "index.html",
                  {"todos": todos,
                   "categories":categories}
                  )