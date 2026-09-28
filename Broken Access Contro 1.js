app.get('/profile/:userId', authenticateToken, (req, res) => {
    const requestedUserId = req.params.userId;
    const currentUserId = req.user.id;

    // Authorization Check: Allow access only if the user owns the profile 
    if (requestedUserId !== currentUserId ) {
        return res.status(403).json();
    }

    User.findById(requestedUserId, (err, user) => {
        if (err) return res.status(500).json();
        if (!user) return res.status(404).json();
        
        // Return only necessary public/profile fields, avoiding sensitive internal data leakage
        res.json({
            id: user.id,
            username: user.username,
            email: user.email
        });
    });
});
