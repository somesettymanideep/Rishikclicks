from django.urls import path
from .views import Home,Services,Contact,RecentProjects
urlpatterns = [
    path('', Home , name='home'),
    path('Services/', Services , name='Services'),
    path('RecentProjects/', RecentProjects , name='RecentProjects'),
    path('Contact/', Contact , name='Contact'),
  
    ]