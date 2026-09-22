# app.py - ISEC3004 Vulnerable Flask Application
# Phase 2: Vulnerable Code Development


from flask import Flask, request, session, redirect, url_for
import logging

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_demo_only'

# ==========================================
# LOGGING SETUP
# ==========================================
logging.basicConfig(
    filename='app_vulnerable.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route('/')
def home():
    if 'user' not in session:
        return '''
            <h1>ISEC3004 Vulnerable App</h1>
            <a href="/login">Login as Victim</a>
        '''
    return f'''
        <h1>Welcome, {session['user']}!</h1>
        <a href="/profile">1. Update Profile (CSRF Target)</a><br><br>
        <a href="/feedback">2. Submit Feedback (Log Injection Target)</a><br><br>
        <a href="/logout">Logout</a>
    '''

@app.route('/login')
def login():
    session['user'] = 'victim_user'
    session['email'] = 'victim@example.com'
    return redirect(url_for('home'))

# ==========================================
# CSRF VULNERABLE ROUTE (Kristina's Task)
# ==========================================
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_email = request.form.get('email')
        
        # TODO: KRISTINA - Add CSRF vulnerable code here
        # EXAMPLE:
        # VULNERABILITY: No CSRF token validation
        # RISK: Attacker can forge requests to change user email without authorization
        session['email'] = new_email
        logging.info(f"Profile updated. New email: {new_email}")
        
        return f'''
            <h1>Profile Updated!</h1>
            <p>Your new email is: {new_email}</p>
            <a href="/">Home</a>
        '''
    
    current_email = session.get('email', 'victim@example.com')
    return f'''
        <h1>Update Profile</h1>
        <form method="POST">
            <label>Email:</label><br>
            <input type="email" name="email" value="{current_email}" required><br><br>
            <button type="submit">Update Email</button>
        </form>
        <a href="/">Home</a>
    '''

# ==========================================
# LOG INJECTION VULNERABLE ROUTE (Bhagya's Task)
# ==========================================
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        comment = request.form.get('comment')
        
        # TODO: BHAGYA - Add Log Injection vulnerable code here
        # EXAMPLE:
        # VULNERABILITY: Direct user input concatenation in logs
        # RISK: Attacker can inject CRLF characters (\r\n) to forge fake log entries
        logging.info(f"User Feedback: {comment}")
        
        return '''
            <h1>Feedback Submitted!</h1>
            <p>Thank you for your feedback.</p>
            <a href="/">Home</a>
        '''
    
    return '''
        <h1>Submit Feedback</h1>
        <form method="POST">
            <label>Your Comment:</label><br>
            <textarea name="comment" rows="4" cols="50" required></textarea><br><br>
            <button type="submit">Submit</button>
        </form>
        <a href="/">Home</a>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)