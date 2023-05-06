from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Weight
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note_data')  # updated the field name to match the HTML
        weight = request.form.get('weight_data')
        weight_lifted = request.form.get('weight_lifted')
        if note and len(note) < 1:
            flash('Note is too short!', category='error')
        elif weight and len(weight) < 1:
            flash('Weight is required!', category='error')
        else:
            if note:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
            if weight:
                new_weight = Weight(weight_data=weight, weight_lifted=weight_lifted, user_id=current_user.id)
                db.session.add(new_weight)
            db.session.commit()
            flash('Information added!', category='success')
    return render_template("home.html", user=current_user)

def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})



