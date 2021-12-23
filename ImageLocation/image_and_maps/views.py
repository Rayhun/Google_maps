from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Image


class ImageUpload(TemplateView):
    template_name = 'image_and_maps/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Image Upload'
        return context
    
    def post(self, request):
        image = request.FILES.get('image')
        print(image, "***")
        Image.objects.create(image=image)
        return render(request, self.template_name)
