from flask import Flask, render_template, session, url_for, redirect, flash
from bagelapp.form import Guess
from bagelapp import app, db
import random
from bagelapp.models import Game_play
from bagelapp.bagels_new import pico, fermi

@app.route("/")
@app.route("/home")
def home():
    return render_template("bagles.html")

@app.route("/game", methods=['GET', 'POST'])
def game_start():
    form = Guess()
    if form.validate_on_submit():
        number=str(random.randint(100,999))
        your_number= str(form.guess.data)
        if number == your_number:
            return redirect(url_for('correct_guess'))
        elif fermi(number, your_number) > 0:
            hint= "Fermi" * fermi(number, your_number)
            db.create_all()
            user = Game_play(num_guess = your_number, correct_num=number, hint=hint)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('guess_again'))
        elif pico(number, your_number) > 0:
            hint= 'Pico' * pico(number, your_number)
            db.create_all()
            user = Game_play(num_guess = your_number, correct_num=number, hint=hint)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('guess_again'))
        else: 
            db.create_all()
            user = Game_play(num_guess = your_number, correct_num=number, hint="Bagles")
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('guess_again'))
    return render_template("game_start.html", form=form)

@app.route("/guess_again", methods=['GET', 'POST'])
def guess_again():
    
    guess_counter =  [x for x in Game_play.query.all()]
    form = Guess()
    your_number= str(form.guess.data)
    correct_number = str(*Game_play.query.with_entities(db.distinct(Game_play.correct_num)).first()).rstrip(',')
    if form.validate_on_submit():
        if your_number == correct_number:
            return redirect(url_for('correct_guess'))
        else:
            if Game_play.query.get(9) != None:
                return redirect(url_for('out_of_turns'))
            elif fermi(correct_number, your_number) > 0:
                hint= "Fermi" * fermi(correct_number, your_number)
                user = Game_play(num_guess = your_number, correct_num=correct_number, hint=hint)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('guess_again'))
            elif pico(correct_number, your_number) > 0:
                hint= 'Pico' * pico(correct_number, your_number)
                user = Game_play(num_guess = your_number, correct_num=correct_number, hint=hint)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('guess_again'))
            else:
                user_guess=Game_play(num_guess = your_number, correct_num=correct_number, hint="Bagels")
                db.session.add(user_guess)
                db.session.commit()
                return redirect(url_for('guess_again'))
    return render_template("guess_again.html", guess_counter=guess_counter, form=form)

@app.route("/correct_guess")
def correct_guess():
    db.drop_all()
    return render_template("correct_guess.html")

@app.route("/out_of_turns")
def out_of_turns():
    db.drop_all()
    return render_template("out_of_turns.html")

