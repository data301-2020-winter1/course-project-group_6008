import pandas as pd

def load_and_process(url_or_csv_file, Player_Position):

    players_stats_og = pd.read_csv(url_or_csv_file) #Read in the csv file

    players_stats_university = (
        players_stats_og[players_stats_og['Collage'].notnull()]
        .reset_index()
        .drop(columns=['index']) 
        ) #Filter data to only players that attended a US college prior to getting drafted in the NBA
   
    players_stats_university_wrangled = (
        players_stats_university.rename(columns={'Pos' : 'Position'})
        .sort_values(by = 'Position', ascending=False)
        .reset_index()
        .drop(columns = ['BMI', 'Height', 'Weight', 'Birth_Place', 'index'])
        ) #Wrangle data and remove irrelevant columns 
    
    #if Player_Position == 'PG' x = 1
    #elif Player_Position == 'SG': x = 2
    #elif Player_Position == 'PF': x = 3
    #elif Player_Position == 'SF': x = 4
    #elif Player_Position == 'C':x = 5
    #else:print("Invalid Position")'
   
    players_stats_university_wrangled_by_position = (
        players_stats_university_wrangled.loc[players_stats_university_wrangled['Position'] == Player_Position]
        .sort_values(by = 'EFF', ascending=False)
        .reset_index()
        .drop(columns=['index'])
        ) #Filter data by player position and sort by their effeciency rating in descending order
    
    return players_stats_university_wrangled_by_position