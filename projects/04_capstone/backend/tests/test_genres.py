import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_access.repositories.GenresRepository import GenresRepository
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

    def test_genres_all_success(self):
        """Test: Get all genres - Success"""
        with patch.object(GenresRepository, "get_all", return_value={"items": [{"id": 1, "name": "Test"}], "page": 1, "pages": 1, "total": 1}):
            res = self.client().get("/api/genres/")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["genres"][0]["name"], "Test")

    def test_genres_by_id_success(self):
        """Test: Get genre by id - Success"""
        with patch.object(GenresRepository, "get", return_value={"id": 1, "name": "Test"}):
            res = self.client().get("/api/genres/1")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["name"], "Test")

    def test_get_genre_by_id_not_found(self):
        """Test: Get genre by id - Not found"""
        with patch.object(GenresRepository, "get", return_value=None):
            res = self.client().get("/api/genres/1")
            self.assertEqual(res.status_code, 404)

    def test_update_genre_success(self):
        """Test: Update genre - Success"""
        with patch.object(GenresRepository, "update", return_value={"id": 1, "name": "Test"}):
            res = self.client().patch("/api/genres/1", data=json.dumps(dict({"id": 1, "name": "Test"})), content_type="application/json")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["name"], "Test")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
