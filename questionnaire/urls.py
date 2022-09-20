from django.urls import path, re_path
from rest_framework_nested.routers import DefaultRouter

from questionnaire.views import QuestionnaireViewSet, QuestionViewSet, AnswerVewSet


router = DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerVewSet)

urlpatterns = [
    path('questionnaire/', QuestionnaireViewSet.as_view()),
    re_path(r'^questionnaire/(?P<uuid>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$', QuestionnaireViewSet.as_view())
] + router.urls
