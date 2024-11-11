from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admin"
        ordering = ['-created_at']  # Untuk mengrutkan dari yang terbaru

    def __str__(self) -> str:
        return f"{self.username} ({self.email})"

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"
        ordering = ['name']  # Untuk mengurutkan berdasarkan nama

    def __str__(self) -> str:
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact_info = models.TextField()
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pemasok"
        verbose_name_plural = "Pemasok"
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name} - {self.contact_info}"

class Item(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=False)
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Barang"
        verbose_name_plural = "Barang"
        ordering = ['-created_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantity__gte=0),
                name='quantity_non_negative'
            ),
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name='price_non_negative'
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} - {self.quantity} unit(s) @ Rp{self.price}"