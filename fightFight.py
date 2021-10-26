import subprocess as sp
import pymysql
import pymysql.cursors
import getpass

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printError():
    print(bcolors.RED + "Error: Operation failed." + bcolors.RESET)

def TakeInput(items: list = [], Type: list = []):
    """Util function to quickly take input from user"""
    inputs = {}
    for idx, item in enumerate(items):
        val = input('Please enter ' + item +
                    ' (Type: ' + Type[idx] + '): ')
        inputs[item] = val
    return inputs

def get_teams_by_player():
    """Get the list of all teams the player has been a part of"""
    try:
        playerInfo = TakeInput(["Player Name", "Player Tag"], ["VARCHAR", "VARCHAR"])
        query = ("SELECT team_id FROM 5_stack_stats "
                    "WHERE player_name='%s' AND player_tag='%s'" % (playerInfo["Player Name"], playerInfo["Player Tag"]))
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + row['team_id'] + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()
    return

def get_matches_by_team():
    """Get the list of all the matches played by a team"""
    try:
        teamInfo = TakeInput(["team_id"], ["INT"])
        query = ("SELECT DISTINCT match_id FROM match_description "
                    "WHERE team_id='%s'" % (teamInfo["team_id"]))
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + row['match_id'] + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()
    return

def get_round_stats():
    """Get the list of all the round stats of a player for a particular match"""
    try:
        roundInfo = TakeInput(["player_name", "player_tag", "match_id"], ["VARCHAR", "VARCHAR", "INT"])
        query = ("SELECT round_no, kills, assists, deaths, damage_dealt, first_blood, planter, defuser "
                    "FROM round "
                    "WHERE player_name='%s' AND player_tag='%s' AND match_id='%s'" 
                    % (roundInfo["player_name"], roundInfo["player_tag"], roundInfo["match_id"]))
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
    query = ("SELECT agent_id, name FROM agent;")
    cur.execute(query)
    retval = cur.fetchall()
    for agent in retval:
        print(agent["name"])
        print("Signature abilities:")
        query = ("SELECT name FROM signature_ability WHERE agent_id = %d" % (agent["agent_id"]))
        cur.execute(query)
        namerows = cur.fetchall()
        for name in namerows:
            print(name["name"])
        print("")

def get_total_wins():
    """Get total wins and losses of a player"""
    playerName = input("Enter player name: ")
    playerTag = input("Enter player tag: ")
    query = ("SELECT SUM(team.wins) "
                "FROM team "
                "INNER JOIN 5_stack_stats")

def get_total_wins_by_agent():
    """Get total wins and losses of a player for a particular agent"""
    try:
        playerName = input("Enter player name: ")
        playerTag = input("Enter player tag: ")
        agentID = input("Enter agent ID: ")
        query = ("SELECT SUM(wins) FROM plays "
                    "WHERE player_name = '%s' AND player_tag = '%s"
                    % (playerName, playerTag))
        print(query)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()
    return

def insert_player():
    """Insert player into database"""
    try:
        playerInfo = TakeInput(["player_name", "player_tag", "date_of_birth", "time_played", "rank_rating", "region", "coach-name", "coach-tag"], ["VARCHAR", "VARCHAR", "DATE", "TIME", "INT", "VARCHAR", "VARCHAR", "VARCHAR"])
        query = ("INSERT INTO player VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s', '%s')" % (playerInfo["player_name"], playerInfo["player_tag"], playerInfo["date_of_birth"], playerInfo["time_played"], int(playerInfo["rank_rating"]), playerInfo["region"], playerInfo["coach-name"], playerInfo["coach-tag"]))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()

def update_player_rating():
    """Updater player rating entry in database"""
    try:
        playerInfo = TakeInput(["player_name", "player_tag", "updated_rating"], ["VARCHAR", "VARCHAR", "INT"])
        query = ("UPDATE player SET rank_rating = %d WHERE name = '%s' AND tag = '%s';" % (int(playerInfo["updated_rating"]), playerInfo["player_name"], playerInfo["player_tag"]))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()

def update_player_region():
    """Updater player rating entry in database"""
    try:
        playerInfo = TakeInput(["player_name", "player_tag", "updated_region"], ["VARCHAR", "VARCHAR", "VARCHAR"])
        query = ("UPDATE player SET region = '%s' WHERE name = '%s' AND tag = '%s';" % (playerInfo["updated_region"], playerInfo["player_name"], playerInfo["player_tag"]))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()

def update_agent_lore():
    """Update agent lore in database"""
    try:
        agentInfo = TakeInput(["agent_id", "updated_lore"], ["INT", "TEXT"])
        query = ("UPDATE agent SET lore = '%s' WHERE agent_id = %d;" % (agentInfo["updated_lore"], int(agentInfo["agent_id"])))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()

def delete_player():
    """Delete player entry from database"""
    try:
        playerInfo = TakeInput(["player_name", "player_tag"], ["VARCHAR", "VARCHAR"])
        query = ("DELETE FROM player WHERE name = '%s' AND tag = '%s'" % (playerInfo["player_name"], playerInfo["player_tag"]))
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        printError()

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    if(ch == 1):
        insert_player()
    elif(ch == 2):
        update_player_rating()
    elif(ch == 3):
        update_player_region()
    elif(ch == 4):
        update_agent_lore()
    elif(ch == 5):
        delete_player()
    elif(ch == 6):
        get_total_wins_by_agent()
    elif(ch == 7):
        get_teams_by_player()
    elif(ch == 8):
        get_matches_by_team()
    elif(ch == 9):
        get_round_stats()
    elif(ch == 10):
        get_agent_details()
    else:
        print(bcolors.RED + "Error: Invalid Option" + bcolors.RESET)


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    password = getpass.getpass("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password=password,
                              db='VALORANTANALYZER',
                              cursorclass=pymysql.cursors.DictCursor)
        # tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
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
                print("11. Logout")
                print(bcolors.RESET)

                ch = int(input(bcolors.GREEN + "Enter choice> " + bcolors.RESET))
                tmp = sp.call('clear', shell=True)
                if ch == 11:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input(bcolors.YELLOW + "Enter any key to CONTINUE>" + bcolors.RESET)

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(bcolors.RED)
        print("Error: Operation failed.")
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        print(bcolors.RESET)
        tmp = input(bcolors.YELLOW + "Enter any key to CONTINUE>" + bcolors.RESET)
