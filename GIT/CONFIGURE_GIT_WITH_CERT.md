## Configuring Git with SSL/TLS Certificate for Private GitLab Access

When working with a private GitLab instance or any internal Git repository, SSL/TLS certificates are often used to secure communication between your local machine and the Git server. To ensure secure authentication and avoid connection issues, you need to configure Git to trust the server's SSL certificate.

Follow these steps to configure your Git client with the SSL/TLS certificate:

### **1. Obtain the SSL/TLS Certificate**

Your company should provide an SSL certificate, usually in `.p12` format (e.g., `<company>_certificate.p12`). This certificate is required for secure communication with the Git server.

### **2. Extract the Certificate and Private Key**

From the `.p12` certificate, extract the client certificate (`.crt`) and the private key (`.key`) using the following commands:

```bash
# Extract the client certificate
openssl pkcs12 -in <company>_certificate.p12 -clcerts -nokeys -out <company>_client.crt

# Extract the private key
openssl pkcs12 -in <company>_certificate.p12 -nodes -nocerts | openssl rsa -out <company>_server.key
```

This generates:
- `<company>_client.crt`: the client certificate.
- `<company>_server.key`: the private key.


### **3. Configure Git to Use the Certificate**

Add the paths to the extracted certificate and key in your Git configuration file (`.gitconfig`):

1. Open the `.gitconfig` file (located in your home directory, e.g., `~/.gitconfig`).
2. Add the following:

```ini
[user]
    email = example@<company>.com
    name = example.user

[http "https://gitlab.<company>.com"]
    sslCert = "/path/to/<company>_client.crt"  # Path to the client certificate
    sslKey = "/path/to/<company>_server.key"   # Path to the private key
```

Replace:
- `/path/to/<company>_client.crt` with the actual path to the certificate.
- `/path/to/<company>_server.key` with the actual path to the private key.
- `https://gitlab.<company>.com` with your company’s GitLab URL.

### **4. Save GitLab Credentials (Optional)**

To avoid repeated login prompts, store your GitLab credentials securely:

1. Add credentials to the `.git-credentials` file:
   ```bash
   https://<gitlab_username>:<personal_access_token>@gitlab.<company>.com
   ```
   Replace:
   - `<gitlab_username>` with your GitLab username.
   - `<personal_access_token>` with your GitLab personal access token (preferred over a password).

2. Ensure your `.gitconfig` references this file:
   ```ini
   [credential]
       helper = store
   ```

### **5. Test the Configuration**

Verify your setup by interacting with the repository, e.g.:

```bash
git clone https://gitlab.<company>.com/your-repository.git
```

If configured correctly, Git will securely connect to the GitLab server without SSL/TLS errors or repeated prompts for credentials.

---

## Explanation of the `openssl` commands used to generate the client certificate and private key

#### **1. Extracting the Client Certificate**

```bash
openssl pkcs12 -in <company>_certificate.p12 -clcerts -nokeys -out <company>_client.crt
```

**Explanation**:
- `openssl`: Command-line tool for managing certificates, keys, and related cryptographic operations.
- `pkcs12`: Specifies that the input file is in PKCS#12 format, commonly used to bundle private keys, certificates, and optionally CA certificates in a single file.
- `-in <company>_certificate.p12`: Path to the input `.p12` file containing the bundled certificate and private key.
- `-clcerts`: Extracts only the client certificate (ignores CA certificates or other types of certificates in the bundle).
- `-nokeys`: Ensures the private key is not included in the output.
- `-out <company>_client.crt`: Specifies the output file where the extracted client certificate will be saved.


#### **2. Extracting the Private Key**

```bash
openssl pkcs12 -in <company>_certificate.p12 -nodes -nocerts | openssl rsa -out <company>_server.key
```

**Explanation**:
- `openssl pkcs12`: Same as above, specifying the input file format.
- `-in <company>_certificate.p12`: Path to the input `.p12` file.
- `-nodes`: Outputs the private key without encrypting it (in plaintext format). This is essential for Git to use the private key directly.
- `-nocerts`: Ensures only the private key is extracted (excludes any certificates from the output).
- `| openssl rsa`: Pipes the extracted private key to another `openssl` command to ensure it is in the correct RSA key format for Git.
- `-out <company>_server.key`: Specifies the output file where the private key will be saved.


#### **Result**:
- The **first command** generates a file `<company>_client.crt` containing the client certificate.
- The **second command** generates a file `<company>_server.key` containing the corresponding private key. 

These files are used to configure Git to establish a secure connection with the server.

### **References**
- [Create a pkcs12 (.pfx or .p12) from OpenSSL files - tbs-internet](https://www.tbs-certificates.co.uk/FAQ/en/288.html)
- [openssl-pkcs12 - OpenSSL Documentation](https://docs.openssl.org/master/man1/openssl-pkcs12/)
- [Working with openssl to extract information from a pkcs12 certificate - StackOverflow Discussion](https://stackoverflow.com/questions/8500475/working-with-openssl-to-extract-information-from-a-pkcs12-certificate)
- [How to Install OpenSSL on Windows](https://kb.firedaemon.com/support/solutions/articles/4000121705)