import pytest
from content.models import articleCreateModel
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def image_fixture(db):
    """Creates a SimpleUploadedFile object for testing."""
    image_path = "static/c.png"  # Replace with your actual image path
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    return SimpleUploadedFile("c.png", image_data, content_type="image/png")

@pytest.fixture
def test_create_blog(db, image_fixture):
    """Creates a blog object with a thumbnail image for testing."""
    blog = articleCreateModel.objects.create(
        title="Python",
        tagline="About Python Programming",
        thumbnail=image_fixture
    )
    yield blog  # Allow for interaction with the fixture instance within tests
    blog.delete()  # Ensure model instance is cleaned up after the test

@pytest.fixture
def test_update_blog(db,test_create_blog):
    blog = test_create_blog
    articleCreateModel.objects.filter(title = blog.title).update(tagline="")
    