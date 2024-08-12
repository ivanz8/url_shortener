from flask import Flask, request, render_template
import pyshorteners

app = Flask(__name__)

def generate_short_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if long_url:
            short_url = generate_short_url(long_url)
    return render_template('index.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
