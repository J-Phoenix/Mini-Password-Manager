from . import crypto_utils, storage

class PasswordManager:
    def __init__(self, master_password: str):
        self.master_password = master_password
        self.data = {}
        self.payload = storage.load_store()
        if self.payload is None:
            # first time → create store
            self.data = {}
            self._save()
        else:
            self.data = crypto_utils.decrypt_data(master_password, self.payload)

    def _save(self):
        self.payload = crypto_utils.encrypt_data(self.master_password, self.data)
        storage.save_store(self.payload)

    def add_credential(self, site: str, username: str, password: str):
        self.data[site] = {"username": username, "password": password}
        self._save()

    def get_credential(self, site: str):
        return self.data.get(site)

    def list_sites(self):
        return list(self.data.keys())

    def delete_credential(self, site: str):
        if site in self.data:
            del self.data[site]
            self._save()
