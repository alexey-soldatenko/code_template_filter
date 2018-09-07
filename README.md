# code_template_filter
Небольшое приложение - пример использования пользовательских шаблонных фильтров.
Данный фильтр будет обрабатывать обрабатывать фрагмент кода для его лучшего визуального отображения.

Сам фильтр находится в code_template_filter/code_block_template/templatetags/code_block.py

Фильтр создает номера строк и добавляет теги с классами, внешним видом которых мы и будем манипулировать.

В шаблоне main_page.html показан пример использования:

{%load code_block%}

{{code|code_block|safe}}

Запустив приложение, на главной странице можно видеть работу фильтра.
