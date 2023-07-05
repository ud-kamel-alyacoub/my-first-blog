from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #define our model "it's an object" and class means "defining object" 
    # and "Post" is the name of the object started with upper case always 
    # models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # models.CharField – this is how you define text with a limited number of characters.
    # models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
    # models.DateTimeField – this is a date and time.
    # models.ForeignKey – this is a link to another model.

    def publish(self): #defining method called publish always start with lower case and _ in between
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #Methods often return something. 
        #There is an example of that in the __str__ method. 
        # In this scenario, when we call __str__() we will get a text (string) with a Post title.
        return self.title