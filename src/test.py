from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#generate key
signer = rsa.generate_private_key(public_exponent=65537, key_size=2048)
message = bytes("Just a regular function", 'utf-8')
#sign a message
signature = signer.sign(message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
print(signature)
#verify the message
pk = signer.public_key()
pk.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

a = hashes.Hash(hashes.SHA256())
print(a)