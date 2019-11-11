from django.core.serializers import serialize
from django.conf import settings
from django.db import models
import json

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename = filename)

# Create your models here.
class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     # print("Type of object is ",type(qs))
    #     return serialize('json', qs, fields = ('id','user','content', 'image'))
    def serialize(self):
        list_values = list(self.values('id','user','content', 'image'))
        # print("Type of object is ",type(qs))
        return json.dumps(list_values)

class UpdateManager(models.Manager):
    def get_queryset(self):
        # print("The model is ",self.model.content)
        return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    # def serialize(self):
    #     return serialize("json", [self,], fields=('id','user','content','image'))
    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            "id" : self.id,
            "content" : self.content,
            "user" : self.user.id,
            "image" : image
        }
        json_data = json.dumps(data)
        return json.loads(json.dumps(json_data))
