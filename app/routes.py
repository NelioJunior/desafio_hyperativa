import unittest
from app import create_app, db
from app.models import User, CreditCard
from flask_jwt_extended import create_access_token
import io

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='testuser')
            user.set_password('password')
            db.session.add(user)
            db.session.commit()
            self.access_token = create_access_token(identity='testuser')

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_card(self):
        response = self.client.post('/add_card', json={
            'card_number': '1234567812345678'
        }, headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 201)

    def test_check_card(self):
        card = CreditCard(card_number='1234567812345678', user_id=1)
        with self.app.app_context():
            db.session.add(card)
            db.session.commit()
        response = self.client.get('/check_card/1234567812345678', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)

    def test_add_cards_from_file(self):
        data = {
            'file': (io.BytesIO(b"1234567812345678\n8765432187654321"), 'cards.txt')
        }
        response = self.client.post('/add_cards_from_file', content_type='multipart/form-data', headers={
            'Authorization': f'Bearer {self.access_token}'
        }, data=data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
