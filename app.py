from flask import Flask, render_template


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'description': 'Work on the Google Search Engine'
    },
    {
        'id': 2,
        'title': 'Cyber Security Engineer',
        'company': 'Facebook',
        'location': 'Menlo Park, CA',
        'description': 'Work on the Facebook Social Network'
    },
    {
        'id': 3,
        'title': 'Mobile App Developer',
        'company': 'Apple',
        'location': 'Cupertino, CA',
        'description': 'Work on the Apple iPhone'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(debug=True)
