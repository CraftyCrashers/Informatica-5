def vergeten_woorden(string, set_):
    lijst = set(string.split())
    return len(set_), len(set_) - len(set_.intersection(lijst)), len(set_.intersection(lijst))
