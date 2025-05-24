BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Дарова', 'Здарова', 'Здорова', 'Превет', 'Hello'],
            'responces': ['Здравствуйте! \n/help - помощь', 'Привет! \n/help - помощь']
        },
        'help': {
            'examples': ['Помоги', 'Помоги мне', 'Помоги, пожалуйста', 'help', 'help me', '/help', '/помощь'],
            'responces': ['\nКоманды: \n\n/json - случайная цитата\n/help - показать команды\n/stop - остановить бота\n/sites - случайный полезный сайт\n/projects - случайный полезный проект']
        },
        'projects': {
            'examples': ['/projects', '/project', '/проекты'],
            'responces': ['https://github.com/PojavLauncherTeam/PojavLauncher - java майнкрафт портированный на андроид',
                          'https://modrinth.com/modpack/deadflymp - моя сборка по майнкрафту (1.19.4/fabric)',
                          'https://godotengine.org - бесплатный и лёгкий игровой движок',
                          'https://store.epicgames.com - магазин игр + unreal enngine',
                          'https://hex-rays.com/ida-free - бесплатно превратить собранную программу в ассемблер',
                          'https://zed.dev/ - лучший редактор кода, который скоро будет доступен под windows',
                          'https://joytokey.net/en/ - если надо превратить джойстик в клавиатуру и мышь (поддерживает слои)'
                          'https://geode-sdk.org/ - лучший модлоадер под geometry dash',
                          'https://eraser.heidi.ie/ - стереть файлы до конца (подробнее об этом - https://dzen.ru/a/XOztxMseqQCyQtUu)',
                          'https://diskanalyzer.com/ - лучший бесплатный анализатор диска, покажет все файлы на диске графически',
                          'https://github.com/keijiro/Minis - лучший midi обработчик под unity',
                          'https://github.com/tModLoader/tModLoader - движок модов для террарии',
                          'https://github.com/TEdit/Terraria-Map-Editor - посмотреть на весь мир террарии, а также изменить его правила и блоки',
                          'https://github.com/stuffbydavid/Mine-imator - бесплатный 3д аниматор по майнкрафту',
                          'https://github.com/mkcs121/APK-Easy-Tool - побаловаться с apk файлами',
                          'https://github.com/blender/blender - продвинутый инструмент для 3д анимации/графики',
                          'https://github.com/n00mkrad/flowframes - бесплатная нейросеть (работает на самом ПК), которая добавляет новые кадры в видео, увеличивает фпс',
                          'https://github.com/GNOME/gimp - бесплатный фотошоп',
                          'https://github.com/microsoft/PowerToys - небольшой пак маленьких функций, которые улучшат работу за ПК'
                          
                        ]
        },
        'sites': {
            'examples': ['/site', '/sites', '/сайты'],
            'responces': ['https://imgur.com - хостинг картинок и видео', 
                          'https://github.com - хостинг исходного кода', 
                          'https://4pda.com - форум по технике', 
                          'https://deepseek.com - бесплатная нейросеть',
                          'https://cobalt.tools - бесплатно скачать видео/аудио с площадок в 4К',
                          'https://docs.unity3d.com - документация по unity',
                          'https://aternos.com - бесплатное создание серверов по майнкрафту',
                          'https://modrinth.com - лучший хостинг модов для майнкрафта',
                          'https://drive.google.com - лучшее облачное хранилище (бесплатно 15 ГБ)',
                          'https://bukkit.org / spigotmc.org - плагины на сервер по майнкрафту',
                          'https://devdocs.io - очень огромная документация по многим языкам программирования',
                          'https://forum.image-line.com - форум по fl studio'
                          ]
        },
        'JSONstatham': {
            'examples': ['/json', '/Джейсон'],
            'responces': [
                'Упал - вставай, встай - упай. Дабуди дабудай   © JSON statham',
                '«Жи-ши» пиши от души   © JSON statham',
                'Когда меня рожали, собственно, я и родился    © JSON statham',
                'Работа не волк, никто не волк, волк - волк    © JSON statham',
            ]
        },
        'Dubstep': {
            'examples': ['/dub', '/dubstep', 'дабстеп'],
            'responces': [
                ''
            ]
        },
        'DubstepArtists': {
            'examples': ['/artists', '/dubstepartists', 'дабстеп музыканты'],
            'responces': [
                ''
            ]
        }

    }
}