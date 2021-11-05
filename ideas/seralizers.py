from rest_framework import serializers

from ideas.models import Idea, Vote


class IdeaSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'youtube_url', 'status']


class VoteSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['idea', 'reason']
