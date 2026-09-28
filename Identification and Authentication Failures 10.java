import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class AuthenticationService {

    private final BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

    public boolean authenticateUser(String inputPassword, User user) {
        if (passwordEncoder.matches(inputPassword, user.getPassword())) {
            return true;
        }
        
        return false;
    }
}