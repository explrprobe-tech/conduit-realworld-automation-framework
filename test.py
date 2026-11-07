#для api метода я буду использовать API Objec Model архитектуру. Я создам класс для данного эндпоинта. Я предполагаю, что уже есть базовый класс в котором прописан base url, я буду использовать его в данном классе. Вообще можно было бы и прописать там метод для создания методов get, post и т.д., но я пропишу в данном классе сейчас

from test.urls import TICKETS_API
from test.tokens import ticket_creator

import requests
class TicketsApi(BaseApi):
    """Работа с обращениями"""
    def __init__(self):
        self.endpoint = TICKETS_API

    def create_ticket(self, headers, data):
        """Создание обращения"""
        self.response = requests.post(url=self.endpoint, headers=headers, data=data)
        return self.response


#дальше добавил бы этот класс в conftest фикстуру с scope session, т.к. нету смысла под каждый тест заново создавать класс, тут нету данных сессий

#conftest.py
from test.tickets_api import TicketsApi
import pytest

@pytest.fixture(scope="session")
def tickets_api():
    """Фикстура для работы с обращениями"""
    tickets_api_object = TicketsApi()
    yield tickets_api_object

#после этого использовал бы данную фикстуру для тестов, тут надо проверить 1 - позитивный кейс с созданием обращения, то есть проверить код 201, проверить ответ и структуру от сервиса

#test_tickets.py
from test.tokens import CREATOR_TICKETS
#тут желательно добавить параметризацию на проверку под несколькими пользователями и проверку создания обращения без токена
def test_create_tickets(tickets_api):
    response = tickets_api.create_ticket(headers={
        "Authorization": f"Bearer {CREATOR_TICKETS}"
    },
    data = {
        "title": "Payment issue",
        "customer_id": 123
        }
    )
    assert response.status_code == 201, "Status is not 201"
    assert response.body == #тут эталон body ответа 
    #также нужно проверить данные в бд, вызвать метод get и проверить, что запрос реально был создан, сверить поля метода get