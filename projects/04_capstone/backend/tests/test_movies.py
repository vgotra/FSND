import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_access.repositories.MoviesRepository import MoviesRepository
from auth import AuthService
from app import app
from unittest.mock import patch
from flask import json
from data_access.exceptions.NotFound import NotFound


class CapstoneAgencyTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_mapping(DEBUG=True, TESTING=True)
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        pass

    @patch.object(MoviesRepository, "get_all", return_value={"items": [{"id": 1, "name": "Test"}], "page": 1, "pages": 1, "total": 1})
    def test_get_movies_all_success(self, repo):
        res = self.client().get("/api/movies/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["movies"][0]["name"], "Test")

    @patch.object(MoviesRepository, "get_all")
    def test_get_movies_all_error(self, repo):
        repo.side_effect = Exception()
        res = self.client().get("/api/movies/")
        self.assertEqual(res.status_code, 500)

    @patch.object(MoviesRepository, "get", return_value={"id": 1, "name": "Test"})
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_get_movie_by_id_success(self, auth, repo):
        res = self.client().get("/api/movies/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["name"], "Test")

    @patch.object(MoviesRepository, "get", return_value={"id": 1, "name": "Test"})
    def test_get_movie_by_id_not_found(self, repo):
        res = self.client().get("/api/movies/1")
        self.assertEqual(res.status_code, 401)

    @patch.object(MoviesRepository, "update", return_value={"id": 1, "name": "Test"})
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_update_movie_success(self, auth, repo):
        res = self.client().patch("/api/movies/1", data=json.dumps(dict({"id": 1, "name": "Test"})), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["name"], "Test")

    @patch.object(MoviesRepository, "update", return_value={"id": 1, "name": "Test"})
    def test_update_movie_error(self, repo):
        res = self.client().patch("/api/movies/1", data=json.dumps(dict({"id": 1, "name": "Test"})), content_type="application/json")
        self.assertEqual(res.status_code, 401)

    @patch.object(MoviesRepository, "create", return_value={"id": 1, "name": "Test"})
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_create_movie_success(self, auth, repo):
        res = self.client().put("/api/movies/", data=json.dumps(dict({"id": 1, "name": "Test"})), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["name"], "Test")

    @patch.object(MoviesRepository, "create", return_value={"id": 1, "name": "Test"})
    def test_create_movie_error(self, repo):
        res = self.client().put("/api/movies/", data=json.dumps(dict({"id": 1, "name": "Test"})), content_type="application/json")
        self.assertEqual(res.status_code, 401)

    @patch.object(MoviesRepository, "delete", return_value=1)
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_delete_movie_success(self, auth, repo):
        res = self.client().delete("/api/movies/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["id"], 1)

    @patch.object(MoviesRepository, "delete", return_value=1)
    def test_delete_movie_error(self, repo):
        res = self.client().delete("/api/movies/1")
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
