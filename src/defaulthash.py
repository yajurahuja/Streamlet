from cryptography.hazmat.primitives import hashes

class common_hash:
    def __init__(self):
        self.hasher = hashes.Hash(hashes.SHA256())

    def __bytes__(self):
        return bytes("self.hasher", 'utf-8')

    def get_hasher(self):
        hasher_copy = self.hasher.copy()
        return hasher_copy


print("test")
b = common_hash()
a = b.get_hasher()
a.update(bytes(b))
print(a.finalize)