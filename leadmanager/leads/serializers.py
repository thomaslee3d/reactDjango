from rest_framework import serializers
from leads.models import Lead  

# Lead Serielizer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        models = Lead 
        fields = '__all__'