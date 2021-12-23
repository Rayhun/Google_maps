from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Image
from .forms import ImageForm


class ImageUpload(TemplateView):
    template_name = 'image_and_maps/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_image'] = Image.objects.all()
        context['form'] = ImageForm()
        return context
    
    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'all_image': Image.objects.all(),
                'form': form,
            }
            return render(request, 'image_and_maps/index.html',context)
        else:
            context = {
                'all_image': Image.objects.all(),
                'form': form,
            }
            return render(request, 'image_and_maps/index.html', context)
