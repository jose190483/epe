from django.shortcuts import render

# Create your views here.
from .sub_views.login_page_view import login_page
from .sub_views.home_view import home_view
from .sub_views.registration_page_view import registration_page
from epe.epe_app.sub_views.parameter_view import parameter_add,parameter_delete,parameter_list,parameter_search