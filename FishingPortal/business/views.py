from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as view

from FishingPortal.business.forms import BusinessCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Business

UserModel = get_user_model()


# @login_required
# def business_create_view(request):
#     form = BusinessCreationForm(request.POST or None)
#
#     if form.is_valid:
#         form.save()
#         return redirect('show_business')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'business/create.html', context)


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessCreationForm
    template_name = 'business/create.html'  # Replace with your actual template path
    success_url = reverse_lazy('show_business')

    def form_valid(self, form):
        # Set the currently logged-in user as the owner of the business being created
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BusinessShowView(LoginRequiredMixin, view.DetailView):
    template_name = 'business/show.html'
    model = Business
    form_class = BusinessCreationForm
    context_object_name = 'business'



class DeleteBusinessView(LoginRequiredMixin, view.DeleteView):
    template_name = 'business/delete.html'
    context_object_name = 'business'
    success_url = 'home'

    def form_valid(self, form):
        messages.success(self.request, "The business was deleted successfully.")
        return super(DeleteBusinessView, self).form_valid(form)

# def delete_business(request, pk):
#     business = Business.objects.all().