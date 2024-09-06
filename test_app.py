import unittest
from flask import Flask
from app import app  

class FlaskTestCase(unittest.TestCase):
    # Configuration initiale avant chaque test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test de la route GET (formulaire)
    def test_get_form(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form', response.data)  # Vérifie que le formulaire est bien présent dans la page HTML

    # Test de la route POST avec une requête valide
    def test_post_form_valid(self):
        # Simule une requête POST avec un texte de test
        response = self.app.post('/', data={'text': 'This is a test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'result', response.data)  # Vérifie que le résultat est présent dans la réponse
        self.assertIn(b'This is a test', response.data)  # Vérifie que le texte soumis est bien dans la réponse

    # Test de la route POST avec une requête vide
    def test_post_form_empty(self):
        # Simule une requête POST avec un texte vide
        response = self.app.post('/', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'result', response.data)  # Vérifie que le résultat est bien traité même si le texte est vide

if __name__ == '__main__':
    unittest.main()
