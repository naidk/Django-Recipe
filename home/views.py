# from django.shortcuts import render,redirect
# from recipes.models import recipe
# from django.views.generic import TemplateView
#
# # Create your views here.
#
#
# class Home(TemplateView):
#     context = {}
#     template_name = 'home/home.html'
#
#     def get(self, request, *args, **kwargs):
#         user = request.user.id
#         if user:
#             return redirect('userhome')
#         data = recipe.objects.all()
#         self.context['data'] = data
#         return render(request,self.template_name , self.context)

from django.shortcuts import render, redirect
from recipes.models import recipe
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = recipe.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('userhome')
        return super().get(request, *args, **kwargs)
