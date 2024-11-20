from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title="AdventureQuest Builder")

@main.route('/start')
def start():
    return render_template('start.html', title="Start Your Journey")


@main.route('/castle')
def castle():
    return render_template('castle.html', title="Haunted Castle")

@main.route('/forest')
def forest():
    return render_template('forest.html', title="Dark Forest")