from app.db.models import Cities, Places
from app.db.connection import get_sync_session
import random

db = get_sync_session()
if len(db.query(Cities).all()) == 0:
    cities = """insert into public."Cities" values
    ('Абаза', 0),
    ('Абакан', 1),
    ('Абдулино', 2),
    ('Абинск', 3),
    ('Агидель', 4),
    ('Агрыз', 5),
    ('Адыгейск', 6),
    ('Азнакаево', 7),
    ('Азов', 8),
    ('Ак-Довурак', 9),
    ('Аксай', 10),
    ('Алагир', 11),
    ('Алапаевск', 12),
    ('Алатырь', 13),
    ('Алдан', 14),
    ('Алейск', 15),
    ('Александров', 16),
    ('Александровск-Сахалинский', 17),
    ('Александровск', 18),
    ('Алексеевка', 19),
    ('Алексин', 20),
    ('Алзамай', 21),
    ('Алупка', 22),
    ('Алушта', 23),
    ('Альметьевск', 24),
    ('Амурск', 25),
    ('Анадырь', 26),
    ('Анапа', 27),
    ('Ангарск', 28),
    ('Андреаполь', 29),
    ('Анжеро-Судженск', 30),
    ('Анива', 31),
    ('Апатиты', 32),
    ('Апрелевка', 33),
    ('Апшеронск', 34),
    ('Арамиль', 35),
    ('Аргун', 36),
    ('Ардатов', 37),
    ('Ардон', 38),
    ('Арзамас', 39),
    ('Аркадак', 40),
    ('Армавир', 41),
    ('Армянск', 42),
    ('Арсеньев', 43),
    ('Арск', 44),
    ('Артём', 45),
    ('Артёмовск', 46),
    ('Артёмовский', 47),
    ('Архангельск', 48),
    ('Асбест', 49),
    ('Асино', 50),
    ('Астрахань', 51),
    ('Аткарск', 52),
    ('Ахтубинск', 53),
    ('Ачинск', 54),
    ('Аша', 55),
    ('Бабаево', 56),
    ('Бабушкин', 57),
    ('Бавлы', 58),
    ('Багратионовск', 59),
    ('Байкальск', 60),
    ('Баймак', 61),
    ('Бакал', 62),
    ('Баксан', 63),
    ('Балабаново', 64),
    ('Балаклава', 65),
    ('Балаково', 66),
    ('Балахна', 67),
    ('Балашиха', 68),
    ('Балашов', 69),
    ('Балей', 70),
    ('Балтийск', 71),
    ('Барабинск', 72),
    ('Барнаул', 73),
    ('Барыш', 74),
    ('Батайск', 75),
    ('Бахчисарай', 76),
    ('Бежецк', 77),
    ('Белая Калитва', 78),
    ('Белая Холуница', 79),
    ('Белгород', 80),
    ('Белебей', 81),
    ('Белинский', 82),
    ('Белово', 83),
    ('Белогорск', 84),
    ('Белозерск', 86),
    ('Белокуриха', 87),
    ('Беломорск', 88),
    ('Белоозёрский', 89),
    ('Белорецк', 90),
    ('Белореченск', 91),
    ('Белоусово', 92),
    ('Белоярский', 93),
    ('Белый', 94),
    ('Белёв', 95),
    ('Бердск', 96),
    ('Березники', 97),
    ('Берёзовский', 98),
    ('Беслан', 100),
    ('Бийск', 101),
    ('Бикин', 102),
    ('Билибино', 103),
    ('Биробиджан', 104),
    ('Бирск', 105),
    ('Бирюсинск', 106),
    ('Бирюч', 107),
    ('Благовещенск', 108),
    ('Благодарный', 110),
    ('Бобров', 111),
    ('Богданович', 112),
    ('Богородицк', 113),
    ('Богородск', 114),
    ('Боготол', 115),
    ('Богучар', 116),
    ('Бодайбо', 117),
    ('Бокситогорск', 118),
    ('Болгар', 119),
    ('Бологое', 120),
    ('Болотное', 121),
    ('Болохово', 122),
    ('Болхов', 123),
    ('Большой Камень', 124),
    ('Бор', 125),
    ('Борзя', 126),
    ('Борисоглебск', 127),
    ('Боровичи', 128),
    ('Боровск', 129),
    ('Бородино', 130),
    ('Братск', 131),
    ('Бронницы', 132),
    ('Брянск', 133),
    ('Бугульма', 134),
    ('Бугуруслан', 135),
    ('Будённовск', 136),
    ('Бузулук', 137),
    ('Буинск', 138),
    ('Буй', 139),
    ('Буйнакск', 140),
    ('Бутурлиновка', 141),
    ('Валдай', 142),
    ('Валуйки', 143),
    ('Велиж', 144),
    ('Великие Луки', 145),
    ('Великий Новгород', 146),
    ('Великий Устюг', 147),
    ('Вельск', 148),
    ('Венёв', 149),
    ('Верещагино', 150),
    ('Верея', 151),
    ('Верхнеуральск', 152),
    ('Верхний Тагил', 153),
    ('Верхний Уфалей', 154),
    ('Верхняя Пышма', 155),
    ('Верхняя Салда', 156),
    ('Верхняя Тура', 157),
    ('Верхотурье', 158),
    ('Верхоянск', 159),
    ('Весьегонск', 160),
    ('Ветлуга', 161),
    ('Видное', 162),
    ('Вилюйск', 163),
    ('Вилючинск', 164),
    ('Вихоревка', 165),
    ('Вичуга', 166),
    ('Владивосток', 167),
    ('Владикавказ', 168),
    ('Владимир', 169),
    ('Волгоград', 170),
    ('Волгодонск', 171),
    ('Волгореченск', 172),
    ('Волжск', 173),
    ('Волжский', 174),
    ('Вологда', 175),
    ('Володарск', 176),
    ('Волоколамск', 177),
    ('Волосово', 178),
    ('Волхов', 179),
    ('Волчанск', 180),
    ('Вольск', 181),
    ('Воркута', 182),
    ('Воронеж', 183),
    ('Ворсма', 184),
    ('Воскресенск', 185),
    ('Воткинск', 186),
    ('Всеволожск', 187),
    ('Вуктыл', 188),
    ('Выборг', 189),
    ('Выкса', 190),
    ('Высоковск', 191),
    ('Высоцк', 192),
    ('Вытегра', 193),
    ('Вышний Волочёк', 194),
    ('Вяземский', 195),
    ('Вязники', 196),
    ('Вязьма', 197),
    ('Вятские Поляны', 198),
    ('Гаврилов Посад', 199),
    ('Гаврилов-Ям', 200),
    ('Гагарин', 201),
    ('Гаджиево', 202),
    ('Гай', 203),
    ('Галич', 204),
    ('Гатчина', 205),
    ('Гвардейск', 206),
    ('Гдов', 207),
    ('Геленджик', 208),
    ('Георгиевск', 209),
    ('Глазов', 210),
    ('Голицыно', 211),
    ('Горбатов', 212),
    ('Горно-Алтайск', 213),
    ('Горнозаводск', 214),
    ('Горняк', 215),
    ('Городец', 216),
    ('Городище', 217),
    ('Городовиковск', 218),
    ('Гороховец', 219),
    ('Горячий Ключ', 220),
    ('Грайворон', 221),
    ('Гремячинск', 222),
    ('Грозный', 223),
    ('Грязи', 224),
    ('Грязовец', 225),
    ('Губаха', 226),
    ('Губкин', 227),
    ('Губкинский', 228),
    ('Гудермес', 229),
    ('Гуково', 230),
    ('Гулькевичи', 231),
    ('Гурьевск', 232),
    ('Гусев', 234),
    ('Гусиноозёрск', 235),
    ('Гусь-Хрустальный', 236),
    ('Давлеканово', 237),
    ('Дагестанские Огни', 238),
    ('Далматово', 239),
    ('Дальнегорск', 240),
    ('Дальнереченск', 241),
    ('Данилов', 242),
    ('Данков', 243),
    ('Дегтярск', 244),
    ('Дедовск', 245),
    ('Демидов', 246),
    ('Дербент', 247),
    ('Десногорск', 248),
    ('Джанкой', 249),
    ('Дзержинск', 250),
    ('Дзержинский', 251),
    ('Дивногорск', 252),
    ('Дигора', 253),
    ('Димитровград', 254),
    ('Дмитриев', 255),
    ('Дмитров', 256),
    ('Дмитровск', 257),
    ('Дно', 258),
    ('Добрянка', 259),
    ('Долгопрудный', 260),
    ('Долинск', 261),
    ('Домодедово', 262),
    ('Донецк', 263),
    ('Донской', 264),
    ('Дорогобуж', 265),
    ('Дрезна', 266),
    ('Дубна', 267),
    ('Дубовка', 268),
    ('Дудинка', 269),
    ('Духовщина', 270),
    ('Дюртюли', 271),
    ('Дятьково', 272),
    ('Евпатория', 273),
    ('Егорьевск', 274),
    ('Ейск', 275),
    ('Екатеринбург', 276),
    ('Елабуга', 277),
    ('Елец', 278),
    ('Елизово', 279),
    ('Ельня', 280),
    ('Еманжелинск', 281),
    ('Емва', 282),
    ('Енисейск', 283),
    ('Ермолино', 284),
    ('Ершов', 285),
    ('Ессентуки', 286),
    ('Ефремов', 287),
    ('Железноводск', 288),
    ('Железногорск-Илимский', 289),
    ('Железногорск', 290),
    ('Жердевка', 292),
    ('Жигулёвск', 293),
    ('Жиздра', 294),
    ('Жирновск', 295),
    ('Жуков', 296),
    ('Жуковка', 297),
    ('Жуковский', 298),
    ('Завитинск', 299),
    ('Заводоуковск', 300),
    ('Заволжск', 301),
    ('Заволжье', 302),
    ('Задонск', 303),
    ('Заинск', 304),
    ('Закаменск', 305),
    ('Заозёрный', 306),
    ('Заозёрск', 307),
    ('Западная Двина', 308),
    ('Заполярный', 309),
    ('Зарайск', 310),
    ('Заречный', 311),
    ('Заринск', 313),
    ('Звенигово', 314),
    ('Звенигород', 315),
    ('Зверево', 316),
    ('Зеленогорск', 317),
    ('Зеленоград', 319),
    ('Зеленоградск', 320),
    ('Зеленодольск', 321),
    ('Зеленокумск', 322),
    ('Зерноград', 323),
    ('Зея', 324),
    ('Зима', 325),
    ('Златоуст', 326),
    ('Злынка', 327),
    ('Змеиногорск', 328),
    ('Знаменск', 329),
    ('Зубцов', 330),
    ('Зуевка', 331),
    ('Ивангород', 332),
    ('Иваново', 333),
    ('Ивантеевка', 334),
    ('Ивдель', 335),
    ('Игарка', 336),
    ('Ижевск', 337),
    ('Избербаш', 338),
    ('Изобильный', 339),
    ('Иланский', 340),
    ('Инза', 341),
    ('Инкерман', 342),
    ('Иннополис', 343),
    ('Инсар', 344),
    ('Инта', 345),
    ('Ипатово', 346),
    ('Ирбит', 347),
    ('Иркутск', 348),
    ('Исилькуль', 349),
    ('Искитим', 350),
    ('Истра', 351),
    ('Ишим', 352),
    ('Ишимбай', 353),
    ('Йошкар-Ола', 354),
    ('Кадников', 355),
    ('Казань', 356),
    ('Калач-на-Дону', 357),
    ('Калач', 358),
    ('Калачинск', 359),
    ('Калининград', 360),
    ('Калининск', 361),
    ('Калтан', 362),
    ('Калуга', 363),
    ('Калязин', 364),
    ('Камбарка', 365),
    ('Каменка', 366),
    ('Каменногорск', 367),
    ('Каменск-Уральский', 368),
    ('Каменск-Шахтинский', 369),
    ('Камень-на-Оби', 370),
    ('Камешково', 371),
    ('Камызяк', 372),
    ('Камышин', 373),
    ('Камышлов', 374),
    ('Канаш', 375),
    ('Кандалакша', 376),
    ('Канск', 377),
    ('Карабаново', 378),
    ('Карабаш', 379),
    ('Карабулак', 380),
    ('Карасук', 381),
    ('Карачаевск', 382),
    ('Карачев', 383),
    ('Каргат', 384),
    ('Каргополь', 385),
    ('Карпинск', 386),
    ('Карталы', 387),
    ('Касимов', 388),
    ('Касли', 389),
    ('Каспийск', 390),
    ('Катав-Ивановск', 391),
    ('Катайск', 392),
    ('Качканар', 393),
    ('Кашин', 394),
    ('Кашира', 395),
    ('Кедровый', 396),
    ('Кемерово', 397),
    ('Кемь', 398),
    ('Керчь', 399),
    ('Кизел', 400),
    ('Кизилюрт', 401),
    ('Кизляр', 402),
    ('Кимовск', 403),
    ('Кимры', 404),
    ('Кингисепп', 405),
    ('Кинель', 406),
    ('Кинешма', 407),
    ('Киреевск', 408),
    ('Киренск', 409),
    ('Киржач', 410),
    ('Кириллов', 411),
    ('Кириши', 412),
    ('Киров', 413),
    ('Кировград', 415),
    ('Кирово-Чепецк', 416),
    ('Кировск', 417),
    ('Кирс', 419),
    ('Кирсанов', 420),
    ('Киселёвск', 421),
    ('Кисловодск', 422),
    ('Клин', 423),
    ('Клинцы', 424),
    ('Княгинино', 425),
    ('Ковдор', 426),
    ('Ковров', 427),
    ('Ковылкино', 428),
    ('Когалым', 429),
    ('Кодинск', 430),
    ('Козельск', 431),
    ('Козловка', 432),
    ('Козьмодемьянск', 433),
    ('Кола', 434),
    ('Кологрив', 435),
    ('Коломна', 436),
    ('Колпашево', 437),
    ('Колпино', 438),
    ('Кольчугино', 439),
    ('Коммунар', 440),
    ('Комсомольск-на-Амуре', 441),
    ('Комсомольск', 442),
    ('Конаково', 443),
    ('Кондопога', 444),
    ('Кондрово', 445),
    ('Константиновск', 446),
    ('Копейск', 447),
    ('Кораблино', 448),
    ('Кореновск', 449),
    ('Коркино', 450),
    ('Королёв', 451),
    ('Короча', 452),
    ('Корсаков', 453),
    ('Коряжма', 454),
    ('Костерёво', 455),
    ('Костомукша', 456),
    ('Кострома', 457),
    ('Котельники', 458),
    ('Котельниково', 459),
    ('Котельнич', 460),
    ('Котлас', 461),
    ('Котово', 462),
    ('Котовск', 463),
    ('Кохма', 464),
    ('Красавино', 465),
    ('Красноармейск', 466),
    ('Красновишерск', 468),
    ('Красногорск', 469),
    ('Краснодар', 470),
    ('Красное Село', 471),
    ('Краснозаводск', 472),
    ('Краснознаменск', 473),
    ('Краснокаменск', 475),
    ('Краснокамск', 476),
    ('Красноперекопск', 477),
    ('Краснослободск', 478),
    ('Краснотурьинск', 480),
    ('Красноуральск', 481),
    ('Красноуфимск', 482),
    ('Красноярск', 483),
    ('Красный Кут', 484),
    ('Красный Сулин', 485),
    ('Красный Холм', 486),
    ('Кремёнки', 487),
    ('Кронштадт', 488),
    ('Кропоткин', 489),
    ('Крымск', 490),
    ('Кстово', 491),
    ('Кубинка', 492),
    ('Кувандык', 493),
    ('Кувшиново', 494),
    ('Кудрово', 495),
    ('Кудымкар', 496),
    ('Кузнецк', 497),
    ('Куйбышев', 498),
    ('Кукмор', 499),
    ('Кулебаки', 500),
    ('Кумертау', 501),
    ('Кунгур', 502),
    ('Купино', 503),
    ('Курган', 504),
    ('Курганинск', 505),
    ('Курильск', 506),
    ('Курлово', 507),
    ('Куровское', 508),
    ('Курск', 509),
    ('Куртамыш', 510),
    ('Курчалой', 511),
    ('Курчатов', 512),
    ('Куса', 513),
    ('Кушва', 514),
    ('Кызыл', 515),
    ('Кыштым', 516),
    ('Кяхта', 517),
    ('Лабинск', 518),
    ('Лабытнанги', 519),
    ('Лагань', 520),
    ('Ладушкин', 521),
    ('Лаишево', 522),
    ('Лакинск', 523),
    ('Лангепас', 524),
    ('Лахденпохья', 525),
    ('Лебедянь', 526),
    ('Лениногорск', 527),
    ('Ленинск-Кузнецкий', 528),
    ('Ленинск', 529),
    ('Ленск', 530),
    ('Лермонтов', 531),
    ('Лесной', 532),
    ('Лесозаводск', 533),
    ('Лесосибирск', 534),
    ('Ливны', 535),
    ('Ликино-Дулёво', 536),
    ('Липецк', 537),
    ('Липки', 538),
    ('Лиски', 539),
    ('Лихославль', 540),
    ('Лобня', 541),
    ('Лодейное Поле', 542),
    ('Ломоносов', 543),
    ('Лосино-Петровский', 544),
    ('Луга', 545),
    ('Луза', 546),
    ('Лукоянов', 547),
    ('Луховицы', 548),
    ('Лысково', 549),
    ('Лысьва', 550),
    ('Лыткарино', 551),
    ('Льгов', 552),
    ('Любань', 553),
    ('Люберцы', 554),
    ('Любим', 555),
    ('Людиново', 556),
    ('Лянтор', 557),
    ('Магадан', 558),
    ('Магас', 559),
    ('Магнитогорск', 560),
    ('Майкоп', 561),
    ('Майский', 562),
    ('Макаров', 563),
    ('Макарьев', 564),
    ('Макушино', 565),
    ('Малая Вишера', 566),
    ('Малгобек', 567),
    ('Малмыж', 568),
    ('Малоархангельск', 569),
    ('Малоярославец', 570),
    ('Мамадыш', 571),
    ('Мамоново', 572),
    ('Мантурово', 573),
    ('Мариинск', 574),
    ('Мариинский Посад', 575),
    ('Маркс', 576),
    ('Махачкала', 577),
    ('Мглин', 578),
    ('Мегион', 579),
    ('Медвежьегорск', 580),
    ('Медногорск', 581),
    ('Медынь', 582),
    ('Межгорье', 583),
    ('Междуреченск', 584),
    ('Мезень', 585),
    ('Меленки', 586),
    ('Мелеуз', 587),
    ('Менделеевск', 588),
    ('Мензелинск', 589),
    ('Мещовск', 590),
    ('Миасс', 591),
    ('Микунь', 592),
    ('Миллерово', 593),
    ('Минеральные Воды', 594),
    ('Минусинск', 595),
    ('Миньяр', 596),
    ('Мирный', 597),
    ('Михайлов', 599),
    ('Михайловка', 600),
    ('Михайловск', 601),
    ('Мичуринск', 603),
    ('Могоча', 604),
    ('Можайск', 605),
    ('Можга', 606),
    ('Моздок', 607),
    ('Мончегорск', 608),
    ('Морозовск', 609),
    ('Моршанск', 610),
    ('Мосальск', 611),
    ('Москва', 612),
    ('Московский', 613),
    ('Муравленко', 614),
    ('Мураши', 615),
    ('Мурино', 616),
    ('Мурманск', 617),
    ('Муром', 618),
    ('Мценск', 619),
    ('Мыски', 620),
    ('Мытищи', 621),
    ('Мышкин', 622),
    ('Набережные Челны', 623),
    ('Навашино', 624),
    ('Наволоки', 625),
    ('Надым', 626),
    ('Назарово', 627),
    ('Назрань', 628),
    ('Называевск', 629),
    ('Нальчик', 630),
    ('Нариманов', 631),
    ('Наро-Фоминск', 632),
    ('Нарткала', 633),
    ('Нарьян-Мар', 634),
    ('Находка', 635),
    ('Невель', 636),
    ('Невельск', 637),
    ('Невинномысск', 638),
    ('Невьянск', 639),
    ('Нелидово', 640),
    ('Неман', 641),
    ('Нерехта', 642),
    ('Нерчинск', 643),
    ('Нерюнгри', 644),
    ('Нестеров', 645),
    ('Нефтегорск', 646),
    ('Нефтекамск', 647),
    ('Нефтекумск', 648),
    ('Нефтеюганск', 649),
    ('Нея', 650),
    ('Нижневартовск', 651),
    ('Нижнекамск', 652),
    ('Нижнеудинск', 653),
    ('Нижние Серги', 654),
    ('Нижний Ломов', 655),
    ('Нижний Новгород', 656),
    ('Нижний Тагил', 657),
    ('Нижняя Салда', 658),
    ('Нижняя Тура', 659),
    ('Николаевск-на-Амуре', 660),
    ('Николаевск', 661),
    ('Никольск', 662),
    ('Никольское', 664),
    ('Новая Ладога', 665),
    ('Новая Ляля', 666),
    ('Новоалександровск', 667),
    ('Новоалтайск', 668),
    ('Новоаннинский', 669),
    ('Нововоронеж', 670),
    ('Новодвинск', 671),
    ('Новозыбков', 672),
    ('Новокубанск', 673),
    ('Новокузнецк', 674),
    ('Новокуйбышевск', 675),
    ('Новомичуринск', 676),
    ('Новомосковск', 677),
    ('Новопавловск', 678),
    ('Новоржев', 679),
    ('Новороссийск', 680),
    ('Новосибирск', 681),
    ('Новосиль', 682),
    ('Новосокольники', 683),
    ('Новотроицк', 684),
    ('Новоузенск', 685),
    ('Новоульяновск', 686),
    ('Новоуральск', 687),
    ('Новохопёрск', 688),
    ('Новочебоксарск', 689),
    ('Новочеркасск', 690),
    ('Новошахтинск', 691),
    ('Новый Оскол', 692),
    ('Новый Уренгой', 693),
    ('Ногинск', 694),
    ('Нолинск', 695),
    ('Норильск', 696),
    ('Ноябрьск', 697),
    ('Нурлат', 698),
    ('Нытва', 699),
    ('Нюрба', 700),
    ('Нягань', 701),
    ('Нязепетровск', 702),
    ('Няндома', 703),
    ('Облучье', 704),
    ('Обнинск', 705),
    ('Обоянь', 706),
    ('Обь', 707),
    ('Одинцово', 708),
    ('Озёрск', 709),
    ('Озёры', 711),
    ('Октябрьск', 712),
    ('Октябрьский', 713),
    ('Окуловка', 714),
    ('Оленегорск', 715),
    ('Олонец', 716),
    ('Олёкминск', 717),
    ('Омск', 718),
    ('Омутнинск', 719),
    ('Онега', 720),
    ('Опочка', 721),
    ('Оренбург', 722),
    ('Орехово-Зуево', 723),
    ('Орлов', 724),
    ('Орск', 725),
    ('Орёл', 726),
    ('Оса', 727),
    ('Осинники', 728),
    ('Осташков', 729),
    ('Остров', 730),
    ('Островной', 731),
    ('Острогожск', 732),
    ('Отрадное', 733),
    ('Отрадный', 734),
    ('Оха', 735),
    ('Оханск', 736),
    ('Очёр', 737),
    ('Павлово', 738),
    ('Павловск', 739),
    ('Павловский Посад', 741),
    ('Палласовка', 742),
    ('Партизанск', 743),
    ('Певек', 744),
    ('Пенза', 745),
    ('Первомайск', 746),
    ('Первоуральск', 747),
    ('Перевоз', 748),
    ('Пересвет', 749),
    ('Переславль-Залесский', 750),
    ('Пермь', 751),
    ('Пестово', 752),
    ('Петергоф', 753),
    ('Петров Вал', 754),
    ('Петровск-Забайкальский', 755),
    ('Петровск', 756),
    ('Петрозаводск', 757),
    ('Петропавловск-Камчатский', 758),
    ('Петухово', 759),
    ('Петушки', 760),
    ('Печора', 761),
    ('Печоры', 762),
    ('Пикалёво', 763),
    ('Пионерский', 764),
    ('Питкяранта', 765),
    ('Плавск', 766),
    ('Пласт', 767),
    ('Плёс', 768),
    ('Поворино', 769),
    ('Подольск', 770),
    ('Подпорожье', 771),
    ('Покачи', 772),
    ('Покров', 773),
    ('Покровск', 774),
    ('Полевской', 775),
    ('Полесск', 776),
    ('Полысаево', 777),
    ('Полярные Зори', 778),
    ('Полярный', 779),
    ('Поронайск', 780),
    ('Порхов', 781),
    ('Похвистнево', 782),
    ('Почеп', 783),
    ('Починок', 784),
    ('Пошехонье', 785),
    ('Правдинск', 786),
    ('Приволжск', 787),
    ('Приморск', 788),
    ('Приморско-Ахтарск', 790),
    ('Приозерск', 791),
    ('Прокопьевск', 792),
    ('Пролетарск', 793),
    ('Протвино', 794),
    ('Прохладный', 795),
    ('Псков', 796),
    ('Пугачёв', 797),
    ('Пудож', 798),
    ('Пустошка', 799),
    ('Пучеж', 800),
    ('Пушкин', 801),
    ('Пушкино', 802),
    ('Пущино', 803),
    ('Пыталово', 804),
    ('Пыть-Ях', 805),
    ('Пятигорск', 806),
    ('Радужный', 807),
    ('Райчихинск', 809),
    ('Раменское', 810),
    ('Рассказово', 811),
    ('Ревда', 812),
    ('Реж', 813),
    ('Реутов', 814),
    ('Ржев', 815),
    ('Родники', 816),
    ('Рославль', 817),
    ('Россошь', 818),
    ('Ростов-на-Дону', 819),
    ('Ростов', 820),
    ('Рошаль', 821),
    ('Ртищево', 822),
    ('Рубцовск', 823),
    ('Рудня', 824),
    ('Руза', 825),
    ('Рузаевка', 826),
    ('Рыбинск', 827),
    ('Рыбное', 828),
    ('Рыльск', 829),
    ('Ряжск', 830),
    ('Рязань', 831),
    ('Саки', 832),
    ('Салават', 833),
    ('Салаир', 834),
    ('Салехард', 835),
    ('Сальск', 836),
    ('Самара', 837),
    ('Санкт-Петербург', 838),
    ('Саранск', 839),
    ('Сарапул', 840),
    ('Саратов', 841),
    ('Саров', 842),
    ('Сасово', 843),
    ('Сатка', 844),
    ('Сафоново', 845),
    ('Саяногорск', 846),
    ('Саянск', 847),
    ('Светлогорск', 848),
    ('Светлоград', 849),
    ('Светлый', 850),
    ('Светогорск', 851),
    ('Свирск', 852),
    ('Свободный', 853),
    ('Себеж', 854),
    ('Севастополь', 855),
    ('Северо-Курильск', 856),
    ('Северобайкальск', 857),
    ('Северодвинск', 858),
    ('Североморск', 859),
    ('Североуральск', 860),
    ('Северск', 861),
    ('Севск', 862),
    ('Сегежа', 863),
    ('Сельцо', 864),
    ('Семикаракорск', 865),
    ('Семилуки', 866),
    ('Семёнов', 867),
    ('Сенгилей', 868),
    ('Серафимович', 869),
    ('Сергач', 870),
    ('Сергиев Посад', 871),
    ('Сердобск', 872),
    ('Серов', 873),
    ('Серпухов', 874),
    ('Сертолово', 875),
    ('Сестрорецк', 876),
    ('Сибай', 877),
    ('Сим', 878),
    ('Симферополь', 879),
    ('Сковородино', 880),
    ('Скопин', 881),
    ('Славгород', 882),
    ('Славск', 883),
    ('Славянск-на-Кубани', 884),
    ('Сланцы', 885),
    ('Слободской', 886),
    ('Слюдянка', 887),
    ('Смоленск', 888),
    ('Снежинск', 889),
    ('Снежногорск', 890),
    ('Собинка', 891),
    ('Советск', 892),
    ('Советская Гавань', 895),
    ('Советский', 896),
    ('Сокол', 897),
    ('Солигалич', 898),
    ('Соликамск', 899),
    ('Солнечногорск', 900),
    ('Соль-Илецк', 901),
    ('Сольвычегодск', 902),
    ('Сольцы', 903),
    ('Сорочинск', 904),
    ('Сорск', 905),
    ('Сортавала', 906),
    ('Сосенский', 907),
    ('Сосновка', 908),
    ('Сосновоборск', 909),
    ('Сосновый Бор', 910),
    ('Сосногорск', 911),
    ('Сочи', 912),
    ('Спас-Деменск', 913),
    ('Спас-Клепики', 914),
    ('Спасск-Дальний', 915),
    ('Спасск-Рязанский', 916),
    ('Спасск', 917),
    ('Среднеколымск', 918),
    ('Среднеуральск', 919),
    ('Сретенск', 920),
    ('Ставрополь', 921),
    ('Старая Купавна', 922),
    ('Старая Русса', 923),
    ('Старица', 924),
    ('Стародуб', 925),
    ('Старый Крым', 926),
    ('Старый Оскол', 927),
    ('Стерлитамак', 928),
    ('Стрежевой', 929),
    ('Строитель', 930),
    ('Струнино', 931),
    ('Ступино', 932),
    ('Суворов', 933),
    ('Судак', 934),
    ('Суджа', 935),
    ('Судогда', 936),
    ('Суздаль', 937),
    ('Сунжа', 938),
    ('Суоярви', 939),
    ('Сураж', 940),
    ('Сургут', 941),
    ('Суровикино', 942),
    ('Сурск', 943),
    ('Сусуман', 944),
    ('Сухиничи', 945),
    ('Сухой Лог', 946),
    ('Сызрань', 947),
    ('Сыктывкар', 948),
    ('Сысерть', 949),
    ('Сычёвка', 950),
    ('Сясьстрой', 951),
    ('Тавда', 952),
    ('Таганрог', 953),
    ('Тайга', 954),
    ('Тайшет', 955),
    ('Талдом', 956),
    ('Талица', 957),
    ('Тамбов', 958),
    ('Тара', 959),
    ('Тарко-Сале', 960),
    ('Таруса', 961),
    ('Татарск', 962),
    ('Таштагол', 963),
    ('Тверь', 964),
    ('Теберда', 965),
    ('Тейково', 966),
    ('Темников', 967),
    ('Темрюк', 968),
    ('Терек', 969),
    ('Тетюши', 970),
    ('Тимашёвск', 971),
    ('Тихвин', 972),
    ('Тихорецк', 973),
    ('Тобольск', 974),
    ('Тогучин', 975),
    ('Тольятти', 976),
    ('Томари', 977),
    ('Томмот', 978),
    ('Томск', 979),
    ('Топки', 980),
    ('Торжок', 981),
    ('Торопец', 982),
    ('Тосно', 983),
    ('Тотьма', 984),
    ('Троицк', 985),
    ('Трубчевск', 987),
    ('Трёхгорный', 988),
    ('Туапсе', 989),
    ('Туймазы', 990),
    ('Тула', 991),
    ('Тулун', 992),
    ('Туран', 993),
    ('Туринск', 994),
    ('Тутаев', 995),
    ('Тында', 996),
    ('Тырныауз', 997),
    ('Тюкалинск', 998),
    ('Тюмень', 999),
    ('Уварово', 1000),
    ('Углегорск', 1001),
    ('Углич', 1002),
    ('Удачный', 1003),
    ('Удомля', 1004),
    ('Ужур', 1005),
    ('Узловая', 1006),
    ('Улан-Удэ', 1007),
    ('Ульяновск', 1008),
    ('Унеча', 1009),
    ('Урай', 1010),
    ('Урень', 1011),
    ('Уржум', 1012),
    ('Урус-Мартан', 1013),
    ('Урюпинск', 1014),
    ('Усинск', 1015),
    ('Усмань', 1016),
    ('Усолье-Сибирское', 1017),
    ('Усолье', 1018),
    ('Уссурийск', 1019),
    ('Усть-Джегута', 1020),
    ('Усть-Илимск', 1021),
    ('Усть-Катав', 1022),
    ('Усть-Кут', 1023),
    ('Усть-Лабинск', 1024),
    ('Устюжна', 1025),
    ('Уфа', 1026),
    ('Ухта', 1027),
    ('Учалы', 1028),
    ('Уяр', 1029),
    ('Фатеж', 1030),
    ('Феодосия', 1031),
    ('Фокино', 1032),
    ('Фролово', 1034),
    ('Фрязино', 1035),
    ('Фурманов', 1036),
    ('Хабаровск', 1037),
    ('Хадыженск', 1038),
    ('Ханты-Мансийск', 1039),
    ('Харабали', 1040),
    ('Харовск', 1041),
    ('Хасавюрт', 1042),
    ('Хвалынск', 1043),
    ('Хилок', 1044),
    ('Химки', 1045),
    ('Холм', 1046),
    ('Холмск', 1047),
    ('Хотьково', 1048),
    ('Цивильск', 1049),
    ('Цимлянск', 1050),
    ('Циолковский', 1051),
    ('Чадан', 1052),
    ('Чайковский', 1053),
    ('Чапаевск', 1054),
    ('Чаплыгин', 1055),
    ('Чебаркуль', 1056),
    ('Чебоксары', 1057),
    ('Чегем', 1058),
    ('Чекалин', 1059),
    ('Челябинск', 1060),
    ('Чердынь', 1061),
    ('Черемхово', 1062),
    ('Черепаново', 1063),
    ('Череповец', 1064),
    ('Черкесск', 1065),
    ('Черноголовка', 1066),
    ('Черногорск', 1067),
    ('Чернушка', 1068),
    ('Черняховск', 1069),
    ('Чехов', 1070),
    ('Чистополь', 1071),
    ('Чита', 1072),
    ('Чкаловск', 1073),
    ('Чудово', 1074),
    ('Чулым', 1075),
    ('Чусовой', 1076),
    ('Чухлома', 1077),
    ('Чёрмоз', 1078),
    ('Шагонар', 1079),
    ('Шадринск', 1080),
    ('Шали', 1081),
    ('Шарыпово', 1082),
    ('Шарья', 1083),
    ('Шатура', 1084),
    ('Шахты', 1085),
    ('Шахунья', 1086),
    ('Шацк', 1087),
    ('Шебекино', 1088),
    ('Шелехов', 1089),
    ('Шенкурск', 1090),
    ('Шилка', 1091),
    ('Шимановск', 1092),
    ('Шиханы', 1093),
    ('Шлиссельбург', 1094),
    ('Шумерля', 1095),
    ('Шумиха', 1096),
    ('Шуя', 1097),
    ('Щербинка', 1098),
    ('Щигры', 1099),
    ('Щучье', 1100),
    ('Щёкино', 1101),
    ('Щёлкино', 1102),
    ('Щёлково', 1103),
    ('Электрогорск', 1104),
    ('Электросталь', 1105),
    ('Электроугли', 1106),
    ('Элиста', 1107),
    ('Энгельс', 1108),
    ('Эртиль', 1109),
    ('Югорск', 1110),
    ('Южа', 1111),
    ('Южно-Сахалинск', 1112),
    ('Южно-Сухокумск', 1113),
    ('Южноуральск', 1114),
    ('Юрга', 1115),
    ('Юрьев-Польский', 1116),
    ('Юрьевец', 1117),
    ('Юрюзань', 1118),
    ('Юхнов', 1119),
    ('Ядрин', 1120),
    ('Якутск', 1121),
    ('Ялта', 1122),
    ('Ялуторовск', 1123),
    ('Янаул', 1124),
    ('Яранск', 1125),
    ('Яровое', 1126),
    ('Ярославль', 1127),
    ('Ярцево', 1128),
    ('Ясногорск', 1129),
    ('Ясный', 1130),
    ('Яхрома', 1131);"""
    db.execute(cities)
    db.commit()


    # Случайные долгота и широта для Санкт-Петербурга (границы города)
min_longitude, max_longitude = 60.5, 60.8
min_latitude, max_latitude = 56.8, 57.0

# Список возможных описаний
descriptions = [
    "Удобная парковка рядом с центром города.",
    "Безопасное место для вашего автомобиля.",
    "Широкие места и доступное ценообразование.",
    "Прекрасный вид и удобный подъезд.",
    "Рядом с торговым центром и ресторанами.",
]

# Список возможных улиц
streets = [
    "Улица Ленина",
    "Проспект Ленина",
    "Улица Кирова",
    "Проспект Волгоградский",
    "Улица Гагарина",
]

parkings = []

for _ in range(50):
    parking = {
        "City_id": 276,
        "parking_longitude": round(random.uniform(min_longitude, max_longitude), 6),
        "parking_latitude": round(random.uniform(min_latitude, max_latitude), 6),
        "number_of_places": random.randint(10, 50),
        "price": round(random.uniform(50, 300), 2),
        "description": random.choice(descriptions),
        "street_name": random.choice(streets),
    }
    new_place = Places(**parking)
    db.add(new_place)
db.commit()