from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [path('createrecipe',views.CustomCreateRecipeView.as_view(),name="createrecipe"),
               path('editrecipe/<int:id>',views.CustomEditRecipeView.as_view(),name="editrecipe"),
               path('deleterecipe/<int:id>',views.CustomDeleteRecipeView.as_view(),name='deleterecipe'),
               path('viewrecipe/<int:id>/',views.CustomViewRecipeView.as_view(),name="viewrecipe"),


]


