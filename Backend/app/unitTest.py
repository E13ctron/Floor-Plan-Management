import unittest
from app import app

class TestUploadFloorPlan(unittest.TestCase):

    def test_upload_floor_plan(self):
        client = app.test_client()
        response = client.post('/upload-floor-plan', data={'file': 'test_floor_plan.pdf'})
        self.assertEqual(response.status_code, 201)
