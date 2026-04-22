from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm

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

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category,
                                              available=True).exclude(id=product.id)[:4]
    cart_product_form = CartAddProductForm()
    return render(request, 'main/product/detail.html', {'product': product,
                                                        'related_product': related_products,
                                                        'cart_product_form': cart_product_form})
