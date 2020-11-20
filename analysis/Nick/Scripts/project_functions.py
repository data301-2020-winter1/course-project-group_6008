import pandas as pd

def load_and_process(url_or_csv_file):

    players_stats_og = pd.read_csv(url_or_csv_file) #Read in the csv file
    
    return players_stats_og
    
def filter_by_uni(DataFrame):
    
    players_stats_university = (
        DataFrame[DataFrame['Collage'].notnull()]
        #.rename(columns={'Collage':'College'}) TEST THIS !!!!!
        .reset_index()
        .drop(columns=['index']) 
        ) #Filter data to only players that attended a US college prior to getting drafted in the NBA
   
    players_stats_university_wrangled = (
        players_stats_university.rename(columns={'Pos' : 'Position'})
        .sort_values(by = 'Position', ascending=False)
        .reset_index()
        .drop(columns = ['BMI', 'Height', 'Weight', 'Birth_Place', 'index'])
        ) #Wrangle data and remove irrelevant columns 
    
    return players_stats_university_wrangled
    
def filter_by_position(DataFrame, Player_Position):
    
    players_stats_university_wrangled_by_position = (
        DataFrame.loc[DataFrame['Position'] == Player_Position]
        .sort_values(by = 'EFF', ascending=False)
        .reset_index()
        .drop(columns=['index'])
        )
    
    return players_stats_university_wrangled_by_position