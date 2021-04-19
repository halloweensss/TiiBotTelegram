class GamePredictor:

    def __init__(self):
        self.currentIndex = 0
        self.history = []
        self.database = Database()

    def getQuestion(self):
        return self.database.hashData[self.currentIndex]

    def reset(self):
        self.currentIndex = 0
        self.history = []

    def IsEnd(self):
        return self.database.hashData[self.currentIndex].isEnd

    def tryNext(self, answer: str):
        question = self.database.hashData[self.currentIndex]
        for a in question.answers:
            if (answer == a.answer):
                self.currentIndex = a.toIndex
                self.history.append((question, a))
                return self.database.hashData[self.currentIndex]
        return question

    def getHistoryQuestions(self):
        return self.history

class Answer:
    def __init__(self,
                 answer: str,
                 toIndex: int):
        self.answer = answer
        self.toIndex = toIndex


class Prediction:
    def __init__(self,
                 text : str,
                 src: str = "",
                 img: str = ""):
        self.text = text
        self.src = src
        self.img = img


class Question:
    def __init__(self,
                 question: str,
                 answers: [],
                 index: int,
                 fromIndex : int,
                 isStart: bool=False,
                 isEnd: bool=False,
                 description: str="",
                 prediction: Prediction=None):
        self.question = question
        self.answers = answers
        self.fromIndex = fromIndex
        self.isStart = isStart
        self.isEnd = isEnd
        self.description = description
        self.index = index
        self.prediction = prediction

