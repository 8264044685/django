from django.shortcuts import render
from django.views import View


# Create your views here.
# class welcome_view(View):
#     def get(self,request):
#         return render(request,'pages/welcome.html')
# class My_index_view(View):
#     def get(self, request):
#         return  render(request,'pages/index.html')
def index(request):
    return  render(request,'pages/index.html')



