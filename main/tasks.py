# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.contrib.auth.models import User

from .crawler.crawler import fetch_fonts
from .models import Font


@shared_task
def parse_page(user_id, url):
    # list containing dicts with keys 'family', 'sources', 'style'
    results = fetch_fonts(url)
    for result in results:
        # print(result)
        sources = result.get('sources')
        user = User.objects.get(id=user_id)
        for source in sources:
            family = result.get('family')
            print(family)
            style = result.get('style')
            # Check if already in database
            similar_obj_exists = Font.objects.filter(user=user,
                                                     family=family,
                                                     style=style).count()
            # If not, create new one
            if not similar_obj_exists:
                Font.objects.create(user=user,
                                    url=source,
                                    family=family,
                                    style=style)

    return True
