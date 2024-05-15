from django.db import models

# Create your models here.

def user_directory_path(instance, filename):

    return '{0}/{1}'.format("recipies_photos",filename)


class recipies_data(models.Model):
    recipie_id = models.AutoField(primary_key=True)
    recipie_name = models.CharField(max_length=100, blank=False, null=False )
    recipie_description = models.CharField(max_length=400, blank=False, null=False)
    recipie_duration = models.IntegerField(blank=False, null=False)
    recipie_ingredients = models.CharField(max_length=800, blank=False, null=False )
    recipie_steps = models.TextField( blank=False, null=False)
    recipie_photo = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")

    class Meta:
        db_table = 'recipies' 

class comments(models.Model):

    recipie_id_fk = models.ForeignKey(recipies_data, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=False, null=False )
    comment = models.CharField(max_length=400, blank=False, null=False)
    rating = models.IntegerField()
   