from bagelapp import db

class Game_play(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_guess = db.Column(db.Integer)
    correct_num = db.Column(db.Integer)
    hint = db.Column(db.String(128))

#to be able to see the correct number delete "' #" from the line below.
    def __repr__(self):
        return f'Guess Counter={self.id} Your Guess={self.num_guess} Hint={self.hint}' #Correct Answer={self.correct_num}'

