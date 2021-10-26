import subprocess as sp
import pymysql
import pymysql.cursors
import getpass


class bcolors:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def printError():
    print(bcolors.RED + "Error: Operation failed." + bcolors.RESET)


def TakeInput(items: list = [], Type: list = []):
    """Util function to quickly take input from user"""
    inputs = {}
    for idx, item in enumerate(items):
        val = input(
            bcolors.GREEN
            + "Please enter "
            + item
            + " (Type: "
            + Type[idx]
            + "): "
            + bcolors.RESET
        )
        inputs[item] = val
    return inputs


def get_teams_by_player():
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
            print(bcolors.PURPLE + row["team_id"] + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()
    return


def get_matches_by_team():
    """Get the list of all the matches played by a team"""
    try:
        teamInfo = TakeInput(["team_id"], ["INT"])
        query = (
            "SELECT DISTINCT match_id FROM match_description "
            "WHERE team_id='%s'" % (teamInfo["team_id"])
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + row["match_id"] + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()
    return


def get_round_stats():
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


def get_agent_details():
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
            print(bcolors.PURPLE + name["name"] + bcolors.RESET)
        print("")


def get_total_wins_by_agent():
    """Get total wins and losses of a player for a particular agent"""
    try:
        playerName = input(bcolors.GREEN + "Enter player name: " + bcolors.RESET)
        playerTag = input(bcolors.GREEN + "Enter player tag: " + bcolors.RESET)
        agentID = input(bcolors.GREEN + "Enter agent ID: " + bcolors.RESET)
        query = (
            "SELECT SUM(wins) FROM plays "
            "WHERE player_name = '%s' AND player_tag = '%s" % (playerName, playerTag)
        )
        print(bcolors.PURPLE + query + bcolors.RESET)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()
    return


def insert_player():
    """Insert player into database"""
    try:
        playerInfo = TakeInput(
            [
                "player_name",
                "player_tag",
                "date_of_birth",
                "time_played",
                "rank_rating",
                "region",
                "coach-name",
                "coach-tag",
            ],
            [
                "VARCHAR",
                "VARCHAR",
                "DATE",
                "TIME",
                "INT",
                "VARCHAR",
                "VARCHAR",
                "VARCHAR",
            ],
        )
        query = (
            "INSERT INTO player VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s', '%s')"
            % (
                playerInfo["player_name"],
                playerInfo["player_tag"],
                playerInfo["date_of_birth"],
                playerInfo["time_played"],
                int(playerInfo["rank_rating"]),
                playerInfo["region"],
                playerInfo["coach-name"],
                playerInfo["coach-tag"],
            )
        )
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()


def update_player_rating():
    """Updater player rating entry in database"""
    try:
        playerInfo = TakeInput(
            ["player_name", "player_tag", "updated_rating"],
            ["VARCHAR", "VARCHAR", "INT"],
        )
        query = (
            "UPDATE player SET rank_rating = %d WHERE name = '%s' AND tag = '%s';"
            % (
                int(playerInfo["updated_rating"]),
                playerInfo["player_name"],
                playerInfo["player_tag"],
            )
        )
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()


def update_player_region():
    """Updater player rating entry in database"""
    try:
        playerInfo = TakeInput(
            ["player_name", "player_tag", "updated_region"],
            ["VARCHAR", "VARCHAR", "VARCHAR"],
        )
        query = "UPDATE player SET region = '%s' WHERE name = '%s' AND tag = '%s';" % (
            playerInfo["updated_region"],
            playerInfo["player_name"],
            playerInfo["player_tag"],
        )
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()


def update_agent_lore():
    """Update agent lore in database"""
    try:
        agentInfo = TakeInput(["agent_id", "updated_lore"], ["INT", "TEXT"])
        query = "UPDATE agent SET lore = '%s' WHERE agent_id = %d;" % (
            agentInfo["updated_lore"],
            int(agentInfo["agent_id"]),
        )
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()


def delete_player():
    """Delete player entry from database"""
    try:
        playerInfo = TakeInput(["player_name", "player_tag"], ["VARCHAR", "VARCHAR"])
        query = "DELETE FROM player WHERE name = '%s' AND tag = '%s'" % (
            playerInfo["player_name"],
            playerInfo["player_tag"],
        )
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()


def partial_search_agent():
    try:
        agentInfo = TakeInput(["partial_agent_name"], ["VARCHAR"])
        query = "SELECT name FROM agent WHERE name LIKE '%%%s%%'" % (
            agentInfo["partial_agent_name"]
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + row["name"] + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()


def partial_search_player():
    try:
        playerInfo = TakeInput(["partial_player_name"], ["VARCHAR"])
        query = "SELECT name FROM player WHERE name LIKE '%%%s%%'" % (
            playerInfo["partial_player_name"]
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + row["name"] + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()


def get_total_wins():
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


def get_total_wins_by_agent():
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


def get_matches_between_two_teams():
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
            print(m)

    except Exception as e:
        printError()
        con.rollback()


def get_kd():
    """Get list of all players with K/D >= x"""
    try:
        x = input("Enter the value of x: ")
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
                print(f"Player name: {name} | Player tag: {tag}")
            elif (k / d) >= float(x):
                print(f"Player name: {name} | Player tag: {tag}")
    except Exception as e:
        printError()
        con.rollback()
    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    if ch == 1:
        insert_player()
    elif ch == 2:
        update_player_rating()
    elif ch == 3:
        update_player_region()
    elif ch == 4:
        update_agent_lore()
    elif ch == 5:
        delete_player()
    elif ch == 6:
        get_total_wins_by_agent()
    elif ch == 7:
        get_teams_by_player()
    elif ch == 8:
        get_matches_by_team()
    elif ch == 9:
        get_round_stats()
    elif ch == 10:
        get_agent_details()
    elif ch == 11:
        partial_search_agent()
    elif ch == 12:
        partial_search_player()
    elif ch == 13:
        get_total_wins()
    elif ch == 14:
        get_total_wins_by_agent()
    elif ch == 15:
        get_matches_between_two_teams()
    elif ch == 16:
        get_kd()
    else:
        print(bcolors.RED + "Error: Invalid Option" + bcolors.RESET)


password = getpass.getpass("Password: ")

# Global
while 1:
    tmp = sp.call("clear", shell=True)

    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password=password,
            db="VALORANTANALYZER",
            cursorclass=pymysql.cursors.DictCursor,
        )
        # tmp = sp.call('clear', shell=True)

        if con.open:
            print(bcolors.GREEN + "Connected" + bcolors.RESET)
        else:
            print(bcolors.RED + "Failed to connect" + bcolors.RESET)

        tmp = input(bcolors.YELLOW + "Enter any key to CONTINUE > " + bcolors.RESET)

        with con.cursor() as cur:
            while 1:
                tmp = sp.call("clear", shell=True)
                # Here taking example of Employee Mini-world
                print(bcolors.BLUE)
                print("1. Insert player into table")  # Hire an Employee
                print("2. Update player rating in table")  # Fire an Employee
                print("3. Update player region in table")  # Promote Employee
                print("4. Update the lore of given agent")  # Employee Statistics
                print("5. Delete player from database")
                print("6. Get total wins by agent")
                print("7. Get all teams a player has been a part of")
                print("8. Get all the matches a team has played")
                print("9. Get the round stats of a player")
                print("10. Get the signature abilities of an agent")
                print("11. Partial search match for agent")
                print("12. Partial search match for player name")
                print("13. Get total wins/losses of player")
                print("14. Get total wins/losses of a player for a particular agent")
                print("15. Get list of matches played between two teams")
                print("16. Get a list of all players with k/d >= x")
                print("17. Logout")
                print(bcolors.RESET)

                ch = int(input(bcolors.GREEN + "Enter choice > " + bcolors.RESET))
                tmp = sp.call("clear", shell=True)
                if ch == 20:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input(
                        bcolors.YELLOW + "Enter any key to CONTINUE > " + bcolors.RESET
                    )

    except Exception as e:
        tmp = sp.call("clear", shell=True)
        print(bcolors.RED)
        print("Error: Operation failed.")
        print(
            "Connection Refused: Either username or password is incorrect or user doesn't have access to database"
        )
        print(bcolors.RESET)
        tmp = input(bcolors.YELLOW + "Enter any key to CONTINUE > " + bcolors.RESET)
