# app.py - ISEC3004 Integrated Vulnerable Application
# Task 12: Integration of CSRF and Log Injection Vulnerabilities
# Integrated by: Sadinya (Member 5)
# Contributors: Kristina (CSRF), Bhagya (Log Injection)

from flask import Flask, request, session, redirect, url_for, render_template_string
import logging

app = Flask(__name__)
app.secret_key = "csrf-demo-secret-key"

# ============================================================
# LOGGING SETUP (Vulnerable to Log Injection)
# ============================================================

logging.basicConfig(
    filename='app_vulnerable.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ============================================================
# DEMO USER
# ============================================================

users = {
    "student": {
        "password": "password123",
        "email": "student@example.com"
    }
}

# ============================================================
# LOGIN PAGE
# ============================================================

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>ISEC3004 Demo - Login</title></head>
<body>
    <h1>ISEC3004 Vulnerability Demonstration</h1>
    <h2>Login</h2>
    <form method="POST" action="/login">
        <label>Username:</label>
        <input type="text" name="username" required><br><br>
        <label>Password:</label>
        <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    <br>
    <p><strong>Demo credentials:</strong><br>Username: student<br>Password: password123</p>
</body>
</html>
"""

# ============================================================
# PROFILE PAGE (CSRF Target)
# ============================================================

PROFILE_PAGE = """
<!DOCTYPE html>
<html>
<head><title>CSRF Demo - Profile</title></head>
<body>
    <h1>User Profile</h1>
    <p>Logged in as: <strong>{{ username }}</strong></p>
    <p>Current email: <strong>{{ email }}</strong></p>
    <hr>
    <h2>Change Email</h2>
    
    <!--
    ==========================================================
    VULNERABLE SECTION (CSRF) - By Kristina
    ==========================================================
    This form performs a state-changing operation.
    The application does NOT generate a CSRF token and
    does NOT validate a CSRF token when this request is received.
    Therefore, a forged request can potentially cause this action 
    to be performed using the authenticated user's session.
    ==========================================================
    -->
    
    <form method="POST" action="/change-email">
        <label>New Email:</label>
        <input type="email" name="email" required>
        <button type="submit">Change Email</button>
    </form>
    <br>
    <a href="/feedback">Go to Feedback Page (Log Injection)</a> | <a href="/logout">Logout</a>
</body>
</html>
"""

# ============================================================
# FEEDBACK PAGE (Log Injection Target)
# ============================================================
FEEDBACK_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Log Injection Demo - Feedback</title></head>
<body>
    <h1>Submit Feedback</h1>
    <p>Welcome, <strong>{{ username }}</strong></p>
    <hr>
    
    <!--
    ==========================================================
    VULNERABLE SECTION (LOG INJECTION) - By Bhagya
    ==========================================================
    The user-supplied 'comment' is written STRAIGHT into the log
    message with no sanitisation. Python's logging module writes
    whatever bytes it is given verbatim, including control characters.
    
    RISK: If 'comment' contains CRLF characters (\\r\\n), the single
    intended entry is split into MULTIPLE lines on disk. An attacker
    can FORGE fake log records (log forging) — e.g. faking an admin 
    login or burying their own activity — destroying the integrity 
    of the audit trail. (CWE-117)
    ==========================================================
    -->
    
    <form method="POST" action="/feedback">
        <label>Your Comment:</label><br>
        <textarea name="comment" rows="4" cols="50" required></textarea><br><br>
        <button type="submit">Submit Feedback</button>
    </form>
    <br>
    <a href="/profile">Back to Profile</a> | <a href="/logout">Logout</a>
</body>
</html>
"""

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("profile"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username]["password"] == password:
            session["username"] = username
            logging.info(f"User logged in: {username}")
            return redirect(url_for("profile"))
        return "<h2>Invalid username or password.</h2><a href='/login'>Try Again</a>"
    return render_template_string(LOGIN_PAGE)

@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("login"))
    username = session["username"]
    return render_template_string(PROFILE_PAGE, username=username, email=users[username]["email"])

# ============================================================
# VULNERABLE CHANGE EMAIL ENDPOINT (CSRF)
# ============================================================

@app.route("/change-email", methods=["POST"])
def change_email():
    if "username" not in session:
        return "You must be logged in.", 401

    username = session["username"]
    new_email = request.form.get("email")

    if not new_email:
        return "Email address is required.", 400

    # ========================================================
    # CSRF VULNERABILITY
    # The application checks authentication but NOT CSRF token.
    # Server cannot distinguish legitimate vs forged requests.
    # ========================================================
    
    old_email = users[username]["email"]
    users[username]["email"] = new_email

    print(f"\n[CSRF] User: {username} | Old: {old_email} | New: {new_email} | CSRF Token: NOT USED\n")
    logging.info(f"Profile updated. User: {username}, New email: {new_email}")

    return f"<h1>Email Changed Successfully</h1><p>User: {username}<br>New email: {new_email}</p><a href='/profile'>Return to Profile</a>"

# ============================================================
# VULNERABLE FEEDBACK ENDPOINT (LOG INJECTION)
# ============================================================

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if "username" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        comment = request.form.get("comment")
        
        # Fixed session key to match Kristina's 'username' for consistency
        user = session.get("username", "anonymous") 
        
        # ========================================================
        # LOG INJECTION VULNERABILITY (CWE-117)
        # Direct user input concatenation in logs without sanitization.
        # RISK: Attacker can inject CRLF characters (\r\n) to forge fake log entries.
        # ========================================================
        
        logging.info(f"New feedback received from user '{user}': {comment}")
        print(f"\n[LOG INJECTION] User: {user} submitted: {comment}\n")
        
        return "<h1>Feedback Submitted!</h1><p>Thank you for your feedback.</p><a href='/profile'>Back to Profile</a>"
    
    username = session["username"]
    return render_template_string(FEEDBACK_PAGE, username=username)

@app.route("/logout")
def logout():
    username = session.get("username", "Unknown")
    logging.info(f"User logged out: {username}")
    session.clear()
    return redirect(url_for("login"))

# ============================================================
# START APPLICATION
# ============================================================
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
