import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Set a secret key for sessions and cookies
app.config['SECRET_KEY'] = os.urandom(24)  # Generates a random 24-byte key

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_description = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default="Open")  # Default status will be 'Open'

    def __repr__(self):
        return f"<Ticket {self.id} - {self.priority}>"


# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Hardcoded admin user for simplicity
admin_user = User(username='admin', password='password')


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Ensure user_id is valid (an integer)
    if user_id is None:
        return None
    return User.query.get(int(user_id))



# Create the database and tables
with app.app_context():
    db.create_all()

# Create the database and tables
with app.app_context():
    db.create_all()

    # Check if the admin user already exists, and if not, add it
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', password='password')
        db.session.add(admin_user)
        db.session.commit()

    # Add a sample ticket (for testing purposes)
    if not Ticket.query.first():
        sample_ticket = Ticket(issue_description="Internet not working", priority="High")
        db.session.add(sample_ticket)
        db.session.commit()



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Fetch the user from the database
        user = User.query.filter_by(username=username).first()

        # Check if the user exists and the password matches
        if user and user.password == password:
            login_user(user)  # Log the user in using Flask-Login
            return redirect(url_for('admin_dashboard'))

    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@login_required
def index():
    # Get all tickets from the database
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)


@app.route('/admin')
@login_required
def admin_dashboard():
    tickets = Ticket.query.all()
    return render_template('admin.html', tickets=tickets)



@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    # Get form data
    issue_description = request.form['issue_description']
    priority = request.form['priority']

    # Create a new Ticket object and store it in the database
    new_ticket = Ticket(issue_description=issue_description, priority=priority)
    db.session.add(new_ticket)
    db.session.commit()

    # Redirect to the homepage after submission
    return redirect('/')


@app.route('/update_ticket_status/<int:ticket_id>', methods=['POST'])
def update_ticket_status(ticket_id):
    ticket = Ticket.query.get(ticket_id)  # Get the ticket by ID

    # If the ticket doesn't exist, redirect to homepage
    if not ticket:
        return redirect('/')

    # Get the new status from the form
    new_status = request.form['status']

    # Update the ticket's status
    ticket.status = new_status
    db.session.commit()

    # Redirect to the homepage to see the updated status
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)