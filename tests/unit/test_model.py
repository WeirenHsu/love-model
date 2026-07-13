from app.model import MODEL_VERSION, predict


def test_predict_returns_i_love_you():
    assert predict("hello") == "I Love You"


def test_predict_is_deterministic():
    assert predict("a") == predict("a")


def test_model_version_format():
    assert MODEL_VERSION.count(".") == 2
