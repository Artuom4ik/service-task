from rest_framework import serializers
from django.utils import timezone

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        extra_kwargs = {
            'name': {
                'required': True,
                'allow_blank': False,
                'max_length': 255
            },
            'description': {
                'required': True,
                'allow_blank': False,
                'max_length': 500
            },
            'status': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'close_at': {'read_only': True},
        }

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user if request and hasattr(request, 'user') else None

        if user and user.role == 'client':
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get(
                'description',
                instance.description
            )

        elif user and user.role == 'employee':
            instance.report = validated_data.get('report', instance.report)

            if instance.report:
                instance.status = 'completed'
                instance.closed_at = timezone.now()

        instance.updated_at = timezone.now()
        instance.save()

        return instance
