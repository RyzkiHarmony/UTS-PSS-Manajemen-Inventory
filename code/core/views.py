from django.shortcuts import render, redirect
from django.db.models import Sum, Avg, F

from django.contrib import messages
from .models import Item, Category, Supplier
from .forms import ItemForm, CategoryForm, SupplierForm

def dashboard(request):
    # Ringkasan sistem
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
    
    # Statistik item
    stats = Item.objects.aggregate(
        total_stock=Sum('quantity'),
        total_value=Sum(F('price') * F('quantity')),  # Use F expressions here
        avg_price=Avg('price')
    )
    
    # Items dengan stok rendah (di bawah 5)
    low_stock_items = Item.objects.filter(quantity__lt=5)
    
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
            item.created_by = request.user  # Assuming user authentication is implemented
            item.save()
            messages.success(request, 'Item berhasil ditambahkan.')
            return redirect('item_list')
    else:
        form = ItemForm()
    
    return render(request, '../templates/item_form.html', {'form': form})

def category_list(request):
    categories = Category.objects.annotate(
        item_count=Count('item'),
        total_value=Sum('item__price' * 'item__quantity'),
        avg_price=Avg('item__price')
    )
    return render(request, '../templates/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            messages.success(request, 'Kategori berhasil ditambahkan.')
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, '../templates/category_form.html', {'form': form})

def supplier_list(request):
    suppliers = Supplier.objects.annotate(
        item_count=Count('item'),
        total_value=Sum('item__price' * 'item__quantity')
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
    return render(request, 'core/categories/items.html', {
        'category': category,
        'items': items
    })