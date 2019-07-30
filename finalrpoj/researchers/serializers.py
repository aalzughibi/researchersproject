from rest_framework import serializers
from .models import profileModel,aboutResearch
from django.contrib.auth.models import User
class aboutResearchSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    class Meta:
        model = aboutResearch
        fields = '__all__'

        # def save(self,**kwargs):
        #     kwargs['user']=self.fields['user'].get_default()
        #     return super().save(**kwargs)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profileModel
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')