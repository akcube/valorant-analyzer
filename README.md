# Valorant Analyzer

## Team

- [Pramod Rao Budramane](https://github.com/PramodRaoB)
- [Vidit Jain](https://github.com/vidit-jain)
- [Kishore Kumar](https://github.com/akcube)

## Description

Developed fully functional CLI-interface database management system which allows users to create users, add matches to database, modify details, and query relevant stats to allow people to perform analysis for professional matches in the popular game [Valorant](https://playvalorant.com/).

![](Phases/image.png)

## Get Started

### Pre-requisites

This project requires [MySQL Server](https://wiki.archlinux.org/title/MySQL) to be installed. 

**apt**

```
sudo apt-get install mysql-server
```

**pacman**

```
sudo pacman -S mysql
```

If you run the Btrfs filesystem, you should consider disabling copy-on-write for the database directory for performance reasons

```
chattr +C /var/lib/mysql/
```

### Running MySQL

- Start MySQL by running the following command

  ``` 
  mysql -u <user_name> -p
  ```

  You will then be prompted to enter your password.

- Create a database named **VALORANTANALYZER** using the following commands. This will create a new user and grant access and modification priveleges to the new user.

  ```
  CREATE DATABASE VALORANTANALYZER CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  CREATE USER '<user>'@'localhost' IDENTIFIED BY '<password>';
  GRANT ALL PRIVILEGES ON dota.* TO '<user>'@'localhost';
  exit
  ```

- If you wish to, dump the sample database into **VALORANTANALYZER** from `core/SQL` 

  ```
   mysql -u <user> -p dota < dump.mysql
  ```

### Running the program

![warning](https://github.githubassets.com/images/icons/emoji/unicode/26a0.png) Using python 3 is heavily recommended. Older version might cause issues.

- To use the CLI, you must install the necessary modules. You may make a virtual environment for this. Note that you are quite free to omit this step.

  ```
  python3 -m venv <venv_name>
  source <venv_name>/bin/activate
  pip3 install -r requirements.txt
  ```

  - Next, create a `.env` file in `core/Python` and populate it with the following contents. Replace the relevant details.

    ```
    MYSQL_HOST=<host> # Usually localhost
    MYSQL_PORT=<port> # Usually 3306
    MYSQL_USER=<uname>
    ```

- Change directories to `core/Python` and run the program using
   ```
   python3 valorant_analyzer.py
   ```

## Using the program

### Basic functionalities

1. Insert player into table (inserts player into table)

2. Update player rating in table (updates a player rank rating after taking player name and tag)

3. Update player region in table (updates a players account region)

4. Update the lore of given agent (updates the lore of an agent)

5. Delete player from database (deletes player from the players database)

6. Get all teams a player has been a part of (lists all team ids of the player)

7. Get all the matches a team has played (lists all match ids of the team)

8. Get the signature abilities of an agent (names signature abilities of agent)

9. Partial search match for agent (returns all agent name matches to string passed)

10. Partial search match for player name (returns all player name matches to string passed)

11. Logout

### Analysis

1. Get the round stats of a player (lists all the relevant stats of a player in a round)

2. Get total wins/losses of player 

3. Get total wins/losses of a player for a particular agent

4. Get list of matches played between two teams (returns all match ids with both teams together)

5. Get a list of all players with k/d >= x

6. Get a list of all agents for a specific player with k/d >= x

7. Get a list of all agents for a specific player with winrate >= x
