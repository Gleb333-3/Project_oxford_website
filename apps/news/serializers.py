from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import News, NewsImage

User = get_user_model()


class NewsCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = News
        fields = '__all__'
        # exclude = ['news_image_carousel']

    news_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        news_carousel = validated_data.pop('news_image_carousel')
        news = News.objects.create(**validated_data)
        images = []
        for image in news_carousel:
            images.append(NewsImage(news=news, image=image))
        NewsImage.objects.bulk_create(images)
        news.save()
        return news

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = NewsImageSerializer(
            instance.news_images.all(), many=True
        ).data
        return representation


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = 'image',