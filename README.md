# Module-5-OWASP-Top-10-Code-Fix

Broken Access Control:

1. The original code doesn’t  authenticate the user or their authorization to verify if they should be able to access the data. It also allows parameter tampering by allowing modification of the url.
The use of an authenticateToken authenticates the user and allows access to their own data while the “requestedUserId !== loggedInUserId” check prevents their access to other data. This enforces the principle of least privilege.

2. This code doesn’t authenticate the user or their authorization to verify if they should be able to access the data. It also allows someone to change the userId parameter in the URL to view account details of other users.
This code makes a check to verify the user can only see their own data while preventing changes to the Id parameter.

Cryptographic Failures:

3. The original code uses a cryptographically broken algorithm that can be used to precompute hashes and doesn’t adequately salt the hashes to provide true randomness.
This code uses the dedicated hashing algorithm BCrypt that allows for the generation of a unique and secure salt.

4. The original code uses SHA-1 for its hashing, which is no longer cryptographically secure because of its susceptibility to collision attacks. The function also doesn’t use a unique salt for each password so identical passwords will generate the same hash.
This code uses BCrypt to generate unique salts for each password so the hashes of identical passwords are never the same.

Injection:

5. The original code takes a parameter from the HTTP request and concatenates it into a SQL string, allowing the user to possibly input executable SQL commands instead of data.
This code uses a prepared statement to pre-compile the SQL query structure on the database server and allows the database to treat the placeholder as data and not code.

6. The original code directly passes the req.query.username object into the MondgoDB findOne query filter without validating or filtering it.  This allows for the injection of malicious objects.
This code wraps the input in String() and forces MongoDB to treat the input as a literal string and not data.

Insecure Design:

7. The original code allows any user to change the password of any other user by knowing their email address with  no further identity verification. It also stores the passwords as plaintext with no encryption or hashing.
This code uses token verification to only allow someone with access to the target email inbox to reset the password and hashes the stored passwords.

Software and Data Integrity Failures:

8. The original code lacks a cryptographic hash check and makes the browser trust whatever file the external CDN serves.  There is no integrity attribute containing a cryptographic hash to verify file contents.
This code adds an integrity hash and crossorigin attribute to the browser rejects the script if it has been modified.

Server-Side Request Forgery:

9. In the original code the application accepts an untrusted, user-supplied URL and passes it to the request.get() without validation or filtering. This can lead to manipulation of the network.
This code implements input validation using explicit allowlists of permitted domains and enforces the https protocol.

Identification and Authentication Failures:

10. The original code compares plaintext passwords, meaning the passwords are stored as unencrypted plaintext instead of a secure, encrypted hash.
This code salts and hashes the passwords before storing them.
