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
        exercise = request.form.get('exercise')
        # updated the field name to match the HTML
        note = request.form.get('note_data')
        weight = request.form.get('weight')
        sets = request.form.get('sets')
        reps = request.form.get('reps')

        if note and len(note) < 1:
            flash('Note is too short!', category='error')
        elif not exercise:
            flash('Please select an exercise!', category='error')
        elif not weight:
            flash('Please enter the weight lifted!', category='error')
        elif not sets:
            flash('Please enter the number of sets!', category='error')
        elif not reps:
            flash('Please enter the number of reps!', category='error')

        else:
            new_weight = Weight(exercise=exercise, weight_lifted=int(weight), sets=int(sets), reps=int(reps), user_id=current_user.id)
            db.session.add(new_weight)
            db.session.commit()
            flash('Weight added!', category='success')
            if note:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
            db.session.commit()
            flash('Information added!', category='success')
            
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # this function expects a JSON from the INDEX.js file
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
