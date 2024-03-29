from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Abraam Benitez!! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite-course')
def favorite_course():
    print('subject: ' + request.args.get("subject"))
    print('course_number: ' + request.args.get("course_number"))

    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_subitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
