import os
import django
import random
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # <-- config ni o'zingni project nomiga almashtir
django.setup()

from django.contrib.auth.models import User
from blog.models import Post  # <-- blog ni o'zingni app nomiga almashtir


def run():
    # Agar user bo'lmasa yaratamiz
    if not User.objects.exists():
        user = User.objects.create_user(
            username="admin",
            password="admin123"
        )
    else:
        user = User.objects.first()

    titles = [
        "Django nima va qanday ishlaydi?",
        "Python dasturlash asoslari",
        "REST API yaratish",
        "Django ORM bilan ishlash",
        "Frontend va Backend farqi",
        "PostgreSQL bilan ulanish",
        "Authentication tizimi",
        "Django’da ImageField ishlatish",
        "Deploy qilish yo'llari",
        "Web dasturlashni qanday boshlash kerak?"
    ]

    for i in range(10):
        Post.objects.create(
            title=titles[i],
            body="Bu test uchun yaratilgan post matni. Django project uchun seed ma'lumot.",
            image="post-image/default.jpg",  # media papkada default.jpg bo'lishi kerak
            publish=timezone.now(),
            author=user,
            status=random.choice([Post.Status.DRAFT, Post.Status.PUBLISHED])
        )

    print("✅ 10 ta post muvaffaqiyatli yaratildi!")


if __name__ == "__main__":
    run()