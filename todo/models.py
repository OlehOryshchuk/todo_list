from django.db import models


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100
    )


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(
        help_text="Enter the deadline for this task.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.name
