from flask import Blueprint, render_template, session, request


main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Pass stats to the home page
    stats = {
        'health': session.get('health', 100),  # Default health is 100
        'mana': session.get('mana', 50),      # Default mana is 50
        'gold': session.get('gold', 10),      # Default gold is 10
        'inventory': session.get('inventory', [])
    }
    return render_template('index.html', stats=stats)
    # return render_template('index.html', title="AdventureQuest Builder")

@main.route('/start', methods=['GET'])
def start():
    # Initialize session values if not already present
    session['health'] = session.get('health', 100)
    session['mana'] = session.get('mana', 50)
    session['strength'] = session.get('strength', 10)

    return render_template('start.html', stats=session)



@main.route('/castle', methods=['GET', 'POST'])
def castle():
    if request.method == 'POST':
        session['health'] -= 10
        session['gold'] += 5
    return render_template('castle.html', title="Haunted Castle", stats=session)

@main.route('/forest', methods=['GET', 'POST'])
def forest():
    if request.method == 'POST':
        session['health'] -= 10
        session['gold'] += 5
    return render_template('forest.html', title="Dark Forest", stats=session)


# @main.route('/riddle', methods=['GET', 'POST'])
# def riddle():
#     if request.method == 'POST':
#         answer = request.form.get('answer', '').lower()
#         if answer == "shadow":
#             session['gold'] += 10
#             message = "Correct! You earned 10 gold."
#         else:
#             session['health'] -= 5
#             message = "Wrong answer! You lost 5 health."
#         return render_template('riddle_result.html', message=message, stats=session)
#     return render_template('riddle.html', title="Solve the Riddle", stats=session)

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.route('/castle/riddle', methods=['GET', 'POST'])
def castle_riddle():
    if request.method == 'POST':
        answer = request.form.get('answer', '').lower()
        if answer == "candle":
            session['gold'] += 15
            message = "Correct! You earned 15 gold."
        else:
            session['health'] -= 10
            message = "Wrong answer! You lost 10 health."
        return render_template('riddle_result.html', message=message, stats=session)
    return render_template('riddle.html', title="Castle Riddle", stats=session, riddle="I am tall when I’m young, and short when I’m old. What am I?")


@main.route('/forest/riddle', methods=['GET', 'POST'])
def forest_riddle():
    if request.method == 'POST':
        answer = request.form.get('answer', '').lower()
        if answer == "echo":
            session['gold'] += 15
            message = "Correct! You earned 15 gold."
        else:
            session['health'] -= 10
            message = "Wrong answer! You lost 10 health."
        return render_template('riddle_result.html', message=message, stats=session)
    return render_template('riddle.html', title="Forest Riddle", stats=session, riddle="I speak without a mouth and hear without ears. What am I?")
