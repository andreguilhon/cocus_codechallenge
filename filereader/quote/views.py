from rest_framework import views
from .serializers import QuoteSerializer
from .models import Quote
from django.db.models import Count
from rest_framework.response import Response



from rest_framework import generics

class QuoteList(generics.ListAPIView):
    # queryset = Quote.objects.order_by('?')[:1]
    serializer_class = QuoteSerializer
    def get_queryset(self):
        quantity = int(self.kwargs['quantity'])
        queryset = Quote.objects.order_by('?')[:quantity]
        return queryset


class MostCommonCharacter(views.APIView):
    def get(self, request):
        most_common = Quote.objects.values("most_common_character").annotate(count=Count('most_common_character')).order_by("-count")[0]
        return Response({'most_common_character': most_common['most_common_character'], 'count': most_common['count']})
