def verlaat_ploeg(verlating, team, lijst_teams):
    lijst_teams.get(team).remove(verlating)
    if lijst_teams.get(team) == []:
        lijst_teams.pop(team)
    return lijst_teams


def vervoegt_ploeg(toevoeging, team, lijst_teams):
    if lijst_teams.get(team) is None:
        lijst_teams[team] = []
    lijst_teams.get(team).append(toevoeging)
    return lijst_teams
