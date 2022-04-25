import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from django_app.models import AccessRecord, WebPage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    # get_or_create will return a tuple and the first object will reference to the model instance

    topic.save()
    return topic


def populateAccessRecords(N=5):
    for entry in range(N):
        # Get the topic for the entry
        topic = add_topic()

        # Create a fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new webpage entry
        webpage = WebPage.objects.get_or_create(
            topic=topic, url=fake_url, name=fake_name)[0]

        # Create a fake access record for the webpage
        access_record = AccessRecord.objects.get_or_create(
            name=webpage, date=fake_date)[0]


def populateUsers(N=10):
    for entry in range(N):
        fake_first_name = fakegen.unique.first_name()
        fake_last_name = fakegen.unique.last_name()
        email = f'{fake_first_name.lower()}{fake_last_name.lower()}@{fakegen.domain_name()}'

        user = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=email)[0]


if __name__ == '__main__':
    print('POPULATING SCRIPT!')
    populateAccessRecords(20)
    populateUsers(50)
    print('POPULATING COMPLETE!')
