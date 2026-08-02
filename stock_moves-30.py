# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: StockMoves
class ProfileManager:
    def __init__(self):
        self.profiles = {"admin": {"role": "admin", "name": "Администратор"}}

    def add_profile(self, name, role, password=None):
        if name in self.profiles:
            print(f"Профиль '{name}' уже существует.")
            return False
        self.profiles[name] = {"role": role, "password": password or ""}
        print(f"Профиль '{name}' создан с ролью '{role}'.")
        return True

    def login(self, name, password):
        if name in self.profiles and self.profiles[name]["password"] == password:
            return name
        else:
            print("Неверное имя или пароль.")
            return None

    def get_profile_role(self, name):
        return self.profiles.get(name, {}).get("role", "unknown")

    def list_profiles(self):
        return {name: data["role"] for name, data in self.profiles.items()}


PROFILE_MANAGER = ProfileManager()
