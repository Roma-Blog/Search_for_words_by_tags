# Парсер с поиском по тэгам

Клиенту нужна была программа, которая ищет упоминания нерелевантных городов на поддоменах, например, чтобы в Санкт-Петербурге не упоминалась Москва в тэгах: ‘title’, ‘description’, ‘keywords’, ‘h1’, ‘h2’, ‘h3’.

Программа, как поисковый бот, парсит все ссылки на странице и проверяет тэги на наличие упоминаний (их можно настроить, любые слова), затем переходит по собранным ссылкам.

В итоге мы получаем JSON-файл со списком адресов и тэгов, где упоминалось искомое. 

Важно было, чтобы программа работала корректно на любом сайте.