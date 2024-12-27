def generate_tweaks(level, days, distance, terrain):
    """
    Generuje słownik tweaks na podstawie danych wejściowych.
    """
    return {
        "TextInput-LwnOJ": {"input_value": str(level)},
        "TextInput-lhPKt": {"input_value": str(days)},
        "TextInput-OlZqZ": {"input_value": str(distance)},
        "TextInput-T7vfQ": {"input_value": str(terrain)},
    }
