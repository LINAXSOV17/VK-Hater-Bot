# для страницы
u_admins = []
bot_id = 0
u_token = ''

# для группы
g_admins = 653310913
group_id = https://vk.me/join/a_aePYYwKUyzVbm2XESw7ltVu3aeJfy4J74=
g_token = 'https://oauth.vk.com/blank.html#access_token=vk1.a.crjBluf3oQ1Vy_w3Drsl0CvRQWW1JrPgjxGqBI60KMoLfiaGHdmrxFaCNJa-fbNqSV42ik8I6PJ2m_t8hEVLYKUdzOAKXwLNMozVpuOUKpZ1i8XejE1waY1hB1_QKBFnGnK972xc9GAw7UhIxU39BLYaz_fRmB7lZYDFQHJXLfCxq0NUjNbD_W6lNferVFseXMspsa16V51ObUxCynTaTA&expires_in=0&user_id=653310913'

# комнады
hate = ['+хейт', '+hate']
unhate = ['-хейт', '-hate']
cooldown = ['!кд', '!cd']

# префиксы
hate_message_prefix = ['текст', 'text']
hate_photo_prefix = ['фото', 'photo']

# варианты сообщений
MESSAGE_VARIANTS = ["Я твой рот ебал", "Пошел нахуй", "Соси мой пайтонский член", "Маме своей так скажи",
                    "Ты быканул или мне показалось", "Не пиши мне, педик", "Ясно гей", "Пидорас ебаный", "Хуй из пасти вытащи и потом говори",
                    "Я вертел тебя на своем цифрововм хуе", "Ну и хули ты высрал", "Тебе уебать или дать пососать", "Нихуя ты умный", "Хорошо сосешь",
                    "А почему рот в говне", "Хуя ты сказанул", "От такой речи мне аж захотелось въебать тебе", "Ну и что ты мне сделаешь",
                    "Пососи ок", "Помойся, воняешь", "Нихуя ты заглотнул", "Готовь очко", "Сын шлюхи", "Вижу тебе понравилось как я тебя ебу",
                    "Лох ебаный", "Иди мамке поплачься", "В школе расскажешь", "Маме привет", "Шароеб ебаный", "Я твой рот ебал",
                    "На, хуй соси и не скули, пока я твою мать не начал ебать", "Че ты на мой хуй садишься как муха на говно",
                    "Сука, ты заебал мне яйца носом щекотать, соси аккуратно", "Прикол, твоя мать шлюха обоссаная", "Ты хули такой токсик, отчим в детстве выебал?",
                    "Оккупировал твое очко", "Ты че там кони двинул, сын пидораса", "Ты че заикаться то начал, хуеглот",
                    "Мамку твою ебал, что на это скажешь?", "Ты на кого выебываешься, фиксик ебаный", "Вхахахава, нихуя ты сказанул, чехол для хуя",
                    "От тебя говном воняет", "От таких слов даже твой батя в гробу перевернулся", "Ну как там с деньгами, еблан?",
                    "Нихуя тебе пердак разорвало", "Чет твой батя не постарался, сливаешься как говно", "Маму ебал", "Все ясно, автор пидорас",
                    "Расширил твое очко до размеров созвездия Гидры", "В палату быстро, долбоеб", "А когда я тебя ебал ты друое орал", "Как уебу тебе залупой по лбу", "Че ты высрал, подзалупник",
                    "Поешь говна", "10 iq ответ", "Завали ебало, уёбище безмозглое, сука я бы тебя закопал", "Хватит ныть как дешевая шлюха при виде огромного члена, твои выпуки читать все равно никто не будет",
                    "Молодец, а теперь отсоси так же, только с заглотом", "Девочка слитая, иди поплачься бате в хуй", "Ебало оффни, подзалупный творог",
                    "Сказал ты, сглотнув сперму своего бати", "Единственное,что отличает тебя от остальных маленьких хуеглотов, это твое оригинальное имя. Передай своим родителям, что они достаточно творческие хуеплеты.",
                    "Я тебе тут ебучку в моче ополаскиваю, нравится?", "Ебашу тебя хуем по лбу", "Обкончал тебя и твою дохлую мамашу",
                    "Че ты мне сделаешь, сын портовой шлюхи?"]

# варианты фото
PHOTO_VARIANTS = ["photo-198847189_457239017", "photo-198847189_457239018", "photo-198847189_457239019", "photo-198847189_457239021", "photo-198847189_457239023",
                  "photo-198847189_457239024", "photo-198847189_457239025", "photo-198847189_457239027", "photo-198847189_457239030", "photo-198847189_457239031",
                  "photo-198847189_457239033", "photo-198847189_457239034", "photo-198847189_457239035", "photo-198847189_457239036", "photo-198847189_457239037",
                  "photo-198847189_457239038", "photo-198847189_457239039", "photo-198847189_457239040", "photo-198847189_457239041", "photo-198847189_457239049",
                  "photo-198847189_457239050", "photo-198847189_457239051", "photo-198847189_457239052", "photo-198847189_457239053", "photo-198847189_457239054",
                  "photo-198847189_457239055", "photo-198847189_457239056", "photo-198847189_457239057", "photo-198847189_457239058", "photo-198847189_457239059",
                  "photo-198847189_457239060", "photo-198847189_457239061", "photo-198847189_457239062", "photo-198847189_457239063", "photo-198847189_457239064",
                  "photo-198847189_457239065", "photo-198847189_457239066", "photo-198847189_457239067", "photo-198847189_457239068", "photo-198847189_457239069",
                  "photo-198847189_457239070", "photo-198847189_457239071", "photo-198847189_457239072", "photo-198847189_457239073", "photo-198847189_457239074",
                  "photo-198847189_457239075", "photo-198847189_457239076", "photo-198847189_457239077", "photo-198847189_457239078", "photo-198847189_457239079",
                  "photo-198847189_457239080", "photo-198847189_457239081", "photo-198847189_457239083", "photo-198847189_457239084", "photo-198847189_457239085",
                  "photo-198847189_457239086", "photo-198847189_457239087", "photo-198847189_457239088", "photo-198847189_457239089", "photo-198847189_457239090",
                  "photo-198847189_457239091", "photo-198847189_457239092", "photo-198847189_457239093", "photo-198847189_457239094", "photo-198847189_457239095",
                  "photo-198847189_457239096"]

# варианты ошибок доступа
ERRORS = "Пососи", "А залупой по голове не хочешь?", "Хуя че вздумал", "Это так не работает", "1к и я подумаю"

