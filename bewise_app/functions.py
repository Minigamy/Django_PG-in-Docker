import requests

from bewise_app.models import Quiz


def checking_for_uniqueness(question: dict):
    # Если в БД нет вопроса с таким id, то создаем запись.
    if not Quiz.objects.filter(question_id=question["id"]).exists():
        Quiz.objects.create(
            question_id=question["id"],
            text=question["question"],
            answer=question["answer"],
            date=question["created_at"]
        )
    # Если в БД есть запись с таким id, то отправляем запрос для получения нового вопроса и рекурсивно вызываем функцию
    # checking_for_uniqueness для проверки нового вопроса на уникальность.
    else:
        new_req = requests.get('https://jservice.io/api/random', data={"count": 1})
        new_req_dict = new_req.json()[0]  # type: dict
        checking_for_uniqueness(new_req_dict)
