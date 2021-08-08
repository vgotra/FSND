import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_access.repositories.LanguagesRepository import LanguagesRepository
from app import app
from unittest.mock import patch
from flask import json


class CapstoneAgencyTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_mapping(DEBUG=True, TESTING=True)
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_languages_all_success(self):
        """Test: Get all languages - Success"""
        with patch.object(LanguagesRepository, "get_all", return_value={"items": [{"id": 1, "name": "Ukrainian"}], "page": 1, "pages": 1, "total": 1}):
            res = self.client().get("/api/languages/")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["languages"][0]["name"], "Ukrainian")

    def test_language_by_id_success(self):
        """Test: Get language by id - Success"""
        with patch.object(LanguagesRepository, "get", return_value={"id": 1, "name": "Ukrainian"}):
            res = self.client().get("/api/languages/1")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["name"], "Ukrainian")

    def test_get_language_by_id_not_found(self):
        """Test: Get language by id - Not found"""
        with patch.object(LanguagesRepository, "get", return_value=None):
            res = self.client().get("/api/languages/1")
            self.assertEqual(res.status_code, 404)

    def test_update_language_success(self):
        """Test: Update language - Success"""
        with patch.object(LanguagesRepository, "update", return_value={"id": 1, "name": "Ukrainian"}):
            res = self.client().patch("/api/languages/1", data=json.dumps(dict({"id": 1, "name": "Ukrainian"})), content_type="application/json")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["name"], "Ukrainian")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
