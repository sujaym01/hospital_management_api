from rest_framework import serializers
from . import models


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Doctor
        fields = [
            "id",
            "user",
            "full_name",
            "image",
            "designation",
            "specialization",
            "available_time",
            "fee",
            "meet_link",
        ]

    def get_full_name(self, obj):
        """
        Retrieve the full name of the associated user.
        """
        return obj.user.get_full_name() if obj.user else None


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = "__all__"


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"
