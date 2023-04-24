from django.core.management import BaseCommand
from tree_menu.models import CategoryModel
from django.core.exceptions import ObjectDoesNotExist


data = (
        (None, 'Бытовая химия'),
        (None, 'Продукты'),
        ('Бытовая химия', 'Моющие средства'),
        ('Бытовая химия', 'Средства гигиены'),
        ('Бытовая химия', 'Средства для ванны'),
        ('Бытовая химия', 'Средства для мытья полов'),
        ('Продукты', 'Пирожные'),
        ('Продукты', 'Мясные изделия'),
        ('Продукты', 'Напитки'),
        ('Продукты', 'Булочные изделия'),
        ('Моющие средства', 'Пемолюкс'),
        ('Средства гигиены', 'Мыло снежинка'),
        ('Средства для ванны', 'Тайд'),
        ('Средства для мытья полов', 'Лысый из бразерс'),
        ('Пирожные', 'Картошка'),
        ('Мясные изделия','Стейк'),
        ('Напитки', 'Добрый Кола'),
        ('Булочные изделия', 'Самса с сыром'),
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Creating models')

        for item in data:
            try:
                parent = CategoryModel.objects.get(title=item[0])
            except ObjectDoesNotExist:
                parent = None

            CategoryModel.objects.create(
                title=item[1],
                parent=parent
            )

        self.stdout.write(self.style.SUCCESS('Created'))

