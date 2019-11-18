from rest_framework import serializers
from jobhunter_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password','location_preference','skills','experience','resume')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            location_preference=validated_data['location_preference'],
            skills=validated_data['skills'],
            experience=validated_data['experience'],
            resume=validated_data['resume'],
        )

        return user


class OpeningsSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.Openings
        fields = ('id', 'title', 'created_on', 'expired_on','image','experience','skills','description','contact_mail','location','website','company','company_logo')
       
