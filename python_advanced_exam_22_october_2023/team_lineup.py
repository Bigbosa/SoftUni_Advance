def team_lineup(*players):
    players_data = {}
    for player, country in players:
        if country in players_data:
            players_data[country].append(player)
        else:
            players_data[country] = [player]

    sorted_data = sorted(players_data.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for country, players in sorted_data:
        result.append(f"{country}:")
        for player in players:
            result.append(f"  -{player}")

    return "\n".join(result)

print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))

print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))

print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany"),
    ("Bruno Fernandes", "Portugal"),
    ("Bernardo Silva", "Portugal"),
    ("Harry Maguire", "England")))


