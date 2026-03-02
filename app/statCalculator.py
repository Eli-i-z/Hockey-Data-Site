import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
playerData = pd.read_csv("app/nhldraft.csv", header=0)   # identify the header row

def getDefensiveGoals():
    defensivePlayers = playerData[playerData.iloc[:, 6] == "D"]
    defensiveGoals = defensivePlayers.iloc[:, 11].sum()
    return defensiveGoals
def getOffensiveGoals():
    offensivePlayers = playerData[playerData.iloc[:, 6] != "D"]
    offensiveGoals = offensivePlayers.iloc[:, 11].sum()
    return offensiveGoals
def getOffensivePlayers():
     offensivePlayers = len(playerData[playerData.iloc[:, 6] != "D"])
     return offensivePlayers
def getDefensivePlayers():
     defensivePlayers = len(playerData[playerData.iloc[:, 6] == "D"])
     return defensivePlayers
def getDeffensiveAssists():
    defensivePlayers = playerData[playerData.iloc[:, 6] == "D"]
    defensiveAssists = defensivePlayers.iloc[:, 12].sum()
    return defensiveAssists
def getOffensiveAssists():
    offensivePlayers = playerData[playerData.iloc[:, 6] != "D"]
    offensiveAssists = offensivePlayers.iloc[:, 12].sum()
    return offensiveAssists
