String username = request.getParameter("username");

String query = "SELECT * FROM users WHERE username = ?";

try (PreparedStatement pstmt = connection.prepareStatement(query)) {
    
    pstmt.setString(1, username);
    
    try (ResultSet rs = pstmt.executeQuery()) {
        while (rs.next()) {
        }
    }
} catch (SQLException e) {
    logger.error(e);
}