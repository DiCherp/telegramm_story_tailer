import telebot
from telebot import types

bot = telebot.TeleBot('7038813466:AAEgoniUhk2U8wgDae8aQuYQlB8cEkUnt1M')


coming_story = 0
#тексты
privetstv = 'привет! я бот, который может рассказывать истории с нелинейным сюжетом, зависящим от твоих выборов!'
vybor = 'выбери историю, которую хотел бы узнать'
gor_serd_1 = 'Жили на земле в старину одни люди, непроходимые леса окружали с трёх сторон таборы этих людей, а с четвёртой — была степь. Были это весёлые, сильные и смелые люди. И вот пришла однажды тяжёлая пора: явились откуда-то иные племена и прогнали прежних в глубь леса. Там были болота и тьма, потому что лес был старый, и так густо переплелись его ветви, что сквозь них не видать было неба, и лучи солнца едва могли пробить себе дорогу до болот сквозь густую листву. '
gor_serd_2 = 'Но когда его лучи падали на воду болот, то подымался смрад, и от него люди гибли один за другим. Тогда стали плакать жёны и дети этого племени, а отцы задумались и впали в тоску. Нужно было уйти из этого леса, и для того были две дороги: одна — назад, — там были сильные и злые враги, другая — вперёд, — там стояли великаны деревья, плотно обняв друг друга могучими ветвями, опустив узловатые корни глубоко в цепкий ил болота.'
gor_serd_3 = 'Эти каменные деревья стояли молча и неподвижно днём, в сером сумраке, и ещё плотнее сдвигались вокруг людей по вечерам, когда загорались костры. И всегда, днём и ночью, вокруг тех людей было кольцо крепкой тьмы, оно точно собиралось раздавить их, а они привыкли к степному простору. А ещё страшней было, когда ветер бил по вершинам деревьев и весь лес глухо гудел, точно грозил и пел похоронную песню тем людям.'
gor_serd_4 = 'Ваше имя - Данте, вы - человек, способный изменить судьбу этих людей'
gor_serd_v_storone1 = 'Шло время, люди голодали, некоторые гибли. Никто еще не отважился пойти против судьбы и попробовать покинуть проклятый лес.'
gor_serd_v_storone2 = 'Все еще не нашлось смельчака, достаточно смелого для того, чтобы противостоять судьбе. Данте в замешательстве, стоит ли ему становиться тем самым человеком?'
gor_serd_v_storone3 = 'Вы решили не вмешиваться в ход событий, сначала смерть поглотила ваших знакомых, а после и вас.'
gor_serd_5 = '— Не своротить камня с пути думою. Кто ничего не делает, с тем ничего не станется. Что мы тратим силы на думу да тоску? Вставайте, пойдём в лес и пройдём его сквозь, ведь имеет же он конец — всё на свете имеет конец! Идёмте! Ну! Гей!..'
gor_serd_6 = '… Повёл их Данко. Дружно все пошли за ним — верили в него. Трудный путь это был! Темно было, и на каждом шагу болото разевало свою жадную гнилую пасть, глотая людей, и деревья заступали дорогу могучей стеной. Переплелись их ветки между собой; как змеи, протянулись всюду корни, и каждый шаг много стоил пота и крови тем людям. Долго шли они… Всё гуще становился лес, всё меньше было сил! И вот стали роптать на Данко, говоря, что напрасно он, молодой и неопытный, повёл их куда-то. А он шёл впереди их и был бодр и ясен.'
gor_serd_7 = 'Данко заметил, что у людей появились сомнения на его счет'
gor_serd_8 = 'гроза грянула над лесом, зашептали деревья глухо, грозно. И стало тогда в лесу так темно, точно в нём собрались сразу все ночи, сколько их было на свете с той поры, как он родился. Шли маленькие люди, между больших деревьев и в грозном шуме молний, шли они, и, качаясь, великаны деревья скрипели и гудели сердитые песни, а молнии, летая над вершинами леса, освещали его на минутку синим, холодным огнём и исчезали так же быстро, как являлись, пугая людей'
gor_serd_9 = 'И деревья, освещённые холодным огнём молний, казались живыми, простирающими вокруг людей, уходивших из плена тьмы, корявые, длинные руки, сплетая их в густую сеть, пытаясь остановить людей. А из тьмы ветвей смотрело на идущих что-то страшное, тёмное и холодное. Это был трудный путь, и люди, утомлённые им, пали духом. Но им стыдно было сознаться в бессилии, и вот они в злобе и гневе обрушились на Данко, человека, который шёл впереди их. И стали они упрекать его в неумении управлять ими, — вот как!'
gor_serd_10 = '— Вы сказали: «Веди!» — и я повел! — крикнул Данко, становясь против них грудью. — Во мне есть мужество вести, вот потому я повёл вас! А вы? Что сделали вы в помощь себе? Вы только шли и не умели сохранить силы на путь более долгий! Вы только шли, шли, как стадо овец!'
gor_serd_11 = 'А лес всё гудел и гудел, вторя их крикам, и молнии разрывали тьму в клочья. Данко смотрел на тех, ради которых он понёс труд, и видел, что они как звери. Много людей стояло вокруг него, но не было на лицах их благородства, и нельзя было ему ждать пощады от них. Тогда и в его сердце вскипело негодование, но от жалости к людям оно погасло. Он любил людей и думал, что, может быть, без него они погибнут. '
gor_serd_12 = 'И вот его сердце вспыхнуло огнём желания спасти их, вывести на лёгкий путь, и тогда в его очах засверкали лучи того могучего огня… А они, увидав это, подумали, что он рассвирепел, отчего так ярко и разгорелись очи, и они насторожились, как волки, ожидая, что он будет бороться с ними, и стали плотнее окружать его, чтобы легче им было схватить и убить Данко. А он уже понял их думу, оттого ещё ярче загорелось в нём сердце, ибо эта их дума родила в нём тоску.'
gor_serd_13 = 'Оно пылало так ярко, как солнце, и ярче солнца, и весь лес замолчал, освещённый этим факелом великой любви к людям, а тьма разлетелась от света его и там, глубоко в лесу, дрожащая, пала в гнилой зев болота. Люди же, изумлённые, стали как камни.'
gor_serd_14 = 'Они бросились за ним, очарованные. Тогда лес снова зашумел, удивлённо качая вершинами, но его шум был заглушён топотом бегущих людей. Все бежали быстро и смело, увлекаемые чудесным зрелищем горящего сердца. И теперь гибли, но гибли без жалоб и слёз. А Данко всё был впереди, и сердце его всё пылало, пылало!'
gor_serd_15 = 'И вот вдруг лес расступился перед ним, расступился и остался сзади, плотный и немой, а Данко и все те люди сразу окунулись в море солнечного света и чистого воздуха, промытого дождём. Гроза была — там, сзади них, над лесом, а тут сияло солнце, вздыхала степь, блестела трава в бриллиантах дождя, и золотом сверкала река… Был вечер, и от лучей заката река казалась красной, как та кровь, что била горячей струёй из разорванной груди Данко.'
gor_serd_16 = 'Люди же, радостные и полные надежд, не заметили смерти его и не видали, что ещё пылает рядом с трупом Данко его смелое сердце. Только один осторожный человек заметил это и, боясь чего-то, наступил на гордое сердце ногой… И вот оно, рассыпавшись в искры, угасло…'
gor_serd_badend = 'К сожалению, вы погибли. На этом история кончается, но вы можете попробовать еще раз!'
gor_serd_goodend = 'Поздравляю с успешным окончанием истории об отважном Данко! Надеюсь, она вам понравилась!'

