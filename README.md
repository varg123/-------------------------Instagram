# Ищем участников конкурса Instagram

Выводит имена участников конкурсов Instagram
Участником конкурса считается тот, кто подписался, поставил лайк и отметил друга.

### Как установить

Устанавливаем переменные окружения LOGIN и PASSWORD в соответствии с данными регистрации.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
$ pip install -r requirements.txt
```


### Пример использования

При запуске скрипта в качестве обязательного параметра указываем ссылку на пост Instagram.
```
$ python main.py https://www.instagram.com/p/BtON034lPhu/2019-04-29 06:50:36,808 - INFO - Instabot Started
2019-04-29 06:50:40,879 - INFO - Logged-in successfully as 'andrey_skilev'!
Getting followers of 1828755772: 100%|███████████████████████████████████████████████████████████████████▉| 12912/12913 [00:27<00:00, 471.63it/s]
Всего участников 95:
lena_ivannik_
bonbon_katrin
victoria_81_
koshkaanka
ann.mass
...
nastya_nastya.28
s.m.adilaeva_77
ksuhamakshanova
2019-04-29 06:51:35,165 - INFO - Bot stopped. Worked: 1 day, 2:12:54.071986
2019-04-29 06:51:35,166 - INFO - Total requests: 2095

```
