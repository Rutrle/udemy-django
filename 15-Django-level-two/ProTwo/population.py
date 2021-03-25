from faker import Faker
import os
import django

fakegen = Faker()


def populate(N=5):
    for fake_user in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user_rec = User.objects.get_or_create(
            first_name=fake_first_name, second_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ProTwo.settings")

    django.setup()
    from AppTwo.models import User
    populate(20)
    print("population completed!")
