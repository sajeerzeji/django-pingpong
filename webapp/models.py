from django.db import models

class PingPong(models.Model):
    pong = models.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def __init__(self, pong):
    #     self.pong = pong
