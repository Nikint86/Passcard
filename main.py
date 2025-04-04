import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    all_passcards = Passcard.objects.all()
    print(all_passcards)

    first_pascard = all_passcards[0]
    print(first_pascard.is_active)
    print(first_pascard.created_at)
    print(first_pascard.passcode)
    print(first_pascard.owner_name)

    active_passcards = Passcard.objects.filter(is_active=True)
    active_count = active_passcards.count()

    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков', active_count)
