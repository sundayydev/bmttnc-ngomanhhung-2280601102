import rsa

class RSACipher:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
    
    def generate_keys(self):
        """Tạo cặp khóa RSA."""
        self.public_key, self.private_key = rsa.newkeys(self.key_size)
        with open("cipher/rsa/keys/private_key.pem", "wb") as priv_file:
            priv_file.write(self.private_key.save_pkcs1("PEM"))
        with open("cipher/rsa/keys/public_key.pem", "wb") as pub_file:
            pub_file.write(self.public_key.save_pkcs1("PEM"))
    
    def load_keys(self):
        """Tải khóa từ file."""
        with open("private_key.pem", "rb") as priv_file:
            private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
        with open("public_key.pem", "rb") as pub_file:
            public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
        return private_key, public_key
    
    def encrypt(self, message: str, key):
        """Mã hóa thông điệp bằng khóa RSA."""
        return rsa.encrypt(message.encode(), key)
    
    def decrypt(self, ciphertext: bytes, key):
        """Giải mã ciphertext RSA."""
        try:
            return rsa.decrypt(ciphertext, key).decode()
        except:
            return "Decryption failed!"
    
    def sign(self, message: str, private_key):
        """Ký thông điệp bằng khóa riêng."""
        return rsa.sign(message.encode(), private_key, 'SHA-256')
    
    def verify(self, message: str, signature: bytes, public_key):
        """Xác minh chữ ký bằng khóa công khai."""
        try:
            return rsa.verify(message.encode(), signature, public_key) == 'SHA-256'
        except:
            return False
