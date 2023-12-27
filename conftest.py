import pytest

@pytest.fixture(params=["firefox", "chrome"])
def browser(request, test_class_instance):
    test_class_instance.browser_name = request.param
