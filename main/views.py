from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/product/list.html',
                  context={
                      'category': category,
                      'categories': categories,
                      'products': products
                  })