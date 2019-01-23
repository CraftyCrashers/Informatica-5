def vlag(richting, kleuren):
    resultaat = ''
    if richting == 'verticaal':
        streep = ' | '
    else:
        streep = '\n-\n'
    for kleur in kleuren:
        if kleur == kleuren[-1]:
            resultaat += kleur
        else:
            resultaat += kleur + streep
    return resultaat
