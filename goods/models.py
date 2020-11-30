from django.db import models
from user.models import UserInfo

class GoodsInfoManager(models.Manager):
    def get_books(self):
        return super(GoodsInfoManager, self).get_queryset().filter(type='books',isDelete=False)
    def get_digital(self):
        return super(GoodsInfoManager, self).get_queryset().filter(type='digital',isDelete=False)
    def get_cloth(self):
        return super(GoodsInfoManager, self).get_queryset().filter(type='cloth',isDelete=False)
    def get_daily(self):
        return super(GoodsInfoManager, self).get_queryset().filter(type='daily',isDelete=False)
    def get_traffic(self):
        return super(GoodsInfoManager, self).get_queryset().filter(type='traffic',isDelete=False)
    def get_other(self):
        return super(GoodsInfoManager, self).get_queryset().filter(type='other',isDelete=False)
    def get_title(self, title):
        return super(GoodsInfoManager, self).get_queryset().filter(title=title,isDelete=False)
    def create_good(self, title, type, picture, price, address, description, user):
        book = self.create(title=title, type=type, picture=picture, price=price, address=address, description=description,user=user, isDelete=False)
        return book


# Create your models here.
class GoodsInfo(models.Model):
    title = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='goods')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    address = models.CharField(max_length=100, default='', blank=True)
    description = models.CharField(max_length=300, default='', blank=True)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods = GoodsInfoManager()

    def __str__(self):
        return self.title