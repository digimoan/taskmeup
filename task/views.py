from django.shortcuts import render

# Create your views here.
from django.views import View


class home_view(View):
    template = 'home.html'

    def get(self, request):
        return render(request, self.template)