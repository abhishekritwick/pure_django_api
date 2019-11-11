from rest_framework import serializers
from status.models import Status


class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


# data = {'content':'Please delete me', 'email':'hello@teamcfe.com'}
# create_obj_serializer = CustomSerializer(data=data)
# if create_obj_serializer.is_valid():
#     valid_data = create_obj_serializer.data
#     print(valid_data)



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    #Field level validation
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError('Content is too long.')
    #     return value

    # Serializer level validation, validation of entire data
    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or Image is required.')
        return data
