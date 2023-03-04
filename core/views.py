from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def core_page(request):
    return render(request, template_name="core/index.html", context={'title': 'Core Page', 'user': request.user})