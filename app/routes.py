from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import CreditCard, User
from . import db
import logging

main = Blueprint('main', __name__)
logging.basicConfig(level=logging.INFO)

@main.route('/add_card', methods=['POST'])
@jwt_required()
def add_card():
    data = request.get_json()
    card_number = data.get('card_number')
    current_user = User.query.filter_by(username=get_jwt_identity()).first()

    if CreditCard.query.filter_by(card_number=card_number).first():
        return jsonify({'message': 'Card already exists'}), 400

    new_card = CreditCard(card_number=card_number, user=current_user)
    db.session.add(new_card)
    db.session.commit()

    logging.info(f"User {current_user.username} added card {card_number}")
    return jsonify({'message': 'Card added successfully'}), 201

@main.route('/check_card/<card_number>', methods=['GET'])
@jwt_required()
def check_card(card_number):
    card = CreditCard.query.filter_by(card_number=card_number).first()
    if card is None:
        return jsonify({'message': 'Card not found'}), 404

    logging.info(f"Card {card_number} found for user {card.user.username}")
    return jsonify({'card_id': card.id}), 200

@main.route('/add_cards_from_file', methods=['POST'])
@jwt_required()
def add_cards_from_file():
    file = request.files['file']
    current_user = User.query.filter_by(username=get_jwt_identity()).first()

    for line in file:
        card_number = line.strip()
        if not CreditCard.query.filter_by(card_number=card_number).first():
            new_card = CreditCard(card_number=card_number, user=current_user)
            db.session.add(new_card)

    db.session.commit()
    logging.info(f"User {current_user.username} added cards from file")
    return jsonify({'message': 'Cards added successfully from file'}), 201

@main.route('/add_cards_from_custom_file', methods=['POST'])
@jwt_required()
def add_cards_from_custom_file():
    file = request.files['file']
    current_user = User.query.filter_by(username=get_jwt_identity()).first()

    lines = file.readlines()
    for line in lines[1:-1]:  # Ignorar a primeira e última linha (cabeçalho e rodapé)
        if line.startswith(b'C'):
            card_number = line[7:26].strip().decode('utf-8')
            if not CreditCard.query.filter_by(card_number=card_number).first():
                new_card = CreditCard(card_number=card_number, user=current_user)
                db.session.add(new_card)

    db.session.commit()
    logging.info(f"User {current_user.username} added cards from custom file")
    return jsonify({'message': 'Cards added successfully from custom file'}), 201