class Database:
    def __init__(self):
        self.data = [
            Question(question="Ваша игра будет для одного или для нескольких игроков?",
                     answers=[Answer(f"Для одного", 1), Answer(f"Для нескольких", 2)],
                     index=0, fromIndex=-1, isStart=True, isEnd=False, description="Игра для нескольких игроков означает, что в игре моут присутствовать другие пользователи локально на одном компьютере, либо через интернет"),

            Question(question="В Вашей игре  двумерная или трехмерная графика?",
                     answers=[Answer(f"Двумерная", 3), Answer(f"Трехмерная", 4)],
                     index=1, fromIndex=0, isStart=False, isEnd=False, description="Двумерная графика - графика, проектирующаяся на два измерения (XY). \n Трехмерная графика – графика, проектирующаяся на три измерения (XYZ)."),

            Question(question="В Вашей игре Вы передвигаетесь персонажем?",
                     answers=[Answer(f"Да", 6), Answer(f"Нет", 5)],
                     index=3, fromIndex=1, isStart=False, isEnd=False, description="В игре Вы управляете неким существом или объектом"),

            Question(question="В Вашей игре нужно решать логические задачи?",
                     answers=[Answer(f"Да", 10), Answer(f"Нет", 9)],
                     index=5, fromIndex=3, isStart=False, isEnd=False, description="В игре присутствуют головоломки, пазлы, загадки."),

            Question(question="",
                     answers=[],
                     index=9, fromIndex=5, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Plague Inc: Evolved'",src="https://store.steampowered.com/app/246620/Plague_Inc_Evolved/",img="https://yandex-images.clstorage.net/5CSu0b230/3f441ahEG/UbgUYyMO1TNS7Ds4yHFS37W0e09b25BM3fYrDDI-1mMAHKP63M0uwRxwmgMRYnrjFSqkwzCuBQjrWT7XVXIgGgntAEdONtVyB-gmFHgdc6qwmAdaI9ucPICrWhkDY4I3VRXSlinhXsAlBdOvMWZ6n6mCKLrsR9yIW9TLOlV-CUYVmWFCSs4sa14w8yRRFSbD8MgHa7ff0KG13gM1JuomHph4iwKYlQpcLWmHeqSnp0dtToAO2JtAWCt0Sw4lrmGS2dQ5kjLmQb9qBKfkAekOh_ww-3t389AJuUrnjcZ2iiYUuItifFny3B05BzboC6eLxUIkjuh3VEwbgENO5T4Nkr1cUeqC8g3fBhx74MXZRlcsoHfnVweIGS0m53FKQo7mdDjvzrx1htgt9QfeQCM3BxGizPqgg3CAX8xDEpnerUrZoE02pjZBO8JUZ8QpYSIDbEj3W4fHSJGFGmPZBnqKGrgUr_qcxVZcFa1L8qgrF5NJWhAmDJtUSGPwz7JZZqkSEUQdalraBTvijCtoTdlSF6iwe38ne1Qd0WqDTdZG0uKsXLvK_MkebJktrxJIE4OfETo08tTjxGzT9Ac6ZVoRlg1oUeJ2lt3LDjCPEL11gm_8MI9n2wNARUGap826eo4SEHin0hA9vvCt3YsOIB836_1C8IZQlyyAl5RrluGqVe6ZNPkeelIdP7aEL2gJjY4nmECnnwvfTAUpnv8ZtrJWHvgU6-ZIEcZ4xRnnFhxHh0_5YgzycKNMZM-Me7ohmi1OibQ5aqp-QdPeaBuQxV2650hAR6vnc6D1xUqvAU5KGgZQ3OfeuNl6jHklm1Zsp7cLnR6MMvQvcPSbaPdCDWJ5ml1cnc6KHkUvhrQr4AmBJlMwHAOfV9tUBUEeow0ihuqiJEA_9hSNghjlnW8S4CufU_UquG6kLwSMMwRzpnHSPeLRdE1CImJxS-ogN9RRoXrXJOxbR_tj2PmhGrcdGsrE")),

            Question(question="",
                     answers=[],
                     index=10, fromIndex=5, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Zuma Deluxe'", src="https://store.steampowered.com/app/3330/Zuma_Deluxe/", img="https://cdn.akamai.steamstatic.com/steam/apps/3330/header.jpg?t=1615205692")),

            Question(question="Ваша игра приключенческая?",
                     answers=[Answer(f"Да", 12), Answer(f"Нет", 11)],
                     index=6, fromIndex=3, isStart=False, isEnd=False, description="Приключенческая игра - один из основных жанров компьютерных игр, представляющий собой интерактивную историю с главным героем, управляемым игроком. Важнейшими элементами игры в жанре приключение являются собственно повествование и исследование мира."),

            Question(question="По мере игры Ваш персонаж становиться сильнее?",
                     answers=[Answer(f"Да", 18), Answer(f"Нет", 17)],
                     index=11, fromIndex=6, isStart=False, isEnd=False, description="Вы можете улучшать своего персонажа, либо спустя некоторое время он сам становится сильнее"),

            Question(question="",
                     answers=[],
                     index=17, fromIndex=11, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Sonic Mania'", src="https://store.steampowered.com/app/584400/Sonic_Mania/", img="https://cdn.akamai.steamstatic.com/steam/apps/584400/header.jpg?t=1602817857")),

            Question(question="",
                     answers=[],
                     index=18, fromIndex=11, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Dead Cells'", src="https://store.steampowered.com/app/588650/Dead_Cells/", img="https://cdn.akamai.steamstatic.com/steam/apps/588650/header.jpg?t=1613038574")),

            Question(question="В Вашей игре есть логические задачи?",
                     answers=[Answer(f"Да", 20), Answer(f"Нет", 19)],
                     index=12, fromIndex=6, isStart=False, isEnd=False, description="В игре присутствуют головоломки, пазлы, загадки."),

            Question(question="",
                     answers=[],
                     index=19, fromIndex=12, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Ori and The Blind Forest'", src="https://store.steampowered.com/app/261570/Ori_and_the_Blind_Forest/", img="https://cdn.akamai.steamstatic.com/steam/apps/261570/header.jpg?t=1590605540")),

            Question(question="",
                     answers=[],
                     index=20, fromIndex=12, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Limbo'", src="https://store.steampowered.com/app/48000/LIMBO/", img="https://cdn.akamai.steamstatic.com/steam/apps/48000/header.jpg?t=1617191668")),

            Question(question="В Вашей игре открытый мир?",
                     answers=[Answer(f"Да", 8), Answer(f"Нет", 7)],
                     index=4, fromIndex=1, isStart=False, isEnd=False, description="Открытый мир - термин в компьютерных играх, обозначающий виртуальный мир, который игрок может свободно исследовать и свободно достигать в нем своих целей."),

            Question(question="Ваша игра Survival horror?",
                     answers=[Answer(f"Да", 14), Answer(f"Нет", 13)],
                     index=7, fromIndex=4, isStart=False, isEnd=False, description="Survival horror - жанр компьютерных игр, для которого характерными являются упор на выживание игрового персонажа и нагнетание атмосферы страха и тревоги, подобно литературе и фильмам ужасов."),

            Question(question="",
                     answers=[],
                     index=14, fromIndex=7, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Amnesia: Rebirth'", src="https://store.steampowered.com/app/999220/Amnesia_Rebirth/", img="https://cdn.akamai.steamstatic.com/steam/apps/999220/header.jpg?t=1617810640")),

            Question(question="",
                     answers=[],
                     index=13, fromIndex=7, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Half-Life: Alyx'", src="https://store.steampowered.com/app/546560/HalfLife_Alyx/", img="https://cdn.akamai.steamstatic.com/steam/apps/546560/header.jpg?t=1605207546")),

            Question(question="В Вашей игре можно передвигаться пешком?",
                     answers=[Answer(f"Да", 16), Answer(f"Нет", 15)],
                     index=8, fromIndex=4, isStart=False, isEnd=False, description="Передвижение персонажа происходит по некоторой поверхности без помощи посторонних средств передвижения"),

            Question(question="",
                     answers=[],
                     index=15, fromIndex=8, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Need for Speed'", src="https://store.steampowered.com/app/1262540/Need_for_Speed/", img="https://cdn.akamai.steamstatic.com/steam/apps/1262540/header.jpg?t=1614949605")),

            Question(question="Цель Вашей игры доставлять посылки?",
                     answers=[Answer(f"Да", 22), Answer(f"Нет", 21)],
                     index=16, fromIndex=8, isStart=False, isEnd=False, description="Цель игры перенести, перевезти посылку из точки А в точку Б"),

            Question(question="",
                     answers=[],
                     index=22, fromIndex=16, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Death Stranding'", src="https://store.steampowered.com/app/1190460/DEATH_STRANDING/", img="https://cdn.akamai.steamstatic.com/steam/apps/1190460/header.jpg?t=1616683107")),

            Question(question="Действия в Вашей игре происходят в будущем?",
                     answers=[Answer(f"Да", 24), Answer(f"Нет", 23)],
                     index=21, fromIndex=16, isStart=False, isEnd=False, description="Будущее — гипотетическая часть линии времени, множество событий, которые ещё не произошли, но могут произойти."),

            Question(question="",
                     answers=[],
                     index=24, fromIndex=21, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Cyberpunk 2077'", src="https://store.steampowered.com/app/1091500/Cyberpunk_2077/", img="https://cdn.akamai.steamstatic.com/steam/apps/1091500/header.jpg?t=1615811936")),

            Question(question="",
                     answers=[],
                     index=23, fromIndex=21, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'The Elder Scrolls V: Skyrim'", src="https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/", img="https://cdn.akamai.steamstatic.com/steam/apps/489830/header.jpg?t=1590515887")),

            Question(question="В Вашей игре двумерная или трехмерная графика?",
                     answers=[Answer(f"Двумерная", 25), Answer(f"Трехмерная", 26)],
                     index=2, fromIndex=0, isStart=False, isEnd=False, description="Двумерная графика - графика, проектирующаяся на два измерения (XY). \n Трехмерная графика – графика, проектирующаяся на три измерения (XYZ)."),

            Question(question="В Вашей игре открытый мир?",
                     answers=[Answer(f"Да", 28), Answer(f"Нет", 27)],
                     index=25, fromIndex=2, isStart=False, isEnd=False, description="Открытый мир - термин в компьютерных играх, обозначающий виртуальный мир, который игрок может свободно исследовать и свободно достигать в нем своих целей."),

            Question(question="В Вашей игре нужно искать предателя?",
                     answers=[Answer(f"Да", 32), Answer(f"Нет", 31)],
                     index=27, fromIndex=25, isStart=False, isEnd=False, description="Предатель - тот, кто предаёт, то есть нарушает верность кому-либо или чему-либо, вероломно изменяет кому-либо или чему-либо."),

            Question(question="",
                     answers=[],
                     index=32, fromIndex=27, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Among Us'", src="https://store.steampowered.com/app/945360/Among_Us/", img="https://cdn.akamai.steamstatic.com/steam/apps/945360/header_alt_assets_1.jpg?t=1617213983")),

            Question(question="В вашей игре есть командная работа?",
                     answers=[Answer(f"Да", 40), Answer(f"Нет", 39)],
                     index=31, fromIndex=27, isStart=False, isEnd=False, description="Работа в команде – это согласованная, осознанная деятельность участников сплочённой группы, направленная на достижение общей цели."),

            Question(question="",
                     answers=[],
                     index=40, fromIndex=31, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Cuphead'", src="https://store.steampowered.com/app/268910/Cuphead/", img="https://cdn.akamai.steamstatic.com/steam/apps/268910/header.jpg?t=1589281999")),

            Question(question="",
                     answers=[],
                     index=39, fromIndex=31, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Hearthstone'", src="https://playhearthstone.com/ru-ru", img="https://i.playground.ru/p/gwQo1hsrGDo44_mI7xuRcQ.jpeg")),

            Question(question="В Вашей игре можно строить?",
                     answers=[Answer(f"Да", 34), Answer(f"Нет", 33)],
                     index=28, fromIndex=25, isStart=False, isEnd=False, description="Строительство — создание (возведение) зданий, строений и сооружений."),

            Question(question="",
                     answers=[],
                     index=34, fromIndex=28, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Terraria'",src="https://store.steampowered.com/app/105600/Terraria/", img="https://cdn.akamai.steamstatic.com/steam/apps/105600/header.jpg?t=1590092560")),

            Question(question="",
                     answers=[],
                     index=33, fromIndex=28, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Diablo'", src="https://diablo2.blizzard.com/ru-ru/#", img="https://gamecheck.ru/uploads/posts/2020-07/1594830534_205.jpg")),

            Question(question="В Вашей игре открытый мир?",
                     answers=[Answer(f"Да", 30), Answer(f"Нет", 29)],
                     index=26, fromIndex=2, isStart=False, isEnd=False, description="Открытый мир - термин в компьютерных играх, обозначающий виртуальный мир, который игрок может свободно исследовать и свободно достигать в нем своих целей."),

            Question(question="В Вашей игре есть командная работа?",
                     answers=[Answer(f"Да", 36), Answer(f"Нет", 35)],
                     index=29, fromIndex=26, isStart=False, isEnd=False, description="Работа в команде – это согласованная, осознанная деятельность участников сплочённой группы, направленная на достижение общей цели."),

            Question(question="",
                     answers=[],
                     index=35, fromIndex=29, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'FIFA'", src="https://www.ea.com/ru-ru/games/fifa/fifa-21", img="https://webteindir.com/wp-content/uploads/2020/06/FIFA-21-fiyat-2048x1153.jpg")),

            Question(question="Ваша игра с видом свехру?",
                     answers=[Answer(f"Да", 42), Answer(f"Нет", 41)],
                     index=36, fromIndex=29, isStart=False, isEnd=False, description="Вид сверху является довольно синонимом вида с высоты птичьего полета, но обычно подразумевает менее высокую точку обзора, чем последний термин. Например, в компьютерных и видеоиграх «вид сверху» персонажа или ситуации часто помещает точку обзора всего на несколько футов (метр или два) выше человеческого роста."),

            Question(question="Ваша игра шутер?",
                     answers=[Answer(f"Да", 46), Answer(f"Нет", 45)],
                     index=41, fromIndex=36, isStart=False, isEnd=False, description="Шутер - жанр компьютерных игр, основанный на стрельбе и уничтожении врагов."),

            Question(question="",
                     answers=[],
                     index=45, fromIndex=41, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'SMITE'", src="https://store.steampowered.com/app/386360/SMITE/", img="https://cdn.akamai.steamstatic.com/steam/apps/386360/header_russian.jpg?t=1616529736")),

            Question(question="Ваша игра использует механику Battle Royale?",
                     answers=[Answer(f"Да", 54), Answer(f"Нет", 53)],
                     index=46, fromIndex=41, isStart=False, isEnd=False, description="Battle Royale - один из жанров массовых многопользовательских онлайнигр, совмещающий в себе элементы симулятора выживания с режимом last man standing. «Королевская битва» сталкивает большое количество управляемых игроками персонажей с минимальным набором снаряжения на ограниченной карте; игроки должны искать на карте оружие и уничтожать противников, пока в игре не останется только один."),

            Question(question="Ваша игра использует мультяшную графику?",
                     answers=[Answer(f"Да", 58), Answer(f"Нет", 57)],
                     index=53, fromIndex=46, isStart=False, isEnd=False, description="Мультяшная (cartoon) графика применяется, в основном для преувеличенных, комических или карикатурных изображений. Но при этом используются более сложные текстуры, рендеринг и тени."),

            Question(question="",
                     answers=[],
                     index=57, fromIndex=53, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Battlefield'", src="https://store.steampowered.com/app/1238810/Battlefield_V/", img="https://cdn.akamai.steamstatic.com/steam/apps/1238810/header.jpg?t=1615895305")),

            Question(question="",
                     answers=[],
                     index=58, fromIndex=53, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Overwatch'", src="https://playoverwatch.com/ru-ru/", img="https://get.wallhere.com/photo/Overwatch-Tracer-Overwatch-1899869.jpg")),

            Question(question="Ваша игра использует мультяшную графику?",
                     answers=[Answer(f"Да", 60), Answer(f"Нет", 59)],
                     index=54, fromIndex=46, isStart=False, isEnd=False, description="Мультяшная (cartoon) графика применяется, в основном для преувеличенных, комических или карикатурных изображений. Но при этом используются более сложные текстуры, рендеринг и тени."),

            Question(question="",
                     answers=[],
                     index=59, fromIndex=54, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Apex Legends'", src="https://www.ea.com/ru-ru/games/apex-legends/about", img="https://i.playground.ru/p/sI04ItCPRsY74PH25sCKnQ.jpeg")),

            Question(question="",
                     answers=[],
                     index=60, fromIndex=54, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Fortnite'", src="https://www.epicgames.com/fortnite/ru/home", img="https://wonder-day.com/wp-content/uploads/2020/03/Wonder-DAY-Wallpapers-Fortnite-2-1.jpg")),

            Question(question="В Вашей игре нужно готовить?",
                     answers=[Answer(f"Да", 48), Answer(f"Нет", 47)],
                     index=42, fromIndex=36, isStart=False, isEnd=False, description="Готовка - приготовление пищи"),

            Question(question="",
                     answers=[],
                     index=48, fromIndex=42, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Overcooked! 2'", src="https://store.steampowered.com/app/728880/Overcooked_2/", img="https://cdn.akamai.steamstatic.com/steam/apps/728880/header.jpg?t=1608812250")),

            Question(question="",
                     answers=[],
                     index=47, fromIndex=42, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Dota 2'", src="https://store.steampowered.com/app/570/Dota_2/", img="https://cdn.akamai.steamstatic.com/steam/apps/570/header.jpg?t=1618283868")),

            Question(question="Ваша игра происходит в кубическом мире?",
                     answers=[Answer(f"Да", 37), Answer(f"Нет", 38)],
                     index=30, fromIndex=26, isStart=False, isEnd=False, description="Кубически мир - это мир, где все состоит из кубов"),

            Question(question="",
                     answers=[],
                     index=37, fromIndex=30, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Minecraft'", src="https://www.minecraft.net/ru-ru/", img="https://bonuspb.ru/uploads/category/57/menu_maynkraft.jpg")),

            Question(question="Действия в Вашей игре происходят в космосе?",
                     answers=[Answer(f"Да", 44), Answer(f"Нет", 43)],
                     index=38, fromIndex=30, isStart=False, isEnd=False, description="Космос - относительно пустые участки Вселенной, которые лежат вне границ атмосфер небесных тел."),

            Question(question="В Вашей игре можно грабить?",
                     answers=[Answer(f"Да", 50), Answer(f"Нет", 49)],
                     index=43, fromIndex=38, isStart=False, isEnd=False, description="Грабеж - открытое хищение чужого имущества."),

            Question(question="",
                     answers=[],
                     index=49, fromIndex=43, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'World of Warcraft'", src="https://worldofwarcraft.com/ru-ru/", img="https://u.livelib.ru/reader/Tacet/o/ldu0kzq9/o-o.jpeg")),

            Question(question="",
                     answers=[],
                     index=50, fromIndex=43, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'GTA 5'", src="https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/", img="https://cdn.akamai.steamstatic.com/steam/apps/271590/header.jpg?t=1618065750")),

            Question(question="В Вашей игре можно свободно летать на корабле?",
                     answers=[Answer(f"Да", 51), Answer(f"Нет", 52)],
                     index=44, fromIndex=38, isStart=False, isEnd=False, description="Возможность путешествия между звёздами космических пилотируемых кораблей или автоматических станций"),

            Question(question="В Вашей игре может находиться свыше 100 игроков?",
                     answers=[Answer(f"Да", 56), Answer(f"Нет", 55)],
                     index=51, fromIndex=44, isStart=False, isEnd=False, description="Игра, в которой может быть больше 100 игровов на одном севере"),

            Question(question="",
                     answers=[],
                     index=52, fromIndex=44, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Destiny 2'", src="https://store.steampowered.com/app/1085660/Destiny_2/", img="https://cdn.akamai.steamstatic.com/steam/apps/1085660/header_russian.jpg?t=1617205372")),

            Question(question="",
                     answers=[],
                     index=55, fromIndex=51, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'No Man’s Sky'", src="https://store.steampowered.com/app/275850/No_Mans_Sky/", img="https://cdn.akamai.steamstatic.com/steam/apps/275850/header_alt_assets_2.jpg?t=1617200814")),

            Question(question="",
                     answers=[],
                     index=56, fromIndex=51, isStart=False, isEnd=True, description="",
                     prediction=Prediction(text="Возможно, Ваша игра будет похожа на 'Eve Online'", src="https://store.steampowered.com/app/8500/EVE_Online/", img ="https://cdn.akamai.steamstatic.com/steam/apps/8500/header_russian.jpg?t=1618500013")),
        ]

        self.hashData = {}
        for q in self.data:
            self.hashData[q.index] = q