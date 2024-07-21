from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    STATUS=(
        ('0','Draft'),
        ('1','Publish'),
    )

    SECTION = (
        ('Popular','Popular'),
        ('Recommended','Recommended'),
        ('New_Arrival','New_Arrival'),
        ('Top_Seller','Top_Seller'),
        
    )

    featured_image = models.ImageField(upload_to='Images')
    Name = models.CharField(max_length=200)
    content = RichTextField()
    price = models.IntegerField()
    discouted_price = models.IntegerField()
    # category = models.ForeignKey(Category,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    status = models.CharField(choices=STATUS,max_length=100)
    section =models.CharField(choices =SECTION,max_length=200)

    def __str__(self):
        return self.Name
    


class Main_Category(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='media/main_category_img')

    def __str__(self):
        return self.Name
    
class Sub_Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='media/sub_category_img')
    product_name = models.CharField(max_length=100,default=None)
    price = models.IntegerField(default=None)
    discount_price = models.IntegerField(default=None)
    Description = models.CharField(max_length=300,null=True)
    product_information = RichTextField()

    def __str__(self):
        return  self.main_category.Name + ' ---- ' + self.Name 
    
# class Sub_Category(models.Model):
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     Name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.category.main_category.Name + '--' + self.category.Name + '--' + self.Name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/blog_img')
    content = RichTextField()
    date = models.DateField(auto_now_add = True)
    author = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title