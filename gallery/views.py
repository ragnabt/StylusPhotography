from django.shortcuts import render
import random
from faker import Faker
from datetime import datetime

fake = Faker()


# Create your views here.


def create_photo():
    categories = ["nature", "cities", "wedding", 'beach']
    category = random.choice(categories)
    title = fake.sentence()
    description = fake.text
    return {
        "title": title,
        "category": category,
        "image": f"https://source.unsplash.com/1600x900/?{category}{random.randint(1, 1000)}",
        "description": description,
        "creation_date": datetime.now(),
    }


def gallery_view(request):
    photos = [create_photo() for i in range(18)]
    return render(request, 'gallery/gallery_home.html', {"photos": photos})


