def getNumber(desc):
    try:
        return int(input(desc))
    except Exception:
        return getNumber(desc)