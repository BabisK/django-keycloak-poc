from rest_framework import serializers

from perm.models import Song


class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
