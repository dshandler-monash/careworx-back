from django.db import models

# Model to access service_list TABLE in serviceListDB Database
class serviceList(models.Model):
    # … fields …
    
    class Meta:
        managed = False