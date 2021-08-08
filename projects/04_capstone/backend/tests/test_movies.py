import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_access.repositories.MoviesRepository import MoviesRepository
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

    def test_movies_all_success(self):
        """Test: Get all movies - Success"""
        with patch.object(MoviesRepository, "get_all", return_value={"items": [{"id": 1, "name": "Test"}], "page": 1, "pages": 1, "total": 1}):
            res = self.client().get("/api/movies/")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["movies"][0]["name"], "Test")

    def test_movies_by_id_success(self):
        """Test: Get movie by id - Success"""
        with patch.object(MoviesRepository, "get", return_value={"id": 1, "name": "Test"}):
            res = self.client().get("/api/movies/1")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["name"], "Test")

    def test_get_movie_by_id_not_found(self):
        """Test: Get movie by id - Not found"""
        with patch.object(MoviesRepository, "get", return_value=None):
            res = self.client().get("/api/movies/1")
            self.assertEqual(res.status_code, 404)

    def test_update_movie_success(self):
        """Test: Update movie - Success"""
        with patch.object(MoviesRepository, "update", return_value={"id": 1, "name": "Test"}):
            res = self.client().patch("/api/movies/1", data=json.dumps(dict({"id": 1, "name": "Test"})), content_type="application/json")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.json["name"], "Test")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
