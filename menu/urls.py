from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index_list'),
    path("about-1/", views.AboutView.as_view(), name='about'),
    # path("carts/", views.CartView.as_view(), name='cart'),
    path("error404/", views.Error404View.as_view(), name='error'),
    path("careers/", views.CareersView.as_view(), name='careers'),
    path("components/lists/", views.ListsView.as_view(), name='list'),
    path("components/maps/", views.MapsView.as_view(), name='map'),
    path("product/", views.ProductsView.as_view(), name='products'),
    # path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    # path("products/", views.ProductListView.as_view(), name="product_list"),
    # path("products/<str:category_slug>/", views.ProductListView.as_view(), name="category_list"),
    # path("products/<str:category_slug>/<str:subcategory_slug>/",
    #      views.ProductListView.as_view(),
    #      name="subcategory_list"
    #      )
]
