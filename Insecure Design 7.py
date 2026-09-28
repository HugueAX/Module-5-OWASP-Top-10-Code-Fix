import secrets
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    
    generic_message = "If that email exists, a reset link has been sent."
    
    if user:
        token = secrets.token_urlsafe(32)
        user.reset_token = token
        user.token_expiry = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        
        
    return generic_message

@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    new_password = request.form['new_password']
    
    user = User.query.filter_by(reset_token=token).first()
    if not user or user.token_expiry < datetime.utcnow():
        return 'Invalid or expired token', 400
        
    user.password_hash = generate_password_hash(new_password, method='scrypt')
    
    user.reset_token = None
    user.token_expiry = None
    db.session.commit()
    
    return 'Password has been reset successfully'