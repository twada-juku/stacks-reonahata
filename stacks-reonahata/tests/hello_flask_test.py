from stacks import create_app
import pytest

@pytest.fixture
def client():
    test_app = create_app({'TESTING': True})
    with test_app.test_client() as client:
        yield client

@pytest.mark.learning
def test_パラメータなしでappを作成():
    default_app = create_app()
    assert default_app.testing == False

@pytest.mark.learning
def test_TESTINGパラメータを与えて作成():
    testing_app = create_app({'TESTING': True})
    assert testing_app.testing == True

@pytest.mark.learning
def test_GETリクエストとテンプレートHTMLの動作確認(client):
    resp = client.get('/hello')
    body = resp.get_data(as_text=True)
    print(str(body))  #動作確認用に一時的に標準出力に出してみる
    assert 'Hello, Flask!' in body
