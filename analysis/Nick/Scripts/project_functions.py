{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (<ipython-input-81-6e3d4ff32374>, line 19)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-81-6e3d4ff32374>\"\u001b[0;36m, line \u001b[0;32m19\u001b[0m\n\u001b[0;31m    elif Position == 'SG':\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "def load_and_wrangle(csv_file):\n",
    "    players_stats_og = pd.read_csv(csv_file)\n",
    "    \n",
    "    players_stats_university = (\n",
    "        players_stats_og[players_stats_og['Collage'].notnull()]\n",
    "        .reset_index()\n",
    "        .drop(columns=['index']) \n",
    "        )\n",
    "\n",
    "    players_stats_university_wrangled = (\n",
    "        players_stats_university.drop(columns = ['BMI', 'Height', 'Weight', 'Birth_Place'])\n",
    "        .rename(columns={'Pos' : 'Position'})\n",
    "        .sort_values(by = 'Position', ascending=False)\n",
    "    )\n",
    "def filter_by_position(dataframe, Position):\n",
    "    \n",
    "    if Position == 'PG':\n",
    "        #x = PG's Weighted Score Calculation\n",
    "    elif Position == 'SG':\n",
    "        #x = players_stats_university_wrangled['column_name'] * weight + players_stats_university_wrangled['column_name'] * weight\n",
    "    elif Position == 'SF':\n",
    "        #x = players_stats_university_wrangled['column_name'] * weight + players_stats_university_wrangled['column_name'] * weight\n",
    "    elif Position == 'PF':\n",
    "        #x = players_stats_university_wrangled['column_name'] * weight + players_stats_university_wrangled['column_name'] * weight\n",
    "    elif Position == 'C':\n",
    "        #x = players_stats_university_wrangled['column_name'] * weight + players_stats_university_wrangled['column_name'] * weight\n",
    "    else:\n",
    "        return print(\"Invalid Position\")\n",
    "    \n",
    "    players_stats_university_wrangled_by_position = (\n",
    "        dataframe.loc[dataframe['Position'] == Position]\n",
    "        .sort_values(by = 'Name', ascending=True)\n",
    "        .reset_index()\n",
    "        .drop(columns=[x])\n",
    "        #.assign(Weighted_Score = x)\n",
    "        #.rename(columns={'Weighted_Score' : 'Weighted Score'})\n",
    "        )\n",
    "    return players_stats_university_wrangled_by_position\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
