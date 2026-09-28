import bcrypt

def hash_password(password: str) -> str:
    # Generate a secure, unique salt 
    password_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
    # Return the string representation for safe database storage
    return hashed_bytes.decode('utf-8')

def verify_password(stored_hash: str, password_attempt: str) -> bool:
    # Securely compare a plain text attempt against the stored hash
    return bcrypt.checkpw(password_attempt.encode('utf-8'), stored_hash.encode('utf-8'))