from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from test.models import FormApply
# Create your views here.

class SiteLogin(LoginView):
    template_name = 'login.html'

def gethome(request):
    return render(request, "content.html")
@login_required
def getAward(request):
    return render(request, "client/award.html")
def getApprove(request):
    return render(request, "admin/approve.html")


def updateForm(request,id):
    if request.user.is_superuser:
        FormApply.objects.filter(id=id).update(status=1)
        return redirect('approve')
