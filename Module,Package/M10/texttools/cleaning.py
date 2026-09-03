def clean(text):
    for ch in ".,!?":
        text = text.replace(ch, "")

    text = " ".join(text.split())
    return text