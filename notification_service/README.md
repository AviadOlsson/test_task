# Тестовое задание "Сервис уведомлений"


Спроектировать и разработать сервис, который по заданным правилам запускает рассылку по списку клиентов.

**Сущность "рассылка" имеет атрибуты:**

• уникальный id рассылки

• дата и время запуска рассылки

• текст сообщения для доставки клиенту

• фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)

•дата и время окончания рассылки: если по каким-то причинам не успели разослать все сообщения - никакие сообщения клиентам после этого времени доставляться не должны

**Сущность "клиент" имеет атрибуты:**

• уникальный id клиента

• номер телефона клиента в формате **7XXXXXXXXXX** (X - цифра от 0 до 9)

• код мобильного оператора

• тег (произвольная метка)

• часовой пояс

**Сущность "сообщение" имеет атрибуты:**

• уникальный id сообщения

• дата и время создания (отправки)

• статус отправки

• id рассылки, в рамках которой было отправлено сообщение

• id клиента, которому отправили

**Спроектировать и реализовать API для:**

• добавления нового клиента в справочник со всеми его атрибутами

• обновления данных атрибутов клиента

• удаления клиента из справочника

• добавления новой рассылки со всеми её атрибутами

• получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам

• получения детальной статистики отправленных сообщений по конкретной рассылке

• обновления атрибутов рассылки

• удаления рассылки

• обработки активных рассылок и отправки сообщений клиентам
