import sqlite3
from sqlite3 import Error

def createPlayer(conn,playerID,playerName,valueCrix,position,photoLink,userId):
    crix = 500
    sql = ''' INSERT INTO players (playerID,playerName,valueCrix,position,photoLink,userId)
              VALUES (?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (playerID,playerName,valueCrix,position,photoLink,userId))
    conn.commit()
    return cur.lastrowid

def getPlayerId(conn,playerID):
    sql = ''' SELECT playerID FROM players WHERE playerID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (playerID,))
    result = cur.fetchone()
    if result is None:
        return False
    else:
        return True

def getPlayerIdByName(conn,playerName):
    sql = ''' SELECT playerId FROM players WHERE playerName = ? '''
    cur = conn.cursor()
    cur.execute(sql, (playerName,))
    result = cur.fetchone()
    return result[0]

def getAllPlayers(conn,userId):
    sql = ''' SELECT playerName FROM players WHERE userId = ? '''
    cur = conn.cursor()
    cur.execute(sql, (userId,))
    result = cur.fetchall()
    return [row[0] for row in result]

def getUserIdByPlayerName(conn,playerName):
    sql = ''' SELECT userId FROM players WHERE playerName = ? '''
    cur = conn.cursor()
    cur.execute(sql,(playerName,))
    result = cur.fetchone()
    if result is None:
        return "0"
    else:
        return result

def getUserIdByPlayerId(conn,playerId):
    sql = ''' SELECT userId FROM players WHERE playerID = ? '''
    cur = conn.cursor()
    cur.execute(sql,(playerId,))
    result = cur.fetchone()
    if result is None:
        return False
    else:
        return result

def setUserId(conn,playerId,userId):
    sql = ''' UPDATE players SET userId = ? WHERE playerID = ? '''
    cur = conn.cursor()
    cur.execute(sql,(userId,playerId,))
    result = cur.fetchone
    conn.commit()
    return cur.lastrowid

def getValueCrix(conn,playerName):
    sql = ''' SELECT valueCrix FROM players WHERE playerName = ? '''
    cur = conn.cursor()
    cur.execute(sql,(playerName,))
    result = cur.fetchone()
    return result[0]

def getPosition(conn,playerName):
    sql = ''' SELECT position FROM players WHERE playerName = ? '''
    cur = conn.cursor()
    cur.execute(sql,(playerName,))
    result = cur.fetchone()
    return result[0]

def removePlayer(conn,playerID):
    sql = ''' DELETE FROM players WHERE playerID = ? '''
    cur = conn.cursor()
    cur.execute(sql,(playerID,))
    conn.commit()
    return

def getCountPlayers(conn,userId):
    sql = ''' SELECT Count(playerID) FROM players WHERE userId = ? '''
    cur = conn.cursor()
    cur.execute(sql,(userId,))
    result = cur.fetchone()
    return result[0]