from flask import Flask, render_template, url_for, request
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/entry_level_1')
def entry_level_1():
    episodes = queries.entry_level_1()
    for episode in episodes:
        if episode['episodes'] > 99:
            episode['is_long'] = True
        else:
            episode['is_long'] = False
    return render_template('entry_level_1.html', episodes=episodes)


@app.route('/entry_level_2')
def entry_level_2():
    data = queries.entry_level_2()
    data[0]['name'] = data[0]['name'] + " 🥇"
    data[1]['name'] = data[1]['name'] + " 🥈"
    data[2]['name'] = data[2]['name'] + " 🥉"
    all_count = 0
    for person in data:
        all_count = all_count + person['counts']
    return render_template('entry_level_2.html', data=data, roles=all_count)


@app.route('/entry_level_3', methods=['GET', 'POST'])
def entry_level_3():
    if request.method == 'POST':
        data = ""
        season = request.form['season']
        episode = request.form['episode']
        print(season, episode)
        data = queries.entry_level_3(season, episode)
        return render_template('entry_level_3.html', data=data)
    return render_template('entry_level_3.html', data=None)


@app.route('/pa_1', methods=['GET', 'POST'])
def pa_1():
    if request.method == 'POST':
        genre = request.form['genre']
        data = queries.pa_1(genre)
        return render_template('pa_1.html', data=data)
    return render_template('pa_1.html', data=None)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()

