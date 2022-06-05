from utils import *

def partial_search_agent(cur, con):
    try:
        agentInfo = TakeInput(["partial_agent_name"], ["VARCHAR"])
        query = "SELECT name FROM agent WHERE name LIKE '%%%s%%'" % (
            agentInfo["partial_agent_name"]
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + str(row["name"]) + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()


def partial_search_player(cur, con):
    try:
        playerInfo = TakeInput(["partial_player_name"], ["VARCHAR"])
        query = "SELECT name FROM player WHERE name LIKE '%%%s%%'" % (
            playerInfo["partial_player_name"]
        )
        cur.execute(query)
        retval = cur.fetchall()
        for row in retval:
            print(bcolors.PURPLE + str(row["name"]) + bcolors.RESET)
    except Exception as e:
        con.rollback()
        printError()



