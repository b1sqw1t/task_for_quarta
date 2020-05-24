from rest_framework import serializers

from .models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    """
    Todo serializer
    """

    class Meta:
        model = TodoModel
        fields = ('id', 'todo', 'created', 'changed', 'expiry_date', 'status', 'completion_date', 'change')

    change = serializers.BooleanField(default=False, required=False, read_only=True)
