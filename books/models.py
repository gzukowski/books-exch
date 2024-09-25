from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/product/', null=True)
    external_image = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.title
    
class Exchange(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    
    requester = models.ForeignKey(User, related_name='exchange_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='exchange_received', on_delete=models.CASCADE)
    requester_book = models.ForeignKey(Book, related_name='requested_exchanges', on_delete=models.CASCADE)
    receiver_book = models.ForeignKey(Book, related_name='received_exchanges', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.requester.username} wants to exchange {self.requester_book.title} for {self.receiver_book.title}"