from utils import *

def insert_player(cur, con):
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



