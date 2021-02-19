from django.urls import reverse
from common.models import TimeStampedModel
from django.db import models
from django_resized import ResizedImageField
from django.conf import settings


class CategoryQueryset(models.QuerySet):
    def name(self, name):
        return self.filter(name=name)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQueryset(self.model, using=self._db)

    def published(self, name):
        return self.get_queryset().name(name)


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Unique value for product page URL, created from name.",
    )
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(
        "Meta Keywords",
        max_length=255,
        help_text="Comma-delimited set of SEO keywords for meta tag",
    )
    meta_description = models.CharField(
        "Meta Description", max_length=255, help_text="Content for description meta tag"
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    objects = models.Manager()  # The default manager.

    category_manager = CategoryManager()

    class Meta:
        db_table = "categories"
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category_detail", args=[str(self.slug)])


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text="Unique value for product page URL, created from name.",
    )
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True, db_index=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_one = models.ImageField(upload_to="images/")
    image_two = models.ImageField(blank=True, null=True, upload_to="images/")
    image_three = models.ImageField(blank=True, null=True, upload_to="images/")
    image_four = models.ImageField(blank=True, null=True, upload_to="images/")
    image_five = models.ImageField(blank=True, null=True, upload_to="images/")

    class Meta:
        db_table = "products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product_detail", args=[str(self.slug)])

    def get_add_to_cart_url(self):
        return reverse("cart:add_to_cart", args=[str(self.slug)])

    def get_remove_from_cart_url(self):
        return reverse("cart:remove_from_cart", args=[str(self.slug)])

    def get_categories(self):
        categories = []
        for category in self.categories.all():
            categories.append(category)
        return categories

    def get_thumbnail(self):
        product_image = ProductImage.objects.get(
            product=self.id, img_category="thumbnail"
        )
        thumbnail = product_image.image.url
        return thumbnail

    def get_images(self):
        product_image = ProductImage.objects.filter(
            product=self.id, img_category="other"
        )[:3]
        return product_image


class ProductImage(TimeStampedModel):
    category = [
        ("thumbnail", "thumbnail"),
        ("other", "other"),
    ]
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = ResizedImageField(size=[120, 120], quality=75)
    img_category = models.CharField(max_length=20, choices=category, default="other")

    def __str__(self):
        return "{} {}".format(self.product.name, self.img_category)

    class Meta:
        db_table = "product_images"
        ordering = ["-created_at"]
