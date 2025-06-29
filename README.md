### Документация к проекту
Проект представляет собой программу, позволяющую при помощи искусственного интеллекта предоставить пользователю отсортированный список цен на любые игровые товары, приложенный вместе с адресами интернет-магазинов.

---

### Описание
Система представляет собой интерактивную поисковую строку, принимающую названия искомых компьютерных игр, и в итоге выводящую на экран пользователя таблицу с открытыми источниками, предоставляющих товар по своему ценнику. Данный табличный список отсортирован, что позволяет покупателю найти самую дешёвую цену на определённую игру, и также моментально попасть на сайт данного магазина благодаря секции URL всех выведенных маркетплэйсов.

---

### Функциональные требования

#### Серверная часть
Серверная часть данной системы должна обеспечивать выполнение следующих требований:
- Собирать данные о ценах на видеоигры из открытых источников (API магазинов, парсинг сайтов);
- Хранить данные в определённой базе (Использование PostgreSQL);
- Обрабатывать данные с использованием Искусственного Интеллекта для анализа тенденций цен, прогнозирования и фильтрации некорректных данных;
- Реализировать API для взаимодействия с клиентской частью.

#### Клиентская часть
На клиентской части приложения должны быть реализованы следующие возможности и требования:
- Удобный интерфейс для поиска видеоигр;
- Система фильтрации поиска по различным категориям: названию, жанру, платформе, году издания и другим параметрам;
- Отображение списка цен с указанием магазинов и ссылок на данный продукт;
- Сортировка результатов по цене, популярности, рейтингу интернет-магазина и другим кртиериям;
- Возможность создания пользовательского аккаунта для сохранения избранных игр;
- Уведомления о снижении цен на выбранные игры (По рассылке в email или в самом приложений).

#### Искусственный интеллект
Искусственный интеллект при работе приложения должен:
- Анализировать исторические данные для прогнозирования изменения цен;
- Классифицировать и фильтровать данные для исключения некорректных и устаревших предложений;
- Иметь рекомендательную систему для предложения пользователю игр, которые могут быть ему интересны.

---

### Нефункциональные требования

#### Производительность
- Время ответа сервера на запросы не должно превышать 5 секунд;
- Обработка данных должна происходить в режиме, близком к реальному времени.

#### Маштабируемость
- Система должна быть способна обрабатывать данные из большого количества источников (Более 100 магазинов);
- Программа должна облажать возможностью добавления новых магазинов и платформ без значительных изменений в архитектуре.

#### Безопасность
- Защита пользовательских данных (логины, пароли, избранные игры);
- Обеспечение безопасности API (использование HTTPS, авторизация и аутентификация).

#### Надёжность
- Минимизация времени простоя сервера (uptime не менее 99,5%);
- Резервное копирование данных.

---

### Требования к информационной и программной совместимости

#### Серверная часть
- Язык программирования: Python (Django/FastAPI);
- База данных: PostreSQL;
- Искусственный интеллект: Tenserflow/PyTorch, Scikit-learn;
- Парсинг данных: BeautifulSoup, Scrapy.

#### Клиентская часть
- Веб-приложение: React.js/Vue.js

#### Инфраструктура
- Хостинг: AWS/Google Cloud;
- Контейнеризация: Docker;
- Оркестрация: Kubernetes.

---

### Стадии и этапы разработки

#### Анализ и проектирование
- Исследование рынка и выбор источников данных;
- Проектирование архитектуры приложения.

#### Настройка инструментов и окружения
- Настройка Git;
- Настройка используемых библиотек и описание их использования.

#### Разработка серверной части
- Разработка функционала серверной части;
- Разработка REST(RESTful) API для обработки запросов;
- Реализация многопоточной обработки запросов;
- Вспомогательный блок с графическим интерфейсом для управления и настройки сервером.

#### Разработка клиентской части
- Разработка функционала;
- Реализация графического интерфейса для ввода и вывода данных;
- Реализация многопоточной обработки запросов.

#### Интеграция базы данных
- Выбор подходящей СУБД (SQLite);
- Реализация модели данных.

#### Анализ данных с использованием технологий ИИ
- Реализация функции для обработки и анализа данных на сервере;
- Реализация представления "обработанных" данных в клиент.

#### Тестирование
- Тестирование функциональности и производительности;
- Исправление ошибок и оптимизация.

#### Развёртывание проекта
- Развёртывание приложения на выбранной платформе.

---

cd PriceSlide
