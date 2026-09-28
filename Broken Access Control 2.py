@app.route('/account/<int:user_id>')
@login_required # Ensure the user is authenticated first
def get_account(user_id):
    # 1. Authorization Check: Compare requested object ID with session ID
    if current_user.id != user_id and not current_user.is_admin:
        # Fail securely: Return a 403 Forbidden or 404 Not Found to prevent enumeration
        abort(403)
        
    # 2. Database Fetch
    user = db.query(User).filter_by(id=user_id).first()
    
    if not user:
        abort(404)
        
    return jsonify(user.to_dict())