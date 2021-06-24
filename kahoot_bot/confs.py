links = [
    "/img_kahoot/1img.webp",
    "/img_kahoot/2img.webp",
    "/img_kahoot/3img.webp",
    "/img_kahoot/4img.webp",
    "/img_kahoot/5img.webp",
    "/img_kahoot/6img.webp",
    "/img_kahoot/7img.webp",
    "/img_kahoot/8img.webp",
    "/img_kahoot/9img.webp",
    "/img_kahoot/10img.webp",
    "/img_kahoot/11img.webp",
    "/img_kahoot/12img.webp",
    "/img_kahoot/13img.webp",
    "/img_kahoot/14img.webp",
    "/img_kahoot/15img.webp",
    "/img_kahoot/16img.webp",
    "/img_kahoot/17img.webp",
    "/img_kahoot/18img.webp",
    "/img_kahoot/19img.webp",
    "/img_kahoot/20img.webp",
    "/img_kahoot/21img.webp",
    "/img_kahoot/22img.webp",
    "/img_kahoot/23img.webp",
    "/img_kahoot/24img.webp",
    "/img_kahoot/25img.webp",
]

qwerty = [
    "Что выведет данная команда?",
    "Python это змея?",
    "Какого знака не может быть в переменной?",
    "Что выведет данная команда?",
    "Какие цвета на лого python?",
    "Что выведет данная команда?",
    "Что выведет данная команда?",
    "Создатель python человек?",
    "Что выведет данная команда?",
    "Что выведет данная команда?",
    "Python - интерпретируемый язык или компилируемый?",
    "Сколько видов импорта сущуствует?",
    "Можно ли создать декоратор из класса?",
    "Можно ли использовать несколько декораторов для одной функции?",
    "Как пишутся комментарии в питоне?",
    "Как перевести первый символ строки в верхний регистр?",
    "Сколько методов в кортеже?",
    "Что выведет данная команда?",
    "Как зовут создателя python?",
    "Каким знаком обозначается остаток от деления нацело?",
    "Kак обозначается неравенство в Python?",
    "Какой набор символов используется для переноса строки ?",
    "Целую часть от деления можно найти с помощью?",
    "Сколько значений может принимать строковый тип данных?",
    "Команда, выполняющая или не выполняющая действие в зависимости от значения логического условия?",
]


answers = [
    {
        "condition": "🟥 3 + 2\n🟦 (5)\n🟨 5\n🟩 SyntaxError",
        "solution": [("🟥", False), ("🟦", False), ("🟨", True), ("🟩", False)],
    },
    {
        "condition": "🟥 True\n🟦 False",
        "solution": [("🟥", False), ("🟦", True)],
    },
    {
        "condition": "🟥 -\n🟦 Цифры\n🟨 _\n🟩 Буквы",
        "solution": [("🟥", True), ("🟦", False), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 1\n🟦 a\n🟨 b\n🟩 Error",
        "solution": [("🟥", False), ("🟦", False), ("🟨", False), ("🟩", True)],
    },
    {
        "condition": "🟥 Фиолетовый-Черный\n🟦 Синий-Зеленый\n🟨 Явно змея\n🟩 Желтый-Синий",
        "solution": [("🟥", False), ("🟦", False), ("🟨", False), ("🟩", True)],
    },
    {
        "condition": "🟥 От 1 до 100\n🟦 i 100 раз\n🟨 Error\n🟩 От 0 до 99",
        "solution": [("🟥", False), ("🟦", False), ("🟨", True), ("🟩", False)],
    },
    {
        "condition": "🟥 (abc)\n🟦 abc\n🟨 a+b+c\n🟩 Error",
        "solution": [("🟥", False), ("🟦", True), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 True\n🟦 False",
        "solution": [("🟥", True), ("🟦", False)],
    },
    {
        "condition": "🟥 TypeError\n🟦 274, 2\n🟨 274 + 2\n🟩 NameError",
        "solution": [("🟥", True), ("🟦", False), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 True\n🟦 False\n🟨 TypeError\n🟩 1",
        "solution": [("🟥", False), ("🟦", False), ("🟨", True), ("🟩", False)],
    },
    {
        "condition": "🟥 Интерпретируемый язык\n🟦 Компилируемый язык",
        "solution": [("🟥", True), ("🟦", False)],
    },
    {
        "condition": "🟥 4\n🟦 1\n🟨 2\n🟩 3",
        "solution": [("🟥", True), ("🟦", False), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 True\n🟦 False",
        "solution": [("🟥", True), ("🟦", False)],
    },
    {
        "condition": "🟥 True\n🟦 False",
        "solution": [("🟥", True), ("🟦", False)],
    },
    {
        "condition": "🟥 @\n🟦 #\n🟨 *\n🟩 +",
        "solution": [("🟥", False), ("🟦", True), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 .upper()\n🟦 .title()\n🟨 [0].upper()\n🟩 .lower()",
        "solution": [("🟥", False), ("🟦", True), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 2\n🟦 1\n🟨 4\n🟩 3",
        "solution": [("🟥", True), ("🟦", False), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 Error\n🟦 False\n🟨 True\n🟩 ()",
        "solution": [("🟥", False), ("🟦", False), ("🟨", False), ("🟩", True)],
    },
    {
        "condition": "🟥 Нирлатотеп\n🟦 Россум\n🟨 Роберт\n🟩 Гвидо",
        "solution": [("🟥", False), ("🟦", False), ("🟨", False), ("🟩", True)],
    },
    {
        "condition": "🟥 %\n🟦 **\n🟨 //\n🟩 ?!?",
        "solution": [("🟥", False), ("🟦", False), ("🟨", True), ("🟩", False)],
    },
    {
        "condition": "🟥 <>\n🟦 *сделай неравенство*\n🟨 !=\n🟩 /=",
        "solution": [("🟥", False), ("🟦", False), ("🟨", True), ("🟩", False)],
    },
    {
        "condition": "🟥 \p\n🟦 \\n\n🟨 /http\n🟩 /r",
        "solution": [("🟥", False), ("🟦", True), ("🟨", False), ("🟩", False)],
    },
    {
        "condition": "🟥 //\n🟦 /\n🟨 %\n🟩 div",
        "solution": [("🟥", True), ("🟦", False), ("🟨", False), ("🟩", True)],
    },
    {
        "condition": "🟥 1\n🟦 2\n🟨 3\n🟩 4",
        "solution": [("🟥", False), ("🟦", False), ("🟨", False), ("🟩", True)],
    },
    {
        "condition": "🟥 Логический тип данных\n🟦 Логическое условие\n🟨 Условный оператор\n🟩 Условное выражение",
        "solution": [("🟥", False), ("🟦", False), ("🟨", True), ("🟩", False)],
    },
]