@bot.message_handler(commands=['start'])
def nachalo(message):
    bot.send_message(message.chat.id, privetstv)
    stories(message)

def stories(message):
    markup = types.InlineKeyboardMarkup()
    story_1 = types.InlineKeyboardButton('Горящее сердце', callback_data='goryaschee_serdce')
    markup.add(story_1)
    bot.send_message(message.chat.id, vybor, reply_markup=markup)

@bot.message_handler(commands=['stories'])
def stor(message):
    stories(message)


@bot.message_handler(regexp='начать историю "Горящее сердце"')
def gor_serd(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_1, reply_markup=markup)

def gor_serd2(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_2')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_2, reply_markup=markup)

def gor_serd3(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_3')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_3, reply_markup=markup)

def gor_serd_razvetv_1(message):
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Помочь людям', callback_data='gor_serd-pomosch')
    btn_2 = types.InlineKeyboardButton('Остаться в стороне', callback_data='gor_serd-v_storone_1')
    markup.row(btn_1);markup.row(btn_2)
    bot.send_message(message.chat.id, gor_serd_4, reply_markup=markup)

def gor_serd_v_storone_1(message):
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Помочь людям', callback_data='gor_serd-pomosch')
    btn_2 = types.InlineKeyboardButton('Остаться в стороне', callback_data='gor_serd-v_storone2')
    markup.row(btn_1);markup.row(btn_2)
    bot.send_message(message.chat.id, gor_serd_v_storone1, reply_markup=markup)

def gor_serd_v_storone_2(message):
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Помочь людям', callback_data='gor_serd-pomosch')
    btn_2 = types.InlineKeyboardButton('Остаться в стороне', callback_data='gor_serd-end_by_nachalo')
    markup.row(btn_1);markup.row(btn_2)
    bot.send_message(message.chat.id, gor_serd_v_storone2, reply_markup=markup)

def gor_serd_pomosch(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_4')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, 'Данко произнес:')
    bot.send_message(message.chat.id, gor_serd_5, reply_markup=markup)

def gor_serd4(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_5')
    markup.row(btn_next1)
    bot.send_message(message.chat.id,'Посмотрели на него и увидали, что он лучший из всех, потому что в очах его светилось много силы и живого огня.')
    bot.send_message(message.chat.id, '— Веди ты нас! — сказали они')
    bot.send_message(message.chat.id,'Тогда он повёл…', reply_markup=markup)

def gor_serd5(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_6')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_6, reply_markup=markup)

def gor_serd_razvetv_2(message):
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Не обращать внимания', callback_data='dalee_7')
    btn_2 = types.InlineKeyboardButton('Высказать недовольство по поводу недоверия к себе', callback_data='vozm1')
    markup.row(btn_1); markup.row(btn_2)
    bot.send_message(message.chat.id, gor_serd_7, reply_markup=markup)


def gor_serd6(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_8')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_8, reply_markup=markup)

def gor_serd7(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_9')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_9, reply_markup=markup)

def gor_serd_razvetv_3(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Ответить негодующим людям', callback_data='vozm2')
    btn_next2 = types.InlineKeyboardButton('Промолчать', callback_data='dalee_10')
    markup.row(btn_next1); markup.row(btn_next2)
    bot.send_message(message.chat.id, 'Остановились они и под торжествующий шум леса, среди дрожащей тьмы, усталые и злые, стали судить Данко.', reply_markup=markup)

def gor_serd8(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_11')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, '— Ты умрёшь! Ты умрёшь! — ревели они.', reply_markup=markup)

def gor_serd9(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_12')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_11, reply_markup=markup)

def gor_serd10(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_13')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_12, reply_markup=markup)

def gor_serd_razvetv_4(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Вырвать из груди полыхающее сердце', callback_data='dalee_14')
    btn_next2 = types.InlineKeyboardButton('Решить, что эти люди недостойны жизни', callback_data='vozm3')
    markup.row(btn_next1);
    markup.row(btn_next2)
    bot.send_message(message.chat.id, 'А лес всё пел свою мрачную песню, и гром гремел, и лил дождь…')
    bot.send_message(message.chat.id, '— Что сделаю я для людей?! — сильнее грома крикнул Данко.', reply_markup=markup)

def gor_serd11(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_15')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_13, reply_markup=markup)

def gor_serd12(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_16')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, '— Идём! — крикнул Данко и бросился вперёд на свое место, высоко держа горящее сердце и освещая им путь людям.')
    bot.send_message(message.chat.id, gor_serd_14, reply_markup=markup)

def gor_serd13(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_17')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_15, reply_markup=markup)

def gor_serd14(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Далее', callback_data='dalee_18')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, 'Кинул взор вперёд себя на ширь степи гордый смельчак Данко, — кинул он радостный взор на свободную землю и засмеялся гордо. А потом упал и — умер.', reply_markup=markup)

def gor_serd15(message):
    markup = types.InlineKeyboardMarkup()
    btn_next1 = types.InlineKeyboardButton('Окончить историю', callback_data='dalee_19')
    markup.row(btn_next1)
    bot.send_message(message.chat.id, gor_serd_16, reply_markup=markup)

def gor_serd_bad_end(message):
    unmarkup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, gor_serd_badend, reply_markup=unmarkup)
    stories(message)

def gor_serd_good_end(message):
    unmarkup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, gor_serd_goodend, reply_markup=unmarkup)
    stories(message)









@bot.callback_query_handler(func= lambda callback: True)
def callback_message(callback):
    unmarkup = types.ReplyKeyboardRemove()
    if callback.data == 'goryaschee_serdce':
        markup = types.ReplyKeyboardMarkup()
        btn_start = types.KeyboardButton('начать историю "Горящее сердце"')
        btn_back = types.KeyboardButton('выбрать другую')
        markup.row(btn_start); markup.row(btn_back)
        bot.send_message(callback.message.chat.id, 'вы выбрали историю "Горящее сердце"', reply_markup=markup)
    if callback.data == 'dalee':
        gor_serd2(callback.message)
    if callback.data == 'dalee_2':
        gor_serd3(callback.message)
    if callback.data == 'dalee_3':
        gor_serd_razvetv_1(callback.message)
    if callback.data == 'gor_serd-pomosch':
        bot.send_message(callback.message.chat.id, 'вы выбрали помочь людям', reply_markup=unmarkup)
        gor_serd_pomosch(callback.message)
    if callback.data == 'gor_serd-v_storone_1':
        bot.send_message(callback.message.chat.id, 'вы выбрали остаться в стороне',reply_markup=unmarkup)
        gor_serd_v_storone_1(callback.message)
    if callback.data == 'gor_serd-v_storone2':
        bot.send_message(callback.message.chat.id,'вы выбрали остаться в стороне' , reply_markup=unmarkup)
        gor_serd_v_storone_2(callback.message)
    if callback.data == 'gor_serd-end_by_nachalo':
        bot.send_message(callback.message.chat.id, gor_serd_v_storone3)
        gor_serd_bad_end(callback.message)
    if callback.data == 'dalee_4':
        gor_serd4(callback.message)
    if callback.data == 'dalee_5':
        gor_serd5(callback.message)
    if callback.data == 'dalee_6':
        gor_serd_razvetv_2(callback.message)
    if callback.data == 'dalee_7':
        bot.send_message(callback.message.chat.id, 'Люди начали считать вас слабым, некоторые из них решили бросить вас и вернуться назад.')
        gor_serd6(callback.message)
    if callback.data == 'vozm1':
        bot.send_message(callback.message.chat.id, 'Вы показали людям, что сильны духом и они перестали вас упрекать')
        gor_serd6(callback.message)
    if callback.data == 'dalee_8':
        gor_serd7(callback.message)
    if callback.data == 'dalee_9':
        gor_serd_razvetv_3(callback.message)
    if callback.data == 'vozm2':
        bot.send_message(callback.message.chat.id, gor_serd_10)
        bot.send_message(callback.message.chat.id, 'Но эти слова разъярили их ещё более.')
        gor_serd8(callback.message)
    if callback.data == 'dalee_10':
        bot.send_message(callback.message.chat.id, 'Ваше молчание разъярило людей')
        gor_serd8(callback.message)
    if callback.data == 'dalee_11':
        gor_serd9(callback.message)
    if callback.data == 'dalee_12':
        gor_serd10(callback.message)
    if callback.data == 'dalee_13':
        gor_serd_razvetv_4(callback.message)
    if callback.data == 'vozm3':
        bot.send_message(callback.message.chat.id,'Вы решили, что не хотите помогать этим людям. Тьма леса поглотила их, а после и вас')
        gor_serd_bad_end(callback.message)
    if callback.data == 'dalee_14':
        bot.send_message(callback.message.chat.id, 'И вдруг он разорвал руками себе грудь и вырвал из неё своё сердце и высоко поднял его над головой.')
        gor_serd11(callback.message)
    if callback.data == 'dalee_15':
        gor_serd12(callback.message)
    if callback.data == 'dalee_16':
        gor_serd13(callback.message)
    if callback.data == 'dalee_17':
        gor_serd14(callback.message)
    if callback.data == 'dalee_18':
        gor_serd15(callback.message)
    if callback.data == 'dalee_19':
        gor_serd_good_end(callback.message)






@bot.message_handler()
def all_the_words(message):
    if message.text.lower() == 'выбрать другую':
        unmarkup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'возвращаемся назад', reply_markup=unmarkup)
        stories(message)
    elif message.text.lower() == 'начать историю "Горящее сердце"':
        bot.send_message(message.chat.id, 'начинаем')
        gor_serd(message)
    elif message.text.lower() == 'Помочь людям':
        bot.send_message(message.chat.id, 'вы выбрали помочь людям')




