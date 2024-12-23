## CCT College Dublin

|                        |                                                                     |
|------------------------|---------------------------------------------------------------------|
| **Module Title:**      | Cryptography Theory and Practice                                    |
| **Assessment Title:**  | Securing Communication and Data Integrity in Modern IT Environments |
| **Lecturer Name:**     | Dr. Naila Aslam                                                     |
| **Student Full Name:** | Javier Alfonso Ocampo                                               |
| **Student Number:**    | 2024328                                                             |

## Assessment Title: Securing Communication and Data Integrity in Modern IT Environments

### Task 1: Securing Communication and Data Integrity with IPSEC

Securing communication in a global corporation is essential for protecting sensitive information between its headquarters and regional offices. IPSEC, or Internet Protocol Security, is a widely used framework that safeguards communication at the network layer. It ensures confidentiality, integrity, and authentication of data as it travels across networks. Two key components of IPSEC, Encapsulation Security Payload (ESP) and Authentication Header (AH), play important roles in securing communication. This report explains how these protocols work and addresses the challenges of implementing IPSEC in dynamic network environments where IP addresses frequently change.

Encapsulation Security Payload (ESP) is primarily designed to protect the confidentiality of transmitted data. It encrypts the content of an IP packet, ensuring that unauthorized parties cannot read the information. In addition to encryption, ESP can also verify the integrity and authenticity of the data, preventing tampering during transit. ESP operates in two modes. In transport mode, it encrypts only the data portion of the IP packet, leaving the original header visible. This mode is suitable for communication between individual devices. In tunnel mode, it encrypts the entire IP packet, including the original header, and adds a new header for routing. This mode is commonly used for secure communication between networks, such as when connecting a headquarters to its branch offices through a VPN.

Authentication Header (AH) is another protocol in IPSEC that focuses on providing integrity and authentication without encrypting the data. AH ensures that the data remains unchanged during transmission and verifies that it comes from a trusted source. Like ESP, AH can operate in transport mode or tunnel mode. In transport mode, it authenticates the data and portions of the original IP header, while in tunnel mode, it authenticates the entire packet, including a new header. Unlike ESP, AH does not provide encryption, which means the data remains visible. This makes AH suitable for scenarios where encryption is not necessary but verifying data authenticity and integrity is crucial.

Implementing IPSEC in dynamic network environments can present several challenges. One common issue is the frequent change of IP addresses in networks that use DHCP (Dynamic Host Configuration Protocol). Since IPSEC relies on predefined Security Associations (SAs) to manage encryption and authentication parameters, changes in IP addresses can disrupt these configurations. To address this, dynamic protocols such as Internet Key Exchange version 2 (IKEv2) can be used to automatically update and renegotiate SAs when IP addresses change. IKEv2 also includes a feature called MOBIKE, which ensures that secure connections remain active even when devices switch networks.

Another challenge is the increased workload on devices caused by the encryption and decryption of data. These processes require significant computing resources, which can slow down network performance, especially in high-traffic environments. To mitigate this issue, organizations can use hardware-based encryption accelerators or dedicated devices that handle cryptographic operations more efficiently. Choosing efficient encryption algorithms, such as AES (Advanced Encryption Standard), can also help optimize performance without compromising security.

Interoperability is another concern, as devices from different vendors may implement IPSEC differently. This can lead to compatibility issues when configuring secure connections. To address this, organizations should ensure that all devices follow standardized IPSEC implementations. Regular updates to firmware and software can also help maintain compatibility and security. Additionally, IPSEC can face challenges in networks that use NAT (Network Address Translation), as NAT modifies packet headers, which can interfere with IPSEC’s authentication process. Enabling a feature called NAT Traversal (NAT-T) allows IPSEC packets to pass through NAT by encapsulating them within UDP headers.

In conclusion, IPSEC is a powerful solution for ensuring secure communication in modern networks. ESP provides encryption and data integrity, while AH focuses on data authenticity. Although dynamic environments and technical challenges may complicate implementation, tools such as IKEv2, NAT Traversal, and hardware optimization offer practical solutions. With proper configuration and management, IPSEC can deliver reliable and scalable protection for sensitive communication across a global organization.


### Task 2: Maximizing Security with Advanced Encryption Standard (AES)

