import base64, secrets
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

KDF_ITERATIONS = 200_000
SALT_SIZE = 16

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive Fernet key from password+salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=KDF_ITERATIONS,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))

def encrypt_data(master, data: dict) -> dict:
    """Encrypt dict into payload with salt+token."""
    import json
    salt = secrets.token_bytes(SALT_SIZE)
    key = derive_key(master, salt)
    f = Fernet(key)
    token = f.encrypt(json.dumps(data).encode())
    return {
        "salt": base64.b64encode(salt).decode(),
        "token": base64.b64encode(token).decode(),
    }

def decrypt_data(master, payload: dict) -> dict:
    """Decrypt payload back to dict."""
    import json
    salt = base64.b64decode(payload["salt"])
    token = base64.b64decode(payload["token"])
    key = derive_key(master, salt)
    f = Fernet(key)
    try:
        return json.loads(f.decrypt(token).decode())
    except InvalidToken:
        raise ValueError("Invalid master password")
