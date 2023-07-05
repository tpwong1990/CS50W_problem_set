from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from . import util
import markdown2
from random import randint

class SearchForm(forms.Form):
    q = forms.CharField(label='q', max_length=100)

class CreateEntry(forms.Form):
    title = forms.CharField(label = 'title', max_length=100)
    entry_input = forms.CharField(label = 'entry_input', min_length=1)

class EditEntry(forms.Form):
    entry_input = forms.CharField(label = 'entry_input', min_length=1)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def visit_entry(request, entry):
    # get entry content
    error = 0
    content = util.get_entry(entry)
    if content == None:
        error = 1
        return render(request, "encyclopedia/view_entry.html", {
            "error": error
    })

    return render(request, "encyclopedia/view_entry.html", {
        "error": error,
        "entry": entry,
        "content": markdown2.markdown(content)
    })

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_entry = form.cleaned_data['q']

            # search the entry list
            submatch_entries=[]
            for entry in util.list_entries():
                if entry.lower() == search_entry.lower(): 
                    return redirect(visit_entry, entry=search_entry)
                elif entry.lower().find(search_entry.lower()) != -1:
                    submatch_entries.append(entry)

            return render(request, "encyclopedia/search_result.html", {
                "entries": submatch_entries
                })


def create(request):
    if request.method == "GET":
        error = 0
        return render(request, "encyclopedia/create.html", {
            "error": error
        })
    if request.method == "POST":
        form = CreateEntry(request.POST)
        error = 0
        if form.is_valid():
            # check if the input title exist or not
            for entry in util.list_entries():
                if form.cleaned_data['title'].lower() == entry.lower():
                    error = 1
                    return render(request, "encyclopedia/create.html", {
                        "error": error 
                    })
            # save entry to disk
            util.save_entry(form.cleaned_data['title'], form.cleaned_data['entry_input'])

            return redirect(visit_entry, entry=form.cleaned_data['title'])
        else:
            error = 2
            return render(request, "encyclopedia/create.html", {
                "error": error 
            })

def edit(request, entry):
    if request.method == "GET":
        error = 0
        return render(request, "encyclopedia/edit.html", {
            "entry": entry,
            "content": util.get_entry(entry),
            "error": error
        })
    if request.method == "POST":
        form = EditEntry(request.POST)
        if form.is_valid():
            content = form.cleaned_data['entry_input']
            util.save_entry(entry, form.cleaned_data['entry_input'])
            return redirect(visit_entry, entry=entry)
        else:
            error = 1
            return render(request, "encyclopedia/edit.html", {
                "error": error 
            })

def random(request):
    entry_list = util.list_entries()
    list_l = len(entry_list)
    entry = entry_list[randint(0,list_l-1)]
    return redirect(visit_entry, entry=entry)
