{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Games Played</th>\n",
       "      <th>MIN</th>\n",
       "      <th>PTS</th>\n",
       "      <th>FGM</th>\n",
       "      <th>FGA</th>\n",
       "      <th>FG%</th>\n",
       "      <th>3PM</th>\n",
       "      <th>3PA</th>\n",
       "      <th>3P%</th>\n",
       "      <th>...</th>\n",
       "      <th>BLK</th>\n",
       "      <th>TOV</th>\n",
       "      <th>PF</th>\n",
       "      <th>EFF</th>\n",
       "      <th>AST/TOV</th>\n",
       "      <th>STL/TOV</th>\n",
       "      <th>Collage</th>\n",
       "      <th>Experience</th>\n",
       "      <th>Height</th>\n",
       "      <th>Pos</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>426</th>\n",
       "      <td>Shawne Williams</td>\n",
       "      <td>63</td>\n",
       "      <td>1087</td>\n",
       "      <td>341</td>\n",
       "      <td>121</td>\n",
       "      <td>300</td>\n",
       "      <td>40.3</td>\n",
       "      <td>64</td>\n",
       "      <td>178</td>\n",
       "      <td>36.0</td>\n",
       "      <td>...</td>\n",
       "      <td>21</td>\n",
       "      <td>30</td>\n",
       "      <td>135</td>\n",
       "      <td>383</td>\n",
       "      <td>1.47</td>\n",
       "      <td>0.83</td>\n",
       "      <td>Western Michigan University</td>\n",
       "      <td>0</td>\n",
       "      <td>207.5</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>414</th>\n",
       "      <td>Sean Kilpatrick</td>\n",
       "      <td>4</td>\n",
       "      <td>72</td>\n",
       "      <td>22</td>\n",
       "      <td>7</td>\n",
       "      <td>20</td>\n",
       "      <td>35.0</td>\n",
       "      <td>4</td>\n",
       "      <td>13</td>\n",
       "      <td>30.8</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>20</td>\n",
       "      <td>2.00</td>\n",
       "      <td>1.50</td>\n",
       "      <td>University of Cincinnati</td>\n",
       "      <td>0</td>\n",
       "      <td>190.0</td>\n",
       "      <td>SG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>199</th>\n",
       "      <td>JaMychal Green</td>\n",
       "      <td>24</td>\n",
       "      <td>164</td>\n",
       "      <td>62</td>\n",
       "      <td>27</td>\n",
       "      <td>47</td>\n",
       "      <td>57.4</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>5</td>\n",
       "      <td>14</td>\n",
       "      <td>25</td>\n",
       "      <td>85</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.36</td>\n",
       "      <td>University of Alabama</td>\n",
       "      <td>0</td>\n",
       "      <td>202.5</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>197</th>\n",
       "      <td>James Michael McAdoo</td>\n",
       "      <td>15</td>\n",
       "      <td>137</td>\n",
       "      <td>62</td>\n",
       "      <td>24</td>\n",
       "      <td>44</td>\n",
       "      <td>54.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>9</td>\n",
       "      <td>6</td>\n",
       "      <td>21</td>\n",
       "      <td>78</td>\n",
       "      <td>0.33</td>\n",
       "      <td>0.83</td>\n",
       "      <td>University of North Carolina</td>\n",
       "      <td>0</td>\n",
       "      <td>202.5</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>193</th>\n",
       "      <td>James Ennis III</td>\n",
       "      <td>62</td>\n",
       "      <td>1051</td>\n",
       "      <td>312</td>\n",
       "      <td>101</td>\n",
       "      <td>247</td>\n",
       "      <td>40.9</td>\n",
       "      <td>31</td>\n",
       "      <td>95</td>\n",
       "      <td>32.6</td>\n",
       "      <td>...</td>\n",
       "      <td>17</td>\n",
       "      <td>39</td>\n",
       "      <td>89</td>\n",
       "      <td>378</td>\n",
       "      <td>1.23</td>\n",
       "      <td>0.64</td>\n",
       "      <td>California State University, Long Beach</td>\n",
       "      <td>0</td>\n",
       "      <td>197.5</td>\n",
       "      <td>SF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>389</th>\n",
       "      <td>Raymond Felton</td>\n",
       "      <td>29</td>\n",
       "      <td>281</td>\n",
       "      <td>108</td>\n",
       "      <td>43</td>\n",
       "      <td>106</td>\n",
       "      <td>40.6</td>\n",
       "      <td>10</td>\n",
       "      <td>34</td>\n",
       "      <td>29.4</td>\n",
       "      <td>...</td>\n",
       "      <td>4</td>\n",
       "      <td>18</td>\n",
       "      <td>17</td>\n",
       "      <td>106</td>\n",
       "      <td>2.28</td>\n",
       "      <td>0.61</td>\n",
       "      <td>University of North Carolina</td>\n",
       "      <td>9</td>\n",
       "      <td>182.5</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>325</th>\n",
       "      <td>Marvin Williams</td>\n",
       "      <td>78</td>\n",
       "      <td>2035</td>\n",
       "      <td>577</td>\n",
       "      <td>210</td>\n",
       "      <td>495</td>\n",
       "      <td>42.4</td>\n",
       "      <td>95</td>\n",
       "      <td>265</td>\n",
       "      <td>35.8</td>\n",
       "      <td>...</td>\n",
       "      <td>36</td>\n",
       "      <td>60</td>\n",
       "      <td>146</td>\n",
       "      <td>798</td>\n",
       "      <td>1.67</td>\n",
       "      <td>1.15</td>\n",
       "      <td>University of North Carolina</td>\n",
       "      <td>9</td>\n",
       "      <td>202.5</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>205</th>\n",
       "      <td>Jarrett Jack</td>\n",
       "      <td>80</td>\n",
       "      <td>2241</td>\n",
       "      <td>957</td>\n",
       "      <td>359</td>\n",
       "      <td>817</td>\n",
       "      <td>43.9</td>\n",
       "      <td>39</td>\n",
       "      <td>146</td>\n",
       "      <td>26.7</td>\n",
       "      <td>...</td>\n",
       "      <td>13</td>\n",
       "      <td>191</td>\n",
       "      <td>143</td>\n",
       "      <td>987</td>\n",
       "      <td>1.95</td>\n",
       "      <td>0.39</td>\n",
       "      <td>Georgia Institute of Technology</td>\n",
       "      <td>9</td>\n",
       "      <td>187.5</td>\n",
       "      <td>PG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>206</th>\n",
       "      <td>Jason Maxiell</td>\n",
       "      <td>61</td>\n",
       "      <td>878</td>\n",
       "      <td>203</td>\n",
       "      <td>81</td>\n",
       "      <td>192</td>\n",
       "      <td>42.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>44</td>\n",
       "      <td>29</td>\n",
       "      <td>96</td>\n",
       "      <td>317</td>\n",
       "      <td>0.66</td>\n",
       "      <td>0.62</td>\n",
       "      <td>University of Cincinnati</td>\n",
       "      <td>9</td>\n",
       "      <td>197.5</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Brandon Bass</td>\n",
       "      <td>82</td>\n",
       "      <td>1929</td>\n",
       "      <td>866</td>\n",
       "      <td>344</td>\n",
       "      <td>683</td>\n",
       "      <td>50.4</td>\n",
       "      <td>9</td>\n",
       "      <td>32</td>\n",
       "      <td>28.1</td>\n",
       "      <td>...</td>\n",
       "      <td>32</td>\n",
       "      <td>83</td>\n",
       "      <td>140</td>\n",
       "      <td>974</td>\n",
       "      <td>1.25</td>\n",
       "      <td>0.49</td>\n",
       "      <td>Louisiana State University</td>\n",
       "      <td>9</td>\n",
       "      <td>200.0</td>\n",
       "      <td>PF</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>350 rows × 28 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Name  Games Played   MIN  PTS  FGM  FGA   FG%  3PM  3PA  \\\n",
       "426       Shawne Williams            63  1087  341  121  300  40.3   64  178   \n",
       "414       Sean Kilpatrick             4    72   22    7   20  35.0    4   13   \n",
       "199        JaMychal Green            24   164   62   27   47  57.4    0    6   \n",
       "197  James Michael McAdoo            15   137   62   24   44  54.5    0    0   \n",
       "193       James Ennis III            62  1051  312  101  247  40.9   31   95   \n",
       "..                    ...           ...   ...  ...  ...  ...   ...  ...  ...   \n",
       "389        Raymond Felton            29   281  108   43  106  40.6   10   34   \n",
       "325       Marvin Williams            78  2035  577  210  495  42.4   95  265   \n",
       "205          Jarrett Jack            80  2241  957  359  817  43.9   39  146   \n",
       "206         Jason Maxiell            61   878  203   81  192  42.2    0    0   \n",
       "49           Brandon Bass            82  1929  866  344  683  50.4    9   32   \n",
       "\n",
       "      3P%  ...  BLK  TOV   PF  EFF  AST/TOV  STL/TOV  \\\n",
       "426  36.0  ...   21   30  135  383     1.47     0.83   \n",
       "414  30.8  ...    0    2    3   20     2.00     1.50   \n",
       "199   0.0  ...    5   14   25   85     0.29     0.36   \n",
       "197   0.0  ...    9    6   21   78     0.33     0.83   \n",
       "193  32.6  ...   17   39   89  378     1.23     0.64   \n",
       "..    ...  ...  ...  ...  ...  ...      ...      ...   \n",
       "389  29.4  ...    4   18   17  106     2.28     0.61   \n",
       "325  35.8  ...   36   60  146  798     1.67     1.15   \n",
       "205  26.7  ...   13  191  143  987     1.95     0.39   \n",
       "206   0.0  ...   44   29   96  317     0.66     0.62   \n",
       "49   28.1  ...   32   83  140  974     1.25     0.49   \n",
       "\n",
       "                                     Collage  Experience  Height  Pos  \n",
       "426              Western Michigan University           0   207.5   PF  \n",
       "414                 University of Cincinnati           0   190.0   SG  \n",
       "199                    University of Alabama           0   202.5   PF  \n",
       "197             University of North Carolina           0   202.5   PF  \n",
       "193  California State University, Long Beach           0   197.5   SF  \n",
       "..                                       ...         ...     ...  ...  \n",
       "389             University of North Carolina           9   182.5   PG  \n",
       "325             University of North Carolina           9   202.5   PF  \n",
       "205          Georgia Institute of Technology           9   187.5   PG  \n",
       "206                 University of Cincinnati           9   197.5   PF  \n",
       "49                Louisiana State University           9   200.0   PF  \n",
       "\n",
       "[350 rows x 28 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    df = (pd.read_csv(url_or_path_to_csv_file)\n",
    "          .drop(columns = ['BMI','Weight','Team','Birth_Place','Birthdate','Age'])\n",
    "          .dropna()\n",
    "          .replace('R', '0')\n",
    "          .sort_values('Experience', ascending = True)\n",
    "         )\n",
    "    return df\n",
    "load_and_process('../../../data/raw/players_stats.csv')"
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
