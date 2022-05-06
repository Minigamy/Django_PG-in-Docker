import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bewise_app.functions import checking_for_uniqueness
from bewise_app.models import Quiz


@csrf_exempt
def accept_request(request):
    if request.method == "POST":
        data = int(
            dict(request.POST)['question_num'][0]
        )  # type: int  # В data храним значение question_num
        last_entry = Quiz.objects.all().last()  # Сохраняем последнюю запись, если ее нет, то вернется объект None.
        question_request = requests.get('https://jservice.io/api/random', data={"count": data})  # Отправляем запрос

        # В переменной хранятся все данные из запроса в виде списка.
        list_question_request = question_request.json()  # type:list

        # Проходим по всем вопросам и проверяем их наличие в БД.
        for i in list_question_request:
            checking_for_uniqueness(i)

        # Если в БД есть записи, то возвращаем вопрос последней из них.
        # Если записей нет, то возвращается объект None.
        if last_entry is not None:
            return HttpResponse(last_entry.text)
        else:
            return HttpResponse(last_entry)
