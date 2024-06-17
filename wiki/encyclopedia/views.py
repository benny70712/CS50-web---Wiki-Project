from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import util
from django import forms
from markdown2 import Markdown
from random import choice

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "title": "Home Page",
        "entries": util.list_entries(),
    })


def view(request, title):
    content = util.get_entry(title)
    if (content == None):
         return render(request, "encyclopedia/error.html", {
        "errorMsg": f"The entry {title} dosn't exist."
    })

    return render(request, "encyclopedia/view.html", {
        "title": title,
        "content": markdowner.convert(content)
    })


def search(request):
    if request.method == "POST":
   
        entry_search = request.POST["q"]
        entries = util.list_entries()

        content = util.get_entry(entry_search)
        if (content):
            return render(request, "encyclopedia/view.html", {
                "title": entry_search,
                "content": markdowner.convert(util.get_entry(entry_search)),
            })

        else:
            recommendations = []
            for entry in entries:
                if entry_search.lower() in entry.lower():
                    recommendations.append(entry)

            return render(request, "encyclopedia/search.html", {
                "title": "Recommendations",
                "recommendations": recommendations,
            })


    
def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        entries = util.list_entries()
        print(request.POST)
        title =request.POST['title']
        content = request.POST['content']

        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/error.html", {
                    "errorMsg": f"The entry {title} already exist."
                })

    
        util.save_entry(title, content)
        return render(request, "encyclopedia/view.html", {
            "title": title,
            "content": markdowner.convert(content),
        })


def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        print(util.get_entry(title))
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    

def save_edit(request):
     if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/view.html", {
            "title": title,
            "content": markdowner.convert(content),
        })
     


def random(request):
    random_entry = choice(util.list_entries())
    return render(request, "encyclopedia/view.html", {
        "title": random_entry,
        "content": markdowner.convert(util.get_entry(random_entry)),
    })








