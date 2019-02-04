def ik_heb_gemoord(opdrachten_lijst, moordenaar):
    if len(opdrachten_lijst) == 1:
        volgend_doelwit = opdrachten_lijst[0]
    elif len(opdrachten_lijst) - opdrachten_lijst.index(moordenaar) > 2:
        opdrachten_lijst.pop(opdrachten_lijst.index(moordenaar) + 1)
        volgend_doelwit = opdrachten_lijst[(opdrachten_lijst.index(moordenaar) + 1)]
    elif len(opdrachten_lijst) - opdrachten_lijst.index(moordenaar) == 2:
        opdrachten_lijst.pop(-1)
        volgend_doelwit = opdrachten_lijst[0]
    else:
        opdrachten_lijst.pop(0)
        volgend_doelwit = opdrachten_lijst[0]
    return volgend_doelwit, opdrachten_lijst


def ik_ben_vermoord(opdrachten_lijst, slachtoffer):
    if len(opdrachten_lijst) - opdrachten_lijst.index(slachtoffer) == 1:
        volgend_doelwit = opdrachten_lijst[0]
    else:
        volgend_doelwit = opdrachten_lijst[opdrachten_lijst.index(slachtoffer) + 1]
    if len(opdrachten_lijst) != 1:
        opdrachten_lijst.pop(opdrachten_lijst.index(slachtoffer))
    return volgend_doelwit, opdrachten_lijst
