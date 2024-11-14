from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class Users(AbstractBaseUser):
    user_id = models.CharField(max_length = 50, unique = True)
    password = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    money = models.BigIntegerField(default = 100000)
    attack = models.BigIntegerField(default = 10)
    defense = models.BigIntegerField(default = 5)
    health = models.BigIntegerField(default = 100)

    USERNAME_FIELD = 'user_id'



class Posts(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE, related_name = 'posts')
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.CharField(max_length = 50, default = "")



class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE, related_name = 'messages')
    recipient = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    content = models.TextField()



class Inventory_Equipment(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    category = models.CharField(max_length = 50) # 아이템 분류
    item_name = models.CharField(max_length = 50) # 아이템 이름
    item_level = models.IntegerField(default = 1) # 아이템 레벨
    item_attack = models.BigIntegerField(blank = True, null = True) # 아이템 공격력
    item_defense = models.BigIntegerField(blank = True, null = True) # 아이템 방어력
    item_health = models.BigIntegerField(blank = True, null = True) # 아이템 체력
    value = models.BigIntegerField(default = 100) # 아이템 가치
    upgrade_cost = models.IntegerField(default = 1000) # 강화 비용
    probability = models.IntegerField(default = 90) # 강화 확률
    image = models.ImageField(blank = True, null = True) # 아이템 이미지
    equip = models.BooleanField(default = False) # 장착여부
    upgrade_select = models.BooleanField(default = False) # 강화 할 아이템 선택 여부
    protected = models.BooleanField(default = False) # 보호 물약 적용 여부



class Inventory_Consumable(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 50)



class Mushrooms(models.Model):
    level = models.IntegerField(blank = True, null = True)
    name = models.CharField(max_length = 50, blank = True, null = True)
    health = models.BigIntegerField(blank = True, null = True)



class Dealer(models.Model):
    name = models.CharField(max_length = 50, blank = True, null = True)
    turns = models.IntegerField(default = 0)



class Card_Pool(models.Model):
    number = models.IntegerField()
    cards_dealt = models.BooleanField(default = False)



class Drawn_Card(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete = models.CASCADE, null = True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE, null = True)
    number = models.IntegerField()