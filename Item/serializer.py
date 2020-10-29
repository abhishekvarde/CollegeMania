from rest_framework import serializers
from .models import *
# from .models import Profile
from drf_extra_fields.fields import Base64FileField, Base64ImageField
import PyPDF2
import io
import logging
import mimetypes


class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        return 'pdf'


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        exclude = ()


class ItemImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = ItemImage
        exclude = ()


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        exclude = ()


class ItemSerializer(serializers.ModelSerializer):
    item_images = ItemImageSerializer(many=True, read_only=True)
    category_all_items = ItemCategorySerializer(read_only=True)

    def to_representation(self, instance):
        data = super(ItemSerializer, self).to_representation(instance)
        data['category'] = ItemCategorySerializer(ItemCategory.objects.get(id=data['category_id'])).data
        # for d in data:
        print(data)
        return data

    class Meta:
        model = Item
        exclude = ()


class ItemCategoryWithItemSerializer(serializers.ModelSerializer):
    category_all_items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = ItemCategory
        exclude = ()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ()


class ConversationSerializer(serializers.ModelSerializer):
    conversation = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        exclude = ()


class UserSerializer(serializers.ModelSerializer):
    uploader = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = User
        # exclude = ()
        fields = ['username', 'first_name', 'last_name', 'email', 'uploader']
