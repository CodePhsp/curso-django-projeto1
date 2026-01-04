from random import randint
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


data_faker = Faker('pt_BR')


def request_recipes():
    return {
        'id': data_faker.random_number(digits=2, fix_len=True),
        'title': data_faker.sentence(nb_words=6),
        'description': data_faker.sentence(nb_words=12),
        'preparation_time': data_faker.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': data_faker.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': data_faker.text(3000),
        'created_at': data_faker.date_time(),
        'author': {
            'first_name': data_faker.first_name(),
            'last_name': data_faker.last_name(),
        },
        'category': {
            'name': data_faker.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(request_recipes())