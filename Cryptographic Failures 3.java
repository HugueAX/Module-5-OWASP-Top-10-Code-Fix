import org.mindrot.jbcrypt.BCrypt;

public String hashPasswordSecure(String password) {
    // Generate a salt
    String salt = BCrypt.gensalt(12);
    
    // Hash the password along with the generated salt
    return BCrypt.hashpw(password, salt);
}

public boolean verifyPassword(String password, String storedHash) {
    // Safely check if the plaintext password matches the stored hash
    return BCrypt.checkpw(password, storedHash);
}