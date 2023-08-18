from . import views
from django.urls import path 

urlpatterns = [
    path("",views.home,name="home"),
    path("emp_all/",views.emp_all,name="emp_all"),
    path("add_emp/",views.add_emp,name="add_emp"),
    path("remove_emp/<int:ids>/",views.remove_emp,name="remove_emp"),
    path("filter_emp/",views.filter_emp,name="filter_emp"),
]


