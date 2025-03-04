from app import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),unique= True, nullable = False)    
    password = db.Column(db.String(200),unique= True, nullable = False) 
    fullName = db.Column(db.String(100),unique= True, nullable = False)
    qualification = db.Column(db.String(80),unique= True, nullable = False)
    dob = db.Column(db.String) 

    scores = db.relationship('Score', backref = 'user', lazy = True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)

    chapters = db.relationship('Chapter', backref = 'subject', lazy = True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)
    
    chapters = db.relationship('Chapter', backref='subject', lazy=True)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable = False)

    quizzes = db.relationship('Quiz', backref = 'chapter', lazy = True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_of_quiz = db.Column(db.DateTime)
    time_duration = db.Column(db.Integer, nullable = False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable = False)
    
    questions = db.relationship('Questions', backref = 'quiz', lazy = True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    question_statement = db.Column(db.Text)
    option1 = db.Column(db.String(200))
    option2 = db.Column(db.String(200))
    option3 = db.Column(db.String(200))
    option4 = db.Column(db.String(200))
    correct_option = db.Column(db.Integer, nullable = False)

    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable = False)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    total_scored = db.Column(db.Integer, nullable = False)
    timeStamp = db.Column(db.DateTime, default = db.func.current_timestamp())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable = False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

