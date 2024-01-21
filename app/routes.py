from flask import Blueprint, render_template, request, jsonify
from app.summarizer import extractive_summarization

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        data = request.get_json()
        paragraph = data['paragraph']
        summary = extractive_summarization(paragraph)
        return jsonify({'summary': summary})
