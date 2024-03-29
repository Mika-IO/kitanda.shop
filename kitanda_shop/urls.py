from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect

app_name = "kitanda_shop"

handler404 = "core.views.handler404"
handler500 = "core.views.handler500"

urlpatterns = [
    path("", views.home, name="landing_page"),
    path("loja/<str:name>/", views.store, name="store"),
    path("product/<str:id>/", views.product, name="product"),
    path("cart/<str:name>/", views.cart, name="cart"),
    path("address/<str:name>/", views.address, name="address"),
    path("review/<str:name>/", views.review, name="review"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path(
        "dashboard/login/",
        lambda r: redirect(
            f"/login?{r.META['QUERY_STRING']}" if r.META["QUERY_STRING"] else "/login"
        ),
    ),
    path("dashboard/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
