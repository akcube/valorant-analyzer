# Valorant Analyzer

# Team
- Pramod Rao Budramane
- Vidit Jain
- Kishore Kumar

## Description
Developed fully functional CLI-interface database management system which allows users to create users, add matches to database, modify details, and query relevant stats to allow people to perform analysis

### List of all commands
1. Insert player into table (inserts player into table)
2. Update player rating in table (updates a player rank rating after taking player name and tag)
3. Update player region in table (updates a players account region)
4. Update the lore of given agent (updates the lore of an agent)
5. Delete player from database (deletes player from the players database)
6. Get all teams a player has been a part of (lists all team ids of the player)
7. Get all the matches a team has played (lists all match ids of the team)
8. Get the round stats of a player (lists all the relevant stats of a player in a round)
9. Get the signature abilities of an agent (names signature abilities of agent)
10. Partial search match for agent (returns all agent name matches to string passed)
11. Partial search match for player name (returns all player name matches to string passed)
12. Get total wins/losses of player 
13. Get total wins/losses of a player for a particular agent
14. Get list of matches played between two teams (returns all match ids with both teams together)
15. Get a list of all players with k/d >= x
16. Get a list of all agents for a specific player with k/d >= x
17. Get a list of all agents for a specific player with winrate >= x
18. Logout

### Functional requirements demonstrated in the video attached

1. Insert player into table
    Inserts a entry with the given details into the player table of the database
2. Update player rating in table
    Updates the rating of an entry with the given details in the player table of the database
3. Update player region in table
    Updates the region of an entry with the given details in the player table of the database
4. Update the lore of a given agent
    Updates the lore of an entry with the given details in the agent table of the database
5. Delete player from database
    Deletes an entry with the given details from the players table of the database
6. Partial search match for player name
    Returns the list of player names from player table which contain the entered partial text as a substring
7. Partial search match for agent name
    Returns the list of agent names from agent table which contain the entered partial text as a substring
8. Get all teams a player has been a part of
    Returns the list of all team_ids which the entered player has been a part of
9. Get all matches a team has played
    Returns the list of all match_ids which the entered team_id has played in
10. Get the round stats of a player
    Returns the statistics of all round played by a particular player in a match
11. Get the signature abilities of an agent
    Lists all the signature abilities of the entered agent
12. Get total wins & losses of a player
    Prints the total wins and losses of the entered player
13. Get a list of all players with a k/d >= x
    Returns the list of all players with a k/d >= x
14. Get a list of all agents with a specific specific with a k/d >= x
    Returns the list of all agents of a specfic player with a k/d >= x
15. Get a list of all agents with a specific specific with a winrate >= x
    Returns the list of all agents of a specfic player with a winrate >= x
