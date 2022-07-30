from django.db import models
import markdown


class BlogItem(models.Model):
    title = models.CharField(max_length=128, null=False)
    text = models.TextField(null=False)
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.text = markdown.markdown(self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

