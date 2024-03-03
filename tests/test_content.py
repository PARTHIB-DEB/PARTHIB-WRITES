import pytest

from content.models import *
from conftest import test_create_blog , test_update_blog

def test_count_test_create_blog(test_create_blog):
    print("Positive : Only 1 Blog")
    assert articleCreateModel.objects.count() == 1

def test_count_test_update_blog(test_update_blog):
    bg = test_update_blog
    print("Positive : Blog Tagline Updated")
    assert articleCreateModel.objects.filter(title = bg.title).tagline == ""