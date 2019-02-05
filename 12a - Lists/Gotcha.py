def ik_heb_gemoord(opdrachten_lijst, moordenaar):
    volgend_doelwit = opdrachten_lijst[(opdrachten_lijst.index(moordenaar) + 2) % len(opdrachten_lijst)]
    if not len(opdrachten_lijst) == 1:
        opdrachten_lijst.pop(opdrachten_lijst.index(moordenaar) + 1 % len(opdrachten_lijst))
    return volgend_doelwit, opdrachten_lijst


def ik_ben_vermoord(opdrachten_lijst, slachtoffer):
    volgend_doelwit = opdrachten_lijst[(opdrachten_lijst.index(slachtoffer) + 1) % len(opdrachten_lijst)]
    if len(opdrachten_lijst) != 1:
        opdrachten_lijst.pop(opdrachten_lijst.index(slachtoffer))
    return volgend_doelwit, opdrachten_lijst
