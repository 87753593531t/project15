from django.contrib import admin

from questionnaire.models import Questionnaire, Question, Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


class AnswerAdminInLine(admin.StackedInline):
    model = Answer
    extra = 0
    classes = ['collapse']


class QuestionAdminInLine(admin.StackedInline):
    model = Question
    extra = 0
    classes = ['collapse']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerAdminInLine
    ]


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [
        QuestionAdminInLine
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        return self.readonly_fields
