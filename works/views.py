from django.shortcuts import reverse
from django.views.generic import FormView

from works.sender import send_message
from works.forms import AppealForm
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)


TOKEN = '5923286722:AAE_VLnyQiWstGS17Gdd7zmRYMe4fbDBbt8'
CHAT_ID = '-1001801986206'


class AppealView(FormView):
    template_name = 'index.html'
    form_class = AppealForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})

        return context

    def get(self, request, *args, **kwargs):
        data = request.GET
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('appeals')

    def form_valid(self, form):
        form.save()

        chat_id = CHAT_ID

        message = f"Новый отзыв от {form.instance.name}:\n" \
                f"Эл. почта: {form.instance.email}\n" \
                f"Сообщение: {form.instance.message}\n"
        send_message(message, chat_id)
        return super().form_valid(form)
