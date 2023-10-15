## GlobalVerse - Генератор кратких новостей с использованием Gradio

![Логотип GlobalVerse](frontend/static/favicon.png)

Добро пожаловать в проект GlobalVerse! Этот проект направлен на создание удобного веб-интерфейса для краткой выжимки новостей из различных международных источников с использованием Gradio. Проект включает в себя функции, такие как парсинг новостей, автоматический перевод и суммаризацию с использованием нейронной сети.

**Содержание**
- [Структура проекта](#структура-проекта)
- [Системные требования](#системные-требования)
- [Установка](#установка)
- [Использование](#использование)
- [Участие в проекте](#участие-в-проекте)
- [Лицензия](#лицензия)

### Краткое описание структуры:
- docs/: Документация проекта.
- frontend/: Фронтенд, разработанный на Svelte и Vite.
- gradio/: Приложение Gradio.
- src/: Исходный код Python, включая модули для обработки данных и нейросети.
- tests/: Тесты проекта.
- LICENSE: Лицензия проекта.
- README.md: Описание проекта.

### Полная структура проекта

Проект организован в несколько каталогов и файлов:

- **docs**: Содержит документацию как для разработчиков, так и для пользователей.
  - `developer_guide.md`: Руководство для разработчиков по настройке проекта.
  - `user_guide.md`: Руководство для пользователей по использованию приложения.

- **frontend**: Содержит веб-приложение, созданное с использованием Svelte и Svelte Kit.
  - `src`: Содержит компоненты Svelte и логику приложения.
  - `static`: Хранит статические ресурсы, такие как изображения.
  - `package.json`: Конфигурация пакета для веб-приложения.
  - `postcss.config.cjs`: Конфигурация PostCSS.
  - `svelte.config.js`: Конфигурация Svelte Kit.
  - `vite.config.js`: Конфигурация Vite.

- **gradio_app**: Содержит веб-приложение Gradio.
  - `app.py`: Основной скрипт приложения Gradio.
  - `__init__.py`: Скрипт инициализации для пакета Gradio.

- **src**: Содержит основную функциональность приложения.
  - **data_processing**: Отвечает за парсинг новостей и перевод.
    - `__init__.py`: Скрипт инициализации для пакета обработки данных.
    - `news_parser.py`: Парсит новости из международных источников.
    - `translator.py`: Осуществляет перевод новостей.
  - **neural_network**: Управляет суммаризацией на основе нейронной сети.
    - `bart_model.py`: Обрабатывает модель суммаризации.
    - `__init__.py`: Скрипт инициализации для пакета нейронных сетей.
  - `requirements.txt`: Список зависимостей проекта.

- **tests**: Содержит файлы с тестами для проекта.
  - `test_data_processing.py`: Тесты для компонентов обработки данных.
  - `test_frontend.py`: Тесты для веб-приложения.

- `LICENSE`: Файл с лицензией проекта.
- `README.md`: Вы читаете этот файл.

### Системные требования

Перед установкой и использованием проекта GlobalVerse убедитесь, что у вас установлены следующие системные требования:

- Python 3.6 или выше
- Node.js
- npm (Node Package Manager)

### Установка зависимостей 
Проект использует множество библиотек. Для установки необходимых зависимостей, выполните следующую команду в корневой директории проекта:

```bash
pip install -r requirements.txt
```

### Установка зависимостей для веб-приложения
```bash
   cd frontend
   npm install
   ```

### Установка

1. Склонируйте репозиторий проекта на свой локальный компьютер:

   ```bash
   git clone https://github.com/Carbon-Group/GlobalVerse-News-Summarizer.git
   ```

2. Перейдите в директорию проекта:

   ```bash
   cd GlobalVerse-News-Summarizer
   ```

### Использование

Для подробных инструкций по использованию обращайтесь к [Руководству пользователя](docs/user_guide.md) и интерфейсу веб-приложения.

Чтобы запустить веб-приложение Gradio, выполните следующую команду из корневой директории проекта:

```bash
python gradio_app/app.py
```

Чтобы запустить веб-приложение Svelte, используйте следующую команду:

```bash
cd frontend
npm run dev
```

Откройте веб-приложение в браузере по указанному URL.

## Документация

- Вся документация проекта доступна в директории docs/. Для пользователей проекта рекомендуется прочитать user_guide.md, а для разработчиков - данное developer_guide.md.

### Участие в проекте

Мы приветствуем ваши вклады в проект. Если вы хотите внести свой вклад, пожалуйста, следуйте указаниям в [Руководстве разработчика](docs/developer_guide.md).

### Лицензия

Этот проект распространяется под лицензией MIT - подробности смотрите в файле

 [LICENSE](LICENSE).
