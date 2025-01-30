import pytest

from blog.factories import PostFactory

@pytest.fixture #fixture possui diversos objetivos, um dos principais é não repetir codigo, podemos reutilizar a fixture.
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published): #funão de teste
    assert post_published.title == 'pytest with factory' #asserção pra ver se é igual ao que definimos
