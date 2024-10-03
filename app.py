from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vocabulary.db'
db = SQLAlchemy(app)

# Vocabulary model
class Vocabulary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), unique=True, nullable=False)
    meaning = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Home route to render the index page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/words', methods=['GET'])
def get_words():
    words = Vocabulary.query.all()
    return jsonify({word.word: word.meaning for word in words})

@app.route('/add_word', methods=['POST'])
def add_word():
    new_word = request.json.get('word')
    meaning = request.json.get('meaning')
    word_entry = Vocabulary(word=new_word, meaning=meaning)
    db.session.add(word_entry)
    db.session.commit()
    return jsonify({'message': 'Word added'}), 201

@app.route('/update_word/<word>', methods=['PUT'])
def update_word(word):
    new_meaning = request.json.get('meaning')
    word_entry = Vocabulary.query.filter_by(word=word).first()
    if word_entry:
        word_entry.meaning = new_meaning
        db.session.commit()
        return jsonify({'message': 'Word updated'})
    return jsonify({'message': 'Word not found'}), 404

@app.route('/delete_word/<word>', methods=['DELETE'])
def delete_word(word):
    word_entry = Vocabulary.query.filter_by(word=word).first()
    if word_entry:
        db.session.delete(word_entry)
        db.session.commit()
        return jsonify({'message': 'Word deleted'})
    return jsonify({'message': 'Word not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

