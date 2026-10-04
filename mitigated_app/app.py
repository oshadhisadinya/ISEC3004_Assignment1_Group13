from flask import Flask, request, session, redirect, url_for, render_template_string, abort
import secrets
import logging

app = Flask(__name__)

# Secret key used by Flask to manage sessions.
app.secret_key = "csrf-demo-secret-key"

# ============================================================
# SECURE LOGGING SETUP
# ============================================================
logging.basicConfig(
    filename="app_mitigated.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
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
# LOG INJECTION MITIGATION (CWE-117)
# ============================================================
def sanitize_log_value(value):
    """
    Neutralize CR and LF characters before writing user-controlled
    data to a log. Escaping them preserves the evidence while ensuring
    that the input remains on one physical log line.
    """
    if value is None:
        return ""
    return str(value).replace("\r", "\\r").replace("\n", "\\n")

# ============================================================
# LOGIN PAGE
# ============================================================
LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Secure App - Login</title></head>
<body>
    <h1>Secure Application (Mitigated)</h1>
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
# PROFILE PAGE (CSRF MITIGATED)
# ============================================================
PROFILE_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Secure App - Profile</title></head>
<body>
    <h1>User Profile</h1>
    <p>Logged in as: <strong>{{ username }}</strong></p>
    <p>Current email: <strong>{{ email }}</strong></p>
    <hr>
    <h2>Change Email</h2>
    
    <!-- CSRF MITIGATION: Synchronizer Token Pattern -->
    <form method="POST" action="/change-email">
        <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
        <label>New Email:</label>
        <input type="email" name="email" required>
        <button type="submit">Change Email</button>
    </form>
    <br>
    <a href="/feedback">Go to Feedback Page (Log Injection Test)</a> | 
    <a href="/logout">Logout</a>
</body>
</html>
"""

# ============================================================
# FEEDBACK PAGE (LOG INJECTION MITIGATED)
# ============================================================
FEEDBACK_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Secure App - Feedback</title></head>
<body>
    <h1>Submit Feedback</h1>
    <p>Welcome, <strong>{{ username }}</strong></p>
    <hr>
    <!-- User feedback is sanitized on the server before logging. -->
    <form method="POST" action="/feedback">
        <label>Your Comment:</label><br>
        <textarea name="comment" rows="4" cols="50" required></textarea><br><br>
        <button type="submit">Submit Feedback</button>
    </form>
    <br>
    <a href="/profile">Back to Profile</a> | 
    <a href="/logout">Logout</a>
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
            session["csrf_token"] = secrets.token_urlsafe(32)
            return redirect(url_for("profile"))
        return "<h2>Invalid username or password.</h2><a href='/login'>Try Again</a>"
    
    return render_template_string(LOGIN_PAGE)

@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("login"))
    
    username = session["username"]
    return render_template_string(
        PROFILE_PAGE,
        username=username,
        email=users[username]["email"],
        csrf_token=session["csrf_token"]
    )

# ============================================================
# SECURITY-ENHANCED CHANGE EMAIL ENDPOINT (CSRF MITIGATED)
# ============================================================
@app.route("/change-email", methods=["POST"])
def change_email():
    if "username" not in session:
        return "You must be logged in.", 401

    username = session["username"]
    submitted_token = request.form.get("csrf_token")
    session_token = session.get("csrf_token")

    # CSRF Protection Check
    if not submitted_token or not session_token or not secrets.compare_digest(submitted_token, session_token):
        print("\n========================================")
        print("CSRF ATTACK BLOCKED")
        print(f"User: {username} | Reason: Missing or invalid CSRF token")
        print("========================================\n")
        abort(403)

    new_email = request.form.get("email")
    if not new_email:
        return "Email address is required.", 400

    old_email = users[username]["email"]
    users[username]["email"] = new_email

    print("\n========================================")
    print("EMAIL CHANGE REQUEST ACCEPTED")
    print(f"User: {username} | New email: {new_email} | CSRF token: VALID")
    print("========================================\n")

    return f"<h1>Email Changed Successfully</h1><p>User: {username}<br>New email: {new_email}</p><a href='/profile'>Return to Profile</a>"

# ============================================================
# SECURITY-ENHANCED FEEDBACK ENDPOINT (LOG INJECTION MITIGATED)
# ============================================================
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        comment = request.form.get("comment")
        if not comment:
            return "Feedback comment is required.", 400

        user = session.get("username", "anonymous")

        # Mitigation: Neutralize CR and LF characters
        safe_user = sanitize_log_value(user)
        safe_comment = sanitize_log_value(comment)

        logging.info("New feedback received from user '%s': %s", safe_user, safe_comment)
        print(f"\n[LOG INJECTION MITIGATED] User: {safe_user} submitted: {safe_comment}\n")

        return "<h1>Feedback Submitted Safely!</h1><p>Your feedback was recorded using secure log handling.</p><a href='/profile'>Back to Profile</a>"

    return render_template_string(FEEDBACK_PAGE, username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)