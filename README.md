# Technical Excellence 101
Курс про техническое совершенство для нетехнарей.

Этот курс представлят из себя серию воркшопов, при помощи которых можно объяснить смысл основных инженерных практик даже тем, кто в жизни не написал ни одной строчки кода. Это могут быть владельцы продукта, бизнес эксперты, скрам-мастера и любые другие участники команды, которые хотят лучше понимать что такое техническое совершенство и почему ему так много внимания уделяют разработчики. Код — это текст, поэтому мы будем объяснять материал на примере обыкновенного текста. Для прохождения курса не требуется никаких специальных знаний, кроме владения текстовым редактором.

Во время курса вы почувствуете себя разработчиком, столкнетесь с препятствиями, с которыми сталкивается каждый разработчик и поймете как инженерные практики помогают преодолеть эти препятствия.

Курс предлагает определенную последовательность модулей для изучения, которая кажется авторам логичной. Но вы можете изучать модули в любой последовательности.

## Какие темы изучаются в курсе?
* Основные команды git
* Merge
* Trunk based development
* Pull request
* Unit testing (модульное тестирование)
* Test-driven development (разработка через тестирование)
* Code review
* Парное программирование
* Continuous Integration (непрерывная интеграция)
* Continuous Delivery (непрерывная поставка)

## Подготовка
1. Установите [Visual Studio Code](https://code.visualstudio.com/download)
2. Установите [git](https://git-scm.com/downloads)
3. Проверьте, что git работает
    * Откройте Terminal в MacOS или Git Bash в Windows
    * Выполните команду `git --version`
    * Если вы увидели вывод `git version 2.23.0`, значит все в порядке, git установлен. Числа могут быть другими.
4. Создайте папку, в которой вы будете работать, например `Projects`  
    Windows:
      ```
      cd %USERPROFILE%
      mkdir Projects
      cd Projects
      ```  
    MacOS:  
      ```
      cd ~
      mkdir Projects
      cd Projects
      ```  
5. Склонируйте репозиторий, выполнив команду   
`git clone https://github.com/bevzuk/technical-excellence-101.git`  
или (если у вас добавлен [SSH сертификат](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account))   
`git clone git@github.com:bevzuk/technical-excellence-101.git`  
или (если у вас установлен [GitHub CLI](https://cli.github.com))  
`gh repo clone bevzuk/technical-excellence-101`
6. Откройте локальный репозиторий в VS Code
    * Запустите VS Code
    * Откройте папку Projects/technical-excellence-101
      * Меню File -> Open Folder ... или 
      * Open ... на главном экране
      * Выберите папку Projects/technical-excellence-101
      * Нажмите Open
        ![](images/Open%20folder.png)
    * В левой панельке Explorer вы должны увидеть структуру проекта
      ![](images/Project%20structure.png)


## Структура курса

### Модуль 1. Git
1. Что такое система управления исходным кодом и какие проблемы она решает
2. Код = текст
3. Зачем нужны ветки
4. Что такое git, github, gitlab, bitbucket
5. Интерфейс командной строки и VS Code
6. git clone — клонировать удаленный репозиторий локально
7. git status — посмотреть статус локального репозитория
8. git add — добавить измененные файлы в снапшот
9. git commit — закомитить снапшот
10. Упражнение. Сохранение изменений в локальном репозитории
11. git pull — получить изменения из удаленного репозитория в локальный
12. git push — отправить изменения из локальног репозитория в удаленный
13. Упражнение. Обмен данными между локальными и удаленным репозиториями

### Модуль 2. Ветки, конфликты и TBD
1. git branch — создать ветку в локальном репозитории
2. git checkout — переключиться в локальную ветку
3. Упражнение. Создание, просмотр, переключение веток
4. Слияние веток
5. Конфликты и способы их разрешения
6. git merge — смержить ветку в текущую
7. Упражнение. Смержить ветку и разрешить конфликты
8. Trunk Based Development (TBD) — практика разработки в одной ветке
9. Упражнение. Совместная работа над общим кодом, используя TBD

### Модуль 3. Code Review
1. Упражнение. Диктант
2. Code Review — практика, помогающая давать обратную связь на код
3. Правила хорошего Code Review
4. Pull Request
5. Упражнение. Создать Pull Request, дать и получить обратную связь, исправить замечания и запушить код в master
6. Парное программирование как альтернатива Code Review
7. Упражнение. Исправить диктант в паре

### Модуль 4. Автотесты и Test Driven Development
1. Автотесты
3. Упражнение. Написать автотест на проверку текста
2. Пирамида тестирования
4. Test Driven Development
5. Упражнение. Написать тест и исправить ошибку в заголовке главы или тексте
6. Сдвиг влево
7. Тестировщик vs QA

### Модуль 5. Continuous Integration & Continuous Deployment (CI/CD)
1. Что такое Continuous Integration
2. Как распознать CI Theatre
3. CI Do/Don't
4. Упражнение. Исправить ошибку в заголовке
5. Continous Delivery и Continuous Deployment
6. Как устроен Deployment Pipeline
7. Типичные ошибки построения пайплайна

## Авторство
Идея курса принадлежит Антону Бевзюку (@bevzuk). В создании курса принимали участие Дарья Баянова, Федор Слесаренко, Арсений Кельдышев, Светлана Кривенко.

