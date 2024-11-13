from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Avg, F, Count
from django.contrib import messages
from .models import Item, Category, Supplier,Admin
from .forms import ItemForm, CategoryForm, SupplierForm

def dashboard(request):
    total_items = Item.objects.count()
    total_stock_value = Item.objects.aggregate(
        total=Sum(F('price') * F('quantity'))
    )['total'] or 0
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()
    
    context = {
        'total_items': total_items,
        'total_stock_value': total_stock_value,
        'total_categories': total_categories,
        'total_suppliers': total_suppliers,
    }
    return render(request, '../templates/dashboard.html', context)

def item_list(request):
    items = Item.objects.all()
    stats = Item.objects.aggregate(
        total_stock=Sum('quantity'),
        total_value=Sum(F('price') * F('quantity')),
        avg_price=Avg('price')
    )
    low_stock_items = Item.objects.filter(quantity__lt=5)
    
    for item in items:
        item.total_value = item.price * item.quantity  # Menghitung total nilai stok
        
    context = {
        'items': items,
        'stats': stats,
        'low_stock_items': low_stock_items,
    }
    return render(request, '../templates/item_list.html', context)

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            try:
                admin = Admin.objects.get(username=request.user)
                item.created_by = admin
            except Admin.DoesNotExist:
                messages.error(request, 'Admin profile not found for this user.')
                return redirect('item_list')
            item.save()
            messages.success(request, 'Item berhasil ditambahkan.')
            return redirect('item_list')
    else:
        form = ItemForm()
    
    return render(request, '../templates/item_form.html', {'form': form})

def category_list(request):
    categories = Category.objects.annotate(
        item_count=Count('item'),
        total_value=Sum(F('item__price') * F('item__quantity')),
        avg_price=Avg('item__price')
    )
    return render(request, '../templates/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            try:
                admin = Admin.objects.get(username=request.user) 
                category.created_by = admin
            except Admin.DoesNotExist:
                messages.error(request, 'Admin profile not found for this user.')
                return redirect('category_list')
            category.save()
            messages.success(request, 'Kategori berhasil ditambahkan.')
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, '../templates/category_form.html', {'form': form})

def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)
    
    # Hitung total
    total_quantity = items.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_value = items.aggregate(
        total=Sum(F('quantity') * F('price'))
    )['total'] or 0
    
    # Hitung statistik kategori
    category.item_count = items.count()
    category.total_value = total_value
    category.avg_price = total_value / category.item_count if category.item_count > 0 else 0
    
    context = {
        'category': category,
        'items': items,
        'total_quantity': total_quantity,
        'total_value': total_value,
    }
    
    return render(request, 'core/templates/category_items.html', context)

def supplier_list(request):
    suppliers = Supplier.objects.annotate(
        item_count=Count('item'),
        total_value=Sum(F('item__price') * F('item__quantity'))
    )
    return render(request, '../templates/suppliers_list.html', {'suppliers': suppliers})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.created_by = request.user
            supplier.save()
            messages.success(request, 'Supplier berhasil ditambahkan.')
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    
    return render(request, '../templates/suppliers_form.html', {'form': form})

def category_items(request, category_id):
    category = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=category)
    return render(request, '../templates/category_items.html', {
        'category': category,
        'items': items
    })