def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob:
        if hey_bob.isupper():
            if hey_bob[-1] == '?':
                return "Calm down, I know what I'm doing!"
            else:
                return "Whoa, chill out!"
        else:
            if hey_bob[-1] == '?':
                return "Sure."
            else:
                return "Whatever."
    return "Fine. Be that way!"
