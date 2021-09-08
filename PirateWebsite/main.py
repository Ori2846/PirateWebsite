from flask import Flask, render_template, send_file
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/AOT')
def index2():
    options = os.listdir(r"I:/PirateWebsite/PirateWebsite/static/Series/AOT")
    forward_message = "Moving Forward..."
    return render_template('AOT.html', options = options,forward_message=forward_message)
@app.route('/AOT/<path:filename>')
def download2(filename):
    return render_template('videoplayer.html', filename="Series/AOT/"+filename)
@app.route('/downloadAOT/<path:filename>')
def download3(filename):
    return send_file('I:/PirateWebsite/PirateWebsite/static/Series/AOT/' + filename, as_attachment=True)
@app.route('/RickAndMorty')
def indexRAM():
    options = os.listdir(r"I:/PirateWebsite/PirateWebsite/static/Series/RickAndMorty")
    forward_message = "Moving Forward..."
    return render_template('RickAndMorty.html', options = options,forward_message=forward_message)
@app.route('/RAM/<path:filename>')
def downloadRAM(filename):
    return render_template('videoplayer.html', filename="Series/RickAndMorty/"+filename)
@app.route('/downloadRAM/<path:filename>')
def downloadRAM2(filename):
    return send_file('I:/PirateWebsite/PirateWebsite/static/Series/RickAndMorty/' + filename, as_attachment=True)
@app.route('/SpongebobMovie')
def indexSpongebobMovie():
    options = os.listdir(r"I:/PirateWebsite/PirateWebsite/static/Series/SpongebobMovie")
    forward_message = "Moving Forward..."
    return render_template('SpongebobMovie.html', options = options,forward_message=forward_message)
@app.route('/SpongebobMovie/<path:filename>')
def downloadSpongebobMovie(filename):
    return render_template('videoplayer.html', filename="Series/SpongebobMovie/"+filename)
@app.route('/downloadSpongebobMovie/<path:filename>')
def downloadSpongebobMovie2(filename):
    return send_file('I:/PirateWebsite/PirateWebsite/static/Series/SpongebobMovie/' + filename, as_attachment=True)
@app.route('/Spongebob')
def indexSpongebob():
    options = os.listdir(r"I:/PirateWebsite/PirateWebsite/static/Series/Spongebob")
    forward_message = "Moving Forward..."
    return render_template('Spongebob.html', options = options,forward_message=forward_message)
@app.route('/Spongebob/<path:filename>')
def downloadSpongebob(filename):
    return render_template('videoplayer.html', filename="Series/Spongebob/"+filename)
@app.route('/downloadSpongebob/<path:filename>')
def downloadSpongebob2(filename):
    return send_file('I:/PirateWebsite/PirateWebsite/static/Series/Spongebob/' + filename, as_attachment=True)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="65001")