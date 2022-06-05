from utils import *

def get_teams_by_player(cur, con):
    """Get the list of all teams the player has been a part of"""
    try:
        playerInfo = TakeInput(["Player Name", "Player Tag"], ["VARCHAR", "VARCHAR"])
        query = (
            "SELECT team_id FROM 5_stack_stats "
            "WHERE player_name='%s' AND player_tag='%s'"
            % (playerInfo["Player Name"], playerInfo["Player Tag"])
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + str(row["team_id"]) + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()
    return


def get_matches_by_team(cur, con):
    """Get the list of all the matches played by a team"""
    try:
        teamInfo = TakeInput(["team_id"], ["INT"])
        query = (
            "SELECT DISTINCT match_id FROM match_description "
            "WHERE team_id='%s'" % (teamInfo["team_id"])
        )
        cur.execute(query)
        retval = cur.fetchall(cur)
        for row in retval:
            print(bcolors.PURPLE + str(row["match_id"]) + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()
    return


def get_round_stats(cur, con):
    """Get the list of all the round stats of a player for a particular match"""
    try:
        roundInfo = TakeInput(
            ["player_name", "player_tag", "match_id"], ["VARCHAR", "VARCHAR", "INT"]
        )
        query = (
            "SELECT round_no, kills, assists, deaths, damage_dealt, first_blood, planter, defuser "
            "FROM round "
            "WHERE player_name='%s' AND player_tag='%s' AND match_id='%s'"
            % (roundInfo["player_name"], roundInfo["player_tag"], roundInfo["match_id"])
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            for key in row.keys():
                print(bcolors.PURPLE + f"{key} : {row[key]}" + bcolors.RESET)
            print("")
    except Exception as e:
        con.rollback()
        printError()
    return


def get_agent_details(cur, con):
    """Get a list of all agents and their abilities"""
    query = "SELECT agent_id, name FROM agent;"
    cur.execute(query)
    retval = cur.fetchall()
    for agent in retval:
        print(bcolors.PURPLE)
        print(agent["name"])
        print("Signature abilities:")
        print(bcolors.RESET)
        query = "SELECT name FROM signature_ability WHERE agent_id = %d" % (
            agent["agent_id"]
        )
        cur.execute(query)
        namerows = cur.fetchall()
        for name in namerows:
            print(bcolors.PURPLE + str(name["name"]) + bcolors.RESET)
        print("")

def get_total_wins(cur, con):
    """Get total wins and losses of a player"""
    try:
        playerName = input(bcolors.GREEN + "Enter player name: " + bcolors.RESET)
        playerTag = input(bcolors.GREEN + "Enter player tag: " + bcolors.RESET)
        query = (
            "SELECT team_id FROM 5_stack_stats WHERE player_name = '%s' AND player_tag = '%s'"
            % (playerName, playerTag)
        )
        cur.execute(query)
        retval = cur.fetchall()
        wins = 0
        total = 0
        for team in retval:
            query = "SELECT wins, matches_played FROM team WHERE team_id = '%s'" % (
                team["team_id"]
            )
            cur.execute(query)
            retval2 = cur.fetchall()
            for count in retval2:
                wins += int(count["wins"])
                total += int(count["matches_played"])
        print(bcolors.PURPLE + f"Wins: {wins} | Losses: {total - wins}" + bcolors.RESET)
    except Exception as e:
        printError()
        con.rollback()


def get_total_wins_by_agent(cur, con):
    """Get total wins and losses of a player for a particular agent"""
    try:
        playerName = input(bcolors.GREEN + "Enter player name: " + bcolors.RESET)
        playerTag = input(bcolors.GREEN + "Enter player tag: " + bcolors.RESET)
        agentID = input(bcolors.GREEN + "Enter agent ID: " + bcolors.RESET)
        query = (
            "SELECT wins, matches_played FROM plays WHERE player_name = '%s' AND player_tag = '%s' AND agent_id = '%s';"
            % (playerName, playerTag, agentID)
        )
        cur.execute(query)
        retval = cur.fetchall()
        wins = 0
        total = 0
        for entry in retval:
            wins += int(entry["wins"])
            total += int(entry["matches_played"])
        print(bcolors.PURPLE + f"Wins: {wins} | Losses: {total - wins}" + bcolors.RESET)
    except Exception as e:
        printError()
        con.rollback()


def get_matches_between_two_teams(cur, con):
    """
    Get all the matches played between two teams
    """
    try:
        matchInfo = TakeInput(["team_id_1", "team_id_2"], ["INT", "INT"])
        query = "SELECT match_id FROM match_description WHERE team_id = '%s';" % (
            matchInfo["team_id_1"]
        )
        cur.execute(query)
        team_one_dict = cur.fetchall()
        query = "SELECT match_id FROM match_description WHERE team_id = '%s';" % (
            matchInfo["team_id_2"]
        )
        cur.execute(query)
        team_two_dict = cur.fetchall()

        team_one_matches = []
        team_two_matches = []

        for k in team_one_dict:
            team_one_matches.append(k["match_id"])
        for k in team_two_dict:
            team_two_matches.append(k["match_id"])

        common = set(team_one_matches) & set(team_two_matches)
        for m in common:
            print(bcolors.PURPLE + str(m) + bcolors.RESET)

    except Exception as e:
        printError()
        con.rollback()


def get_kd(cur, con):
    """Get list of all players with K/D >= x"""
    try:
        x = input(bcolors.GREEN + "Enter the value of x: " + bcolors.RESET)
        query = "SELECT name, tag FROM player;"
        cur.execute(query)
        retval = cur.fetchall()
        for player in retval:
            name = player["name"]
            tag = player["tag"]
            k = 0
            d = 0
            query = (
                "SELECT kills, deaths FROM 5_stack_stats WHERE player_name = '%s' AND player_tag = '%s';"
                % (player["name"], player["tag"])
            )
            cur.execute(query)
            retval2 = cur.fetchall()
            for entry in retval2:
                k += int(entry["kills"])
                d += int(entry["deaths"])
            if d == 0:
                print(
                    bcolors.GREEN
                    + f"Player name: {name} | Player tag: {tag} | K/D = ∞"
                    + bcolors.RESET
                )
            elif (k / d) >= float(x):
                print(
                    bcolors.GREEN
                    + f"Player name: {name} | Player tag: {tag} | K/D = {k/d}"
                    + bcolors.RESET
                )
    except Exception as e:
        printError()
        con.rollback()


def get_kd_for_agent(cur, con):
    """Get a list of all agents for a specific player with K/D ≥ x"""
    try:
        playerName = input(bcolors.GREEN + "Enter the player name: " + bcolors.RESET)
        playerTag = input(bcolors.GREEN + "Enter the player tag: " + bcolors.RESET)
        x = input(bcolors.GREEN + "Enter the value of x: " + bcolors.RESET)
        query = (
            "SELECT agent_id, kills, deaths FROM plays WHERE player_name = '%s' AND player_tag = '%s';"
            % (playerName, playerTag)
        )
        cur.execute(query)
        retval = cur.fetchall()
        for entry in retval:
            k = entry["kills"]
            d = entry["deaths"]
            id = entry["agent_id"]
            if d == 0:
                print(bcolors.PURPLE + f"Agent ID: {id} | K/D = ∞" + bcolors.RESET)
            elif (k / d) >= float(x):
                print(bcolors.PURPLE + f"Agent ID: {id} | K/D = {k/d}" + bcolors.RESET)
    except Exception as e:
        printError()
        con.rollback()


def get_winrate_for_agent(cur, con):
    """Get a list of all agents for a specific player with win rate ≥ x"""
    try:
        playerName = input(bcolors.GREEN + "Enter the player name: " + bcolors.RESET)
        playerTag = input(bcolors.GREEN + "Enter the player tag: " + bcolors.RESET)
        x = input(bcolors.GREEN + "Enter the value of x: " + bcolors.RESET)
        query = (
            "SELECT agent_id, wins, matches_played FROM plays WHERE player_name = '%s' AND player_tag = '%s';"
            % (playerName, playerTag)
        )
        cur.execute(query)
        retval = cur.fetchall()
        for entry in retval:
            k = entry["wins"]
            d = entry["matches_played"]
            id = entry["agent_id"]
            if d == 0:
                print(bcolors.PURPLE + f"Agent ID: {id} | Win rate = ∞" + bcolors.RESET)
            elif (k / d) >= float(x):
                print(
                    bcolors.PURPLE
                    + f"Agent ID: {id} | Win rate = {k/d}"
                    + bcolors.RESET
                )
    except Exception as e:
        printError()
        con.rollback()
