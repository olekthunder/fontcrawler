"""Fills model Font with random instances"""
import random
from string import ascii_lowercase as alph

from .models import Font, User


def generate_fonts(count=10):
    for _ in range(count):
        # random family 6-10 letters
        family = ''.join(random.choice(alph)
                         for _ in range(random.randrange(6, 10)))
        # random style
        style = random.choice(['bold', 'italic', 'cursive'])
        # random url
        url = 'http://{domen}.com/{name}.{ext}'.format(domen=''.join(random.sample(
            alph, random.randint(5, 10))), name=family, ext=random.choice(['woff', 'ttf', 'woff2']))
        # random existing user by pk
        user = User.objects.get(pk=random.randrange(User.objects.count()) + 1)
        Font.objects.create(user=user, family=family, style=style, url=url)
