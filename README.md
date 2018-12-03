# delMyVKWall
Небольшой скрипт для удаления постов со стены ВК

Для работы скрипта необходим Python 3 и библиотека vk_api

для установки vk_api на Unix: pip3 install vk_api 
на windows в CMD: py -m pip install vk_api

Также необходим токен авторизации. 
Переходим по ссылке в новой вкладке, он будет в поле access_token, копируем. Cохраните поле user_id
https://oauth.vk.com/authorize?client_id=6770459&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.52
Запустите скрипт
Если вы все таки не сохранили поле user_id, то откройте любую свою фотографию ВК, откроется ссылка вида: 
https://vk.com/durov?z=photo{ваш user_id}_456264771%2Falbum1_0%2Frev
скопируйте его. 
