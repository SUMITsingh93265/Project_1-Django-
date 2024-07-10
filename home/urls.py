from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("chocolate", views.chocolate, name='chocolate'),
    path("dry_fruit", views.dry_fruit, name='dry_fruit'),
    path("choco_chip", views.choco_chip, name='choco_chip'),
    path("family_icecream", views.family_icecream, name='family_icecream'),
    path("contact/", views.contact, name='contact'),
    path("feedbackcontact", views.feedback, name='feedback'),
    path("ice_recipes", views.ice_recipes, name='ice_recipes'),
    path("delete_ice/<id>/", views.delete_ice , name='delete_ice'),
    path("update_recipe/<id>/", views.update_recipe , name='update_recipe'),
]