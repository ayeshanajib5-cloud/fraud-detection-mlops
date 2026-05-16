from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Fraud Detection API Running"
    }

def test_prediction():
    sample_data = {
        "features": [
            0.0,
            -0.425965884,
            0.960523044882985,
            1.14110934232219,
            -0.16825208,
            0.42098688077219,
            -0.029727552,
            0.476200948720027,
            0.260314333074874,
            -0.568671376,
            -0.371407197,
            1.34126198001957,
            0.359893837038039,
            -0.358090653,
            -0.1371337,
            0.517616806555742,
            0.401725895589603,
            -0.058132823,
            0.0686531494425432,
            -0.033193788,
            0.0849676720682049,
            -0.208253515,
            -0.559824796,
            -0.026397668,
            -0.371426583,
            -0.232793817,
            0.105914779097957,
            0.253844224739337,
            0.0810802569229443,
            3.67
        ]
    }

    response = client.post("/predict", json=sample_data)

    assert response.status_code == 200