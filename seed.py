import products as db

# створюємо таблицю (якщо її ще нема)
db.clear_db()
db.create_table()

# додаємо товари
db.add_product(
    name="Жіноча футболка oversize",
    price=450,
    description="Об’ємна та комфортна oversize футболка добре тримає форму та не сковує рухів, а широкі та довгі рукави створюють практичний та стильний образ.",
    size="S",
    color="Чорний",
    category="Одяг",
    stock=10,
    image_url="static/photos/t-shirt.jpeg",
    is_new=False,
)

db.add_product(
    name="Жіночі джинси",
    price=1460,
    description="Модель вільного, прямого крою, що розширяється донизу. Джинси мають високу посадку, що вдало підкреслює талію та чудово поєднуються з речами oversize крою створюючи зручний повсякденний образ.",
    size="36",
    color="Синій",
    category="Одяг",
    stock=15,
    image_url="static/photos/jeans.jpeg",
    is_new=False,
)

db.add_product(
    name="Сорочка Staff squares",
    price=1260,
    description="Сорочку легко використовувати як елемент багатошарового луку в поєднанні з різним стилем одягу. Матеріал виробу не мнеться та завжди створює відчуття максимального комфорту.",
    size="L",
    color="чорний/білий/сірий",
    category="Одяг",
    stock=10,
    image_url="static/photos/shirt.jpeg",
    is_new=False,
)

db.add_product(
    name="Жіночий світшот oversize fleece",
    price=780,
    description="Однотонний світшот oversize чудово доповнює повсякденний образ та надійно зігріває в прохолодну погоду.",
    size="S",
    color="лимонний",
    category="Одяг",
    stock=20,
    image_url="static/photos/hudi.jpeg",
    is_new=False,
)

db.add_product(
    name="Футболка navy",
    price=440,
    description="Футболка у класичному крої з приємного матеріалу, яка не сковує рухів та забезпечує стильний лук.",
    size="S",
    color="темно-синій",
    category="Одяг",
    stock=15,
    image_url="static/photos/t-shirt2.jpeg",
    is_new=False,
)

db.add_product(
    name="Футболка khaki",
    price=440,
    description="Футболка у класичному крої з приємного матеріалу, яка не сковує рухів та забезпечує стильний лук.",
    size="XL",
    color="хакі.",
    category="Одяг",
    stock=10,
    image_url="static/photos/t-shirt3.jpeg",
    is_new=False,
)

db.add_product(
    name="Худі gray zip",
    price=1310,
    description="Худі приталеного крою з капюшоном та прорізними кишенями на блискавці. Матеріал виробу надає додаткової міцності, забезпечує еластичність та не сковує рухів.",
    size="L",
    color="сірий",
    category="Одяг",
    stock=10,
    image_url="static/photos/hudi2.jpeg",
    is_new=False,
)

db.add_product(
    name="Сукня dark gray",
    price=470,
    description="Сукня, що дарує максимальну свободу рухів і чудово поєднується з кросівками, кедами та капцями.",
    size="S",
    color="темно-сірий",
    category="Одяг",
    stock=15,
    image_url="static/photos/dress.jpeg",
    is_new=False,
)

db.add_product(
    name="Світшот green oversize fleece",
    price=890,
    description="Oversize світшот допоможе створити яскравий образ та зігрити в прохолодну пору.",
    size="M",
    color="зелений",
    category="Одяг",
    stock=20,
    image_url="static/photos/sweetshot.jpeg",
    is_new=True,
)


db.add_product(
    name="Жіночий жилет",
    price=1550,
    description="Утеплена жилетка дозволяє почувати себе вільно та впевнено завдяки вкороченому крою. Вона не сковує рухів, має подвійний утеплювач для прохолодних днів та чудово доповнює будь-який образ.",
    size="М",
    color="коричневий",
    category="Одяг",
    stock=30,
    image_url="static/photos/jacket.jpeg",
    is_new=True,
)

db.add_product(
    name="Жіночий жилет",
    price=1220,
    description="Практична, зручна жилетка вкороченного крою буде чудово поєднуватися з будь-яким одягом і захищати від холоду за рахунок утеплювача та високого коміра.",
    size="L",
    color="сірий",
    category="Одяг",
    stock=30,
    image_url="static/photos/jacket2.jpeg",
    is_new=True,
)

db.add_product(
    name="Кросівки",
    price=1740,
    description="Демісезонні кросівки мають масивну підошву з вираженим протектором, що забезпечує хороше зчеплення. Надійна шнурівка створює зручну фіксацію при ходьбі. Модель є чудовим варіантом як для спорту, так і на щодень.",
    size="40",
    color="чорний",
    category="Взуття",
    stock=20,
    image_url="static/photos/trainers.jpeg",
    is_new=True,
)

db.add_product(
    name="Жіночий спортивний костюм",
    price=1890,
    description="Зручний утеплений спортивний костюм дозволить почуватися “як удома” у будь-якій ситуації завдяки вільному oversize крою. Еластична стяжка на толстовці та висока посадка штанів підкреслять обриси фігури.",
    size="S",
    color="сірий",
    category="Одяг",
    stock=20,
    image_url="static/photos/costum.jpeg",
    is_new=True,
)

db.add_product(
    name="Спортивний костюм",
    price=2070,
    description="Поєднання динамічного стилю з комфортом. Сет зі штанів прямого вільного крою з контрастними лампасами та толстовкою на блискавці. Чудовий вибір для активного дозвілля.",
    size="XL",
    color="чорний",
    category="Одяг",
    stock=20,
    image_url="static/photos/costum2.jpeg",
    is_new=True,
)

db.add_product(
    name="Спортивні штани",
    price=1040,
    description="Утеплені спортивні штани виконані з приємної на дотик європейської бавовни та м’якого флісу. Модель має дуже зручну посадку завдяки еластичним резинкам і поясу зі шнурком та надійно захищає від холоду.",
    size="L",
    color="чорний",
    category="Одяг",
    stock=20,
    image_url="static/photos/trousers.jpeg",
    is_new=True,
)

db.add_product(
    name="Жіночий в'язаний светр",
    price=950,
    description="Светр oversize крою з круглим вирізом та пухнастою текстурною в’язкою забезпечить стильний образ та захист від холоду. Завдяки поєднанню різного матеріалу модель є стійкою до зносу, не розтягується з часом та має невелику вагу.",
    size="M",
    color="молочний",
    category="Одяг",
    stock=20,
    image_url="static/photos/sweater.jpeg",
    is_new=True,
)

