import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error: {e}")
        raise  # Raising the exception to propagate the error

    return conn

def createUser(conn,name, discordId):
    crix = 500
    sql = ''' INSERT INTO user (name, crix, discordId)
              VALUES (?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, crix, discordId))
    conn.commit()
    return cur.lastrowid


def createPlayer(conn,playerID,playerName,valueCrix,position,photoLink,userId):
    crix = 500
    sql = ''' INSERT INTO players (playerID,playerName,valueCrix,position,photoLink,userId)
              VALUES (?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (playerID,playerName,valueCrix,position,photoLink,userId))
    conn.commit()
    return cur.lastrowid

def getUserId(conn,discordId):
    sql = ''' SELECT discordId FROM user WHERE discordId = ? '''
    cur = conn.cursor()
    cur.execute(sql, (discordId,))
    result = cur.fetchone()
    if result is None:
        return False
    else:
        return True

def getPlayerId(conn,playerID):
    sql = ''' SELECT playerId FROM players WHERE playerId = ? '''
    cur = conn.cursor()
    cur.execute(sql, (playerID,))
    result = cur.fetchone()
    if result is None:
        return False
    else:
        return True

def getAllPlayers(conn,userId):
    sql = ''' SELECT playerName FROM players WHERE userId = ? '''
    cur = conn.cursor()
    cur.execute(sql, (userId,))
    result = cur.fetchall()
    return [row[0] for row in result]

def getUserIdByPlayerName(conn,playerName):
    sql = ''' SELECT userId FROM players WHERE playerName == ? '''
    cur = conn.cursor()
    cur.execute(sql,(playerName,))
    result = cur.fetchone()
    return result

# Crix
def getCrix(conn,discordId):
    sql = ''' SELECT crix FROM user WHERE discordId = ? '''
    cur = conn.cursor()
    cur.execute(sql, (discordId,))
    result = cur.fetchone()
    return result[0]

def setCrix(conn,crix,discordId):
    sql = ''' UPDATE user SET crix = ? WHERE discordId = ? '''
    cur = conn.cursor()
    cur.execute(sql, (crix,discordId))
    result = cur.fetchone()
    return cur.lastrowid


