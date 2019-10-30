import uuid
from django.db import models

class Mission(models.Model):
    id = models.UUIDField(
        auto_created=True,
        default=uuid.uuid4,
        editable=False,
        null=False,
    )
    row_id = models.UUIDField(
        auto_created=True,
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        null=False,
        unique=True,
    )
    update_id = models.UUIDField(
        editable=False,
        null=True,
        unique=True,
    )
    writetime = models.DateTimeField(
        auto_now=True,
        null=False
    )
    is_deleted = models.BooleanField(
        default=False,
        editable=True,
        null=False,
    )

    def __str__(self):
        return (
            str(self.id) + " - " +
            str(self.row_id) + " - " +
            str(self.update_id) + " - " +
            str(self.writetime) + " - " +
            str(self.is_deleted)
        )

    @classmethod
    def create(cls, id=None, is_deleted=False):
        if id is not None:
            mission = cls(id=id, is_deleted=is_deleted)
            return mission
        else:
            mission = cls()
            return mission

    def save(self, *args, **kwargs):
        try:
            m_old = Mission.objects.get(
                id=self.id,
                update_id=None,
                is_deleted=False
                )
            m_new = Mission.create(self.id, self.is_deleted)
            super(Mission, m_new).save(*args, **kwargs)
            
            m_old.update_id = m_new.row_id
            super(Mission, m_old).save(*args, **kwargs)

            return m_new
        except Mission.DoesNotExist:
            super(Mission, self).save(*args, **kwargs)
            
            return self