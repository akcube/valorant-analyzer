from utils import *


def update_player_rating(cur, con):
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


def update_player_region(cur, con):
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


def update_agent_lore(cur, con):
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
