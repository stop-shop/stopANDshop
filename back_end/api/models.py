from django.db import models
    
class Shop(models.Model):
    title = models.CharField(max_length=64)
    class Type(models.TextChoices):
        cars = '1', "cars"
        Electronics = '2', "Electronics"
        Games = '3', "Games"
        Fashion = '4', "Fashion"
        Furniture = '5', "Furniture"
        Real_Estate = '6', "Real Estate"
        Food = '7', "Food"
        Equipment = '8', "Equipment"
        Books = '9', "Books"
        pets = '10', "pets"
        Business = '11', "Business - Industrial"
        CraftsmenJobs = '12', " Craftsmen"
        Electrician = '13', "Electrician services"
        Travel = '14', "Travel - Tourism"
        Medical = '15', "Medical Services"
        Events = '16', "Events Services"
        Teaching = '17', "Teaching & Training"
        Others = '18', "Others"
    type = models.CharField(
        max_length=18,
        choices=Type.choices,
        default=Type.Others
    )
    # type = models.CharField(max_length=64)
    description= models.TextField()
    class Category(models.TextChoices):
        goods = '1', "goods"
        services = '2', "services"
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.goods 
    )
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    img = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title    