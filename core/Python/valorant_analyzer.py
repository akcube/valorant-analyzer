import subprocess as sp
import pymysql
import pymysql.cursors
import getpass
import os
from dotenv import load_dotenv

from utils import *

from create_queries import *
from read_queries import *
from update_queries import *
from delete_queries import *
from partial_search_queries import *

load_dotenv()
HOST = os.getenv("MYSQL_HOST")
USER = os.getenv("MYSQL_USER")
PORT = os.getenv("MYSQL_PORT")



def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    if ch == 1:
        insert_player(cur, con)
    elif ch == 2:
        update_player_rating(cur, con)
    elif ch == 3:
        update_player_region(cur, con)
    elif ch == 4:
        update_agent_lore(cur, con)
    elif ch == 5:
        delete_player(cur, con)
    elif ch == 6:
        get_teams_by_player(cur, con)
    elif ch == 7:
        get_matches_by_team(cur, con)
    elif ch == 8:
        get_round_stats(cur, con)
    elif ch == 9:
        get_agent_details(cur, con)
    elif ch == 10:
        partial_search_agent()
    elif ch == 11:
        partial_search_player()
    elif ch == 12:
        get_total_wins(cur, con)
    elif ch == 13:
        get_total_wins_by_agent(cur, con)
    elif ch == 14:
        get_matches_between_two_teams(cur, con)
    elif ch == 15:
        get_kd(cur, con)
    elif ch == 16:
        get_kd_for_agent(cur, con)
    elif ch == 17:
        get_winrate_for_agent(cur, con)
    else:
        print(bcolors.RED + "Error: Invalid Option" + bcolors.RESET)


# Global
while 1:
    password = getpass.getpass("Password: ")
    tmp = sp.call("clear", shell=True)

    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
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
                print("6. Get all teams a player has been a part of")
                print("7. Get all the matches a team has played")
                print("8. Get the round stats of a player")
                print("9. Get the signature abilities of an agent")
                print("10. Partial search match for agent")
                print("11. Partial search match for player name")
                print("12. Get total wins/losses of player")
                print("13. Get total wins/losses of a player for a particular agent")
                print("14. Get list of matches played between two teams")
                print("15. Get a list of all players with k/d >= x")
                print(
                    "16. Get a list of all agents for a specific player with k/d >= x"
                )
                print(
                    "17. Get a list of all agents for a specific player with winrate >= x"
                )
                print("18. Logout")
                print(bcolors.RESET)

                ch = int(input(bcolors.GREEN + "Enter choice > " + bcolors.RESET))
                tmp = sp.call("clear", shell=True)
                if ch == 18:
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
