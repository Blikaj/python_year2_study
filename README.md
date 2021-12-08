# python_year2_study
Репозиторий для учебных проектов и программ на второй курс

Все готовые к использованию программы находятся в своих ветках

#h2 Файловый менеджер: ветка Python-filemanager
#h2 Однопоточный и многопоточный эхо серверы: ветка Python-echoserver
#h2 Web-сервер: Web-server
#h2 FTP-сервер: FTP-сервер
#h2 Ассиметричное шифрование: Crypto-server
#h2 Flask-приложение: flask-app


Ответы на контрольные вопросы лабораторной работы №1:


1. Опишите своими словами значение следующих терминов:
рабочий каталог – папка на машине, в которой разворачивается система контроля версий и в которой происходят изменения файлов во время работы
репозиторий – Удалённая или локальная папка со всеми файлами, коммитами и версиями проекта
коммит – обновление рабочего каталога, происходящее каждый раз, когда внесены существенные изменения
ветка – часть репозитория, содержащая главную или отдельные от главное версии проекта.
2. Ознакомьтесь с гайдом по выбранной вами программе-клиенту Git.
Я выбрал клиент GIT GUI. В данной статье ест вся необходимая информация для работы с клиентом: https://www.geeksforgeeks.org/working-on-git-for-gui/


1. Что такое удаленный репозиторий? 
Удалённый репозиторий – Удалённая рабочая среда со всеми файлами, коммитами и версиями проекта
2. Где нужно вводить команды git?
Команды нужно вводить либо в терминале git (если такой предусмотрен), либо в консоли
3. Для чего нужны ветки в системах контроля веток?
Ветки нужны для созданий различных версий проекта без вреда основной. Например: при разделении обязанностей в работе над проектом команда может создать отдельную ветку для каждого программиста. Также каждый программист может создавать отдельные ветки для тестовых версий своих продуктов.
4. Как возникают конфликты слиянии
Обычно конфликты возникают, когда два человека изменяют одни и те же строки в файле или один разработчик удаляет файл, который в это время изменяет другой разработчик. 
5. Как разрешать конфликты слияния?
Git прерывает работу в самом начале слияния или во время слияния, оставляя конфликтующие участки для изменения вручную.


1. Зачем нужен облачный хостинг репозиториев?
Для быстрого доступа разработчика к коду своего проекта с любой машины.
2. Какими основными функциями обладает сайт github.com?
На Github можно создавать открытые или приватные репозитории, которые будут видны только вам и выбранным вами людям. Есть возможность прямого добавления новых файлов в свой репозиторий через веб-интерфейс сервиса. Код проектов можно не только скопировать через Git, но и скачать в виде обычных архивов с сайта. Кроме Git, сервис поддерживает получение и редактирование кода через SVN и Mercurial. На сайте есть pastebin-сервис gist.github.com для быстрой публикации фрагментов кода.
3. Как организовать командную работу над открытым проектом?
Для этого можно создать приватный репозиторий, к которому предоставить доступ разработчикам, или же просто создать отдельные бранчи для каждого разработчика, после чего через менеджер push и pull заявок контролировать состояние проекта.
