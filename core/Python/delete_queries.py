from utils import *


def delete_player(cur, con):
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


