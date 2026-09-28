app.get('/user', (req, res) => {
    const usernameInput = String(req.query.username || '');

    db.collection('users').findOne({ username: usernameInput }, (err, user) => {
        if (err) {
            console.error("Database error:", err);
            return res.status(500).json({ error: "Internal server error" });
        }
        
        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }

        res.json(user);
    });
});