In today's digital landscape, safeguarding sensitive data is essential for protecting customer trust and ensuring compliance with regulations. The Advanced Encryption Standard (AES) is one of the most secure and widely used encryption algorithms, providing strong protection against unauthorized access. This report discusses how AES ensures data confidentiality, examines its modes of operation for different use cases, and outlines best practices for securely managing AES keys. Additionally, a Python example demonstrates the practical application of AES encryption.

**How AES Ensures Data Confidentiality**

AES is a symmetric encryption algorithm, meaning it uses the same key for both encryption and decryption. It operates on fixed-size blocks of 128 bits and supports key lengths of 128, 192, or 256 bits. These longer key lengths make AES highly resistant to brute-force attacks, as the sheer number of possible key combinations makes decryption without the key computationally infeasible.

The encryption process in AES involves multiple rounds of transformation, including substitution, permutation, and mixing. Each round increases the complexity of the ciphertext, ensuring that even small changes in the plaintext result in entirely different ciphertext. This property, known as diffusion, ensures that attackers cannot infer patterns or reconstruct the original data without the encryption key. AES’s robust design and efficiency make it suitable for applications ranging from securing databases to encrypting communication in real-time systems.

**Modes of Operation for Different Use Cases**

AES is a block cipher, meaning it processes data in fixed-size blocks. To handle larger or varying amounts of data, it operates in different modes. Each mode has unique characteristics and use cases:

- 1. Cipher Block Chaining (CBC): In CBC mode, each block of plaintext is XORed with the ciphertext of the previous block before being encrypted. This adds randomness to the encryption process, ensuring that even identical plaintext blocks produce different ciphertext. CBC is suitable for encrypting files and large datasets but requires an Initialization Vector (IV) to prevent predictable patterns in the first block. The IV must be random and unique for each encryption session to maintain security.

- 2. Galois/Counter Mode (GCM): GCM is a modern mode that combines encryption with authentication, ensuring both data confidentiality and integrity. It processes plaintext in independent blocks, enabling faster encryption and decryption. GCM also generates an authentication tag that verifies the integrity of the encrypted data, making it ideal for secure network communications, such as HTTPS and VPNs. Its efficiency and security make GCM the preferred choice for real-time applications.

- 3. Electronic Codebook (ECB): ECB is the simplest mode, where each plaintext block is encrypted independently. However, it is generally considered insecure because identical plaintext blocks produce identical ciphertext, revealing patterns in the data. As a result, ECB should only be used in non-sensitive applications where data confidentiality is not a priority.


Choosing the Right Mode. The choice of mode depends on the application. For encrypting files or databases, CBC is often suitable, while GCM is better for securing communications where both encryption and integrity are critical. Avoid using ECB for sensitive data due to its inherent vulnerabilities.

Secure Storage and Management of AES Keys. The effectiveness of AES depends heavily on the secure storage and management of encryption keys. If keys are exposed, attackers can decrypt the data regardless of how strong the algorithm is. Below are some best practices for key management:

- 1. Secure Key Storage: Encryption keys should never be stored in plaintext. Instead, they can be protected using hardware security modules (HSMs) or encrypted key storage systems. Storing keys in memory or insecure files increases the risk of compromise.

- 2. Key Rotation: Regularly rotating encryption keys limits the potential damage caused by a compromised key. Rotating keys periodically ensures that older encrypted data cannot be decrypted if the key is exposed.

- 3. Secure Key Transmission: When sharing keys across systems or devices, always use secure transmission protocols like TLS (Transport Layer Security). This prevents keys from being intercepted during transfer.


Below is a Python example demonstrating AES encryption using the `cryptography` library in Galois/Counter Mode (GCM):

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit key and 96-bit IV
key = os.urandom(32)  # 256 bits
iv = os.urandom(12)   # 96 bits, recommended for GCM

# Data to encrypt
plaintext = b"Sensitive customer data"

# Create AES-GCM cipher
cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
encryptor = cipher.encryptor()

# Encrypt data
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Authentication tag
auth_tag = encryptor.tag

print(f"Ciphertext: {ciphertext}")
print(f"Authentication Tag: {auth_tag}")
print(f"IV: {iv}")
```

### Task 3

**Ensuring Data Integrity with SHA (Secure Hash Algorithm)**

An e-commerce platform needs to ensure that files uploaded by users maintain their integrity during storage and transfer. The **Secure Hash Algorithm (SHA)** family provides an effective solution for verifying file integrity by generating a unique hash for each file. This report explains the role of SHA in ensuring data integrity, compares different SHA versions, discusses vulnerabilities of outdated algorithms, and includes a Python example for hashing a file. Additionally, a brief mention of AWS S3 and Cloudinary highlights their support for file integrity and security.

---

**The Role of SHA in Ensuring Data Integrity**

SHA is a cryptographic algorithm used to create a unique, fixed-length hash value for any given input, such as a file or a message. This hash acts like a digital fingerprint, uniquely representing the data's content. Even a small change in the file will result in a completely different hash value, making SHA highly reliable for detecting tampering or corruption.

For an e-commerce platform, this ensures that:
1. Files uploaded by users (e.g., product images or documents) are not altered during upload or storage.
2. Any accidental data corruption or unauthorized changes can be detected by comparing the original hash with a newly computed hash.

---

**Comparison of Different SHA Versions**

The SHA family includes several versions, each with distinct levels of security and performance. Below is a comparison of the commonly used versions:

1. SHA-1
- Hash Length: 160 bits.
- Security: Weak and outdated. Vulnerable to collision attacks, where two different inputs produce the same hash value.
- Current Use: Rarely used due to its insecurity. It is unsuitable for modern applications requiring strong integrity verification.

2. SHA-256
- Hash Length: 256 bits.
- Security: Strong. Resistant to collision and pre-image attacks, making it suitable for verifying file integrity in modern systems.
- Use Cases: Widely used in applications such as digital signatures, blockchain, and file verification.

3. SHA-3
- Hash Length: Configurable (256 bits, 512 bits, etc.).
- Security: Very strong. Unlike SHA-2, SHA-3 is based on a completely different algorithm (Keccak), offering added resistance to certain attacks.
- Use Cases: Advanced cryptographic applications where additional security is needed.


| SHA Version      | Hash Length    | Security                 | Best Use Cases                     |
|------------------|----------------|--------------------------|------------------------------------|
| SHA-1            | 160 bits       | Weak (vulnerable)        | Legacy systems (not recommended)   |
| SHA-256          | 256 bits       | Strong                   | File integrity, digital signatures |
| SHA-3            | 256+ bits      | Very strong              | High-security applications         |


Here’s a Python example of how to generate a hash for a file using **SHA-256**. This ensures that the file’s integrity can be verified later by comparing the hash values.

```python
import hashlib

def compute_file_hash(file_path):
    """
    Generate the SHA-256 hash of a file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # Read the file in chunks to handle large files
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# Example usage
file_path = "example_file.txt"
hash_value = compute_file_hash(file_path)
print(f"SHA-256 Hash of the file: {hash_value}")
```

**AWS S3 and Cloudinary**

E-commerce commonly use external services to store static files. Modern cloud platforms like AWS S3 and Cloudinary provide additional tools to help ensure file integrity and security.

AWS S3
- ETag for Integrity Verification: AWS S3 generates an ETag (often an MD5 hash) for uploaded files. This can be compared with a local hash to ensure the file's integrity.
- Encryption: S3 supports both server-side and client-side encryption to secure data at rest and in transit.
- Access Control: Fine-grained access policies prevent unauthorized access to stored files.

Cloudinary
- Encryption at Rest and in Transit: Files are encrypted during storage and transfer, ensuring privacy and security.
- Signed URLs: These allow secure access to files by adding an expiration time, ensuring only authorized users can retrieve or download files.
- File Management Tools: Cloudinary provides integrated tools for file validation and optimization.

**Conclusion**

SHA is a powerful tool for ensuring the integrity of files uploaded to an e-commerce platform. Modern algorithms like SHA-256 and SHA-3 provide strong security, while outdated algorithms like SHA-1 are no longer suitable due to vulnerabilities. By using secure hash algorithms and leveraging the built-in integrity features of platforms like AWS S3 and Cloudinary, e-commerce platforms can reliably protect user-uploaded files and maintain trust.
