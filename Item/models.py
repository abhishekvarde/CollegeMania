from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Campus(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail_image = models.ImageField(upload_to='category/thumbnail', null=True, blank=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploader')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category_id = models.ForeignKey(ItemCategory, on_delete=models.DO_NOTHING, related_name='category_all_items')
    thumbnail_image = models.ImageField(upload_to='item/thumbnail', null=True, blank=True)
    price = models.FloatField()
    campus_id = models.ForeignKey(Campus, on_delete=models.DO_NOTHING, null=True, blank=True,
                                  related_name='campus_all_items')
    address = models.TextField()
    date_posted = models.DateField(auto_now_add=True, blank=True, null=True)
    contact_details = models.TextField()
    status_sold = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title + " by:" + str(self.user_id)


class ItemImage(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_images')
    image = models.ImageField(upload_to='item/image')

    def __str__(self):
        return self.item_id


class Conversation(models.Model):
    from_user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='from_user')
    to_user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='to_user')
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return " from:" + str(self.from_user_id) + " to:" + str(self.to_user_id) + " for item:" + str(self.item_id)


class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='conversation')
    message = models.TextField()

    def __str__(self):
        return self.conversation_id
