from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()



'''
    model to store the messages from the server to db
'''
class Message(models.Model):
    author = models.ForeignKey(User, related_name = 'author_messages', on_delete = models.CASCADE)
    # deletes all the instance of message of the user if the user is deleted
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.author.username

    def last_10_msg(self):
        return Message.objects.order_by('-timestamp').all()[:10]