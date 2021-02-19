from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm
from django.contrib import messages


# Create your views here.

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = "catalog/product/list_products.html"
    login_url = "/ecommerce/accounts/login"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = self.model.objects.filter(
                Q(name__icontains=query) | Q(sku=query), created_by=self.request.user
            )
        else:
            object_list = self.model.objects.filter(created_by=self.request.user)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product/view_product.html"

class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product/add_product.html"
    success_message = "Product was created successfully"
    error_message = "Error saving the Doc, check fields below."

    def get_success_url(self):
        return reverse("catalog:home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.slug = form.cleaned_data["name"].lower().replace(" ", "-")
        obj.save()
        return super(ProductCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    # specify the model you want to use
    model = Product
    form_class = ProductForm
    template_name = "catalog/product/update_product.html"
    success_message = "Product was updated successfully"
    error_message = "Error saving the Doc, check fields below."

    def get_success_url(self):
        return reverse("catalog:home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.slug = form.cleaned_data["name"].lower().replace(" ", "-")
        obj.save()
        return super(ProductUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    # specify the model you want to use
    model = Product
    template_name = "catalog/product/delete_product.html"
    success_message = "Product Deleted Successfully"

    def get_success_url(self):
        return reverse("catalog:home")
