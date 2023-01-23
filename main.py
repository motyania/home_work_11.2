from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)
path = "candidates.json"
data = load_candidates_from_json(path)


@app.route('/')
def index_page():
    return render_template('list.html', items=data)


@app.route('/candidate/<int:uid>')
def candidate_card(uid):
    canditate = get_candidate(data, uid)
    return render_template('card.html', items=canditate)


@app.route('/search/<candidate_name>')
def candidates_by_name(candidate_name):
    canditate = get_candidates_by_name(data, candidate_name)
    n = len(canditate)
    return render_template('search.html', items=canditate, n=n)


@app.route('/skill/<skill_name>')
def candidates_by_skill(skill_name):
    canditate = get_candidates_by_skill(data, skill_name)
    n = len(canditate)
    return render_template('skill.html', items=canditate, n=n, skill=skill_name)


app.run()
