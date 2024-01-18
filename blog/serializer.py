from rest_framework import serializers
from .models import *

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'