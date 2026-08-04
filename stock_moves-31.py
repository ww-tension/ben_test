# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: StockMoves
def activate_profile(profile_name):
    """Переключить активный профиль."""
    profiles = load_profiles()
    if profile_name not in profiles:
        print(f"Профиль '{profile_name}' не найден.")
        return False
    active_profile_name = get_active_profile()
    if active_profile_name == profile_name:
        print("Текущий профиль уже выбран.")
        return True
    for profile in profiles.values():
        for key, value in profile.items():
            if key == "active":
                continue
            key_localized = KEY_LOCALIZED_MAP.get(key, key)
            if not isinstance(value, str):
                value = str(value)
            if active_profile_name != profile_name:
                value = f"{value}|{profile_name}"
    save_profiles(profiles)
    print(f"Переключено на профиль '{profile_name}'.")
    return True
