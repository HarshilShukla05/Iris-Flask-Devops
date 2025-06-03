import unittest
import json
from app.main import app

class PredictEndpointTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_predict_valid_input(self):
        payload = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        response = self.client.post("/predict", data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("predicted_species", data)
        self.assertIn(data["predicted_species"], ["setosa", "versicolor", "virginica"])

    def test_predict_missing_feature(self):
        payload = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4
            # missing petal_width
        }
        response = self.client.post("/predict", data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()
