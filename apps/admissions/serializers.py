from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    AdmissionsPage,
    AdmissionsImage,
    AdmissionsInfo,
    AdmissionsInfoImage,
)

User = get_user_model()


class AdmissionsCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = AdmissionsPage
        fields = '__all__'

    admissions_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        admissions_carousel = validated_data.pop('admissions_image_carousel')
        admissions_page = AdmissionsPage.objects.create(**validated_data)
        images = []
        for image in admissions_carousel:
            images.append(AdmissionsImage(page=admissions_page, image=image))
        AdmissionsImage.objects.bulk_create(images)
        admissions_page.save()
        return admissions_page

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs


class AdmissionsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AdmissionsImageSerializer(
            instance.admissions_images.all(), many=True
        ).data
        representation['admissions_info'] = AdmissionsInfoSerializer(
            instance.admissions_info.all(), many=True
        ).data
        return representation


class AdmissionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsPage
        fields = '__all__'


class AdmissionsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsImage
        fields = 'image',


class AdmissionsInfoCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = AdmissionsInfo
        fields = '__all__'

    admissions_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        admissions_info_carousel = validated_data.pop('admissions_info_image_carousel')
        admissions_info = AdmissionsInfo.objects.create(**validated_data)
        images = []
        for image in admissions_info_carousel:
            images.append(AdmissionsInfoImage(info=admissions_info, image=image))
        AdmissionsInfoImage.objects.bulk_create(images)
        admissions_info.save()
        return admissions_info

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs


class AdmissionsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AdmissionsInfoImageSerializer(
            instance.admissions_info_images.all(), many=True
        ).data
        return representation


class AdmissionsInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfo
        fields = '__all__'


class AdmissionsInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfoImage
        fields = 'image',