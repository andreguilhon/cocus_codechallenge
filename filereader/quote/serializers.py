from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('line_number', 'line_content', 'most_common_character')