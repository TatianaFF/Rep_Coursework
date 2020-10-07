from rest_framework import serializers
from HTApp2_0.models import Place, Comment


class PlaceListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PlaceDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Place
        fields = '__all__'


class CommentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'