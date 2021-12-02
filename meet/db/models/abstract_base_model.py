import uuid as uuid
from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
        self.is_deleted = True
        self.save()
