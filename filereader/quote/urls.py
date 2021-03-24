from django.urls.conf import re_path, path
from . import views


urlpatterns = [
    re_path(r'quotes/get_many/(?P<quantity>\d+)', views.QuoteList.as_view()),
    path('quotes/most_common_character/', views.MostCommonCharacter.as_view())
]