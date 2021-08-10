import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_access.repositories.LanguagesRepository import LanguagesRepository
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

    @patch.object(LanguagesRepository, "get_all", return_value={"items": [{"id": 1, "name": "Ukrainian"}], "page": 1, "pages": 1, "total": 1})
    def test_get_languages_all_success(self, repo):
        res = self.client().get("/api/languages/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["languages"][0]["name"], "Ukrainian")

    @patch.object(LanguagesRepository, "get_all")
    def test_get_languages_all_error(self, repo):
        repo.side_effect = Exception()
        res = self.client().get("/api/languages/")
        self.assertEqual(res.status_code, 500)

    @patch.object(LanguagesRepository, "get", return_value={"id": 1, "name": "Ukrainian"})
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_get_language_by_id_success(self, auth, repo):
        res = self.client().get("/api/languages/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["name"], "Ukrainian")

    @patch.object(LanguagesRepository, "get", return_value={"id": 1, "name": "Ukrainian"})
    def test_get_language_by_id_not_found(self, repo):
        res = self.client().get("/api/languages/1")
        self.assertEqual(res.status_code, 401)

    @patch.object(LanguagesRepository, "update", return_value={"id": 1, "name": "Ukrainian"})
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_update_language_success(self, auth, repo):
        res = self.client().patch("/api/languages/1", data=json.dumps(dict({"id": 1, "name": "Ukrainian"})), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["name"], "Ukrainian")

    @patch.object(LanguagesRepository, "update", return_value={"id": 1, "name": "Ukrainian"})
    def test_update_language_error(self, repo):
        res = self.client().patch("/api/languages/1", data=json.dumps(dict({"id": 1, "name": "Ukrainian"})), content_type="application/json")
        self.assertEqual(res.status_code, 401)

    @patch.object(LanguagesRepository, "create", return_value={"id": 1, "name": "Ukrainian"})
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_create_language_success(self, auth, repo):
        res = self.client().put("/api/languages/", data=json.dumps(dict({"id": 1, "name": "Ukrainian"})), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["name"], "Ukrainian")

    @patch.object(LanguagesRepository, "create", return_value={"id": 1, "name": "Ukrainian"})
    def test_create_language_error(self, repo):
        res = self.client().put("/api/languages/", data=json.dumps(dict({"id": 1, "name": "Ukrainian"})), content_type="application/json")
        self.assertEqual(res.status_code, 401)

    @patch.object(LanguagesRepository, "delete", return_value=1)
    @patch.object(AuthService, "check_permissions", return_value=True)
    def test_delete_language_success(self, auth, repo):
        res = self.client().delete("/api/languages/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["id"], 1)

    @patch.object(LanguagesRepository, "delete", return_value=1)
    def test_delete_language_error(self, repo):
        res = self.client().delete("/api/languages/1")
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
