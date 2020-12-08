from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from auctions.forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/")
            # return HttpResponseRedirect(reverse('auctions'))
        else:
            for msg in form.error_messages:
                # print(form.error_messages[msg])
                error_message = form.error_messages[msg]

            return render(request = request,
                          template_name = "registration/register.html",
                          context={
                              "form": form,
                              "error_message": error_message,
                          })

    form = CustomUserCreationForm
    return render(request = request,
                  template_name = "registration/register.html",
                  context={"form":form})
