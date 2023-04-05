"""
URL configuration for entreprise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.urls import path

from comptable.views import compte_general_view, compte_tiers_view, code_journal_view, journal_view

urlpatterns = [
    path('', lambda request: redirect('choix_journal')),

    # journal
    path('journal/ajouter', code_journal_view.create, name='create_code_journal'),
    path('journal/modifier/<int:id_object>', code_journal_view.update, name='update_code_journal'),
    path('journal/supprimer/<int:id_object>', code_journal_view.remove, name='remove_journal'),
    path('journal/lister', code_journal_view.read, name='list_code_journal'),

    # compte général
    path('compte_general/ajouter', compte_general_view.create, name='create_compte_general'),
    path('compte_general/modifier/<int:id_object>', compte_general_view.update, name='update_compte_general'),
    path('compte_general/supprimer/<int:id_object>', compte_general_view.remove, name='remove_compte_general'),
    path('compte_general/lister', compte_general_view.read, name='list_compte_general'),

    # compte tiers
    path('compte_tiers/ajouter', compte_tiers_view.create, name='create_compte_tiers'),
    path('compte_tiers/modifier/<int:id_object>', compte_tiers_view.update, name='update_compte_tiers'),
    path('compte_tiers/supprimer/<int:id_object>', compte_tiers_view.remove, name='remove_compte_tiers'),
    path('compte_tiers/lister', compte_tiers_view.read, name='list_compte_tiers'),
    path('compte_tiers/json/<int:compte_general_id>', compte_tiers_view.compte_tiers_ajax, name='compte_tiers_ajax'),

    # journal
    path('journal/choix', journal_view.choix_journal, name='choix_journal'),
    path('journal/ecriture/<int:id_journal>', journal_view.add_journal, name='add_journal'),

    # grand journal
    path('grand_livre/', journal_view.get_grand_livre, name='grand_livre'),

    path('balance/', journal_view.get_balance, name='balance'),

    path('journal/ecriture/view/<int:id_piece>', journal_view.view_ecriture, name='ecriture_journal'),
]