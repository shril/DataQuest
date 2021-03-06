
## <font color=blue>01 Getting to Know the Data</font>
  -  Using pandas, read in each of the four CSV files: <font color=red>game_log.csv, park_codes.csv, person_codes.csv, team_codes.csv</font>. For each:
    -  Use methods and attributes like <font color=red>DataFrame.shape, DataFrame.head()</font>, and <font color=red>DataFrame.tail()</font> to explore the data.
    -  Write a brief paragraph to describe each file, including for the helper files how the data intersects with the main log file.
  -  Research any fields you are not familiar with, using both the text file and Google as needed. In particular, you should explore and write a short paragraph on:
    -  What each defensive position number represents.
    -  The values in the various league fields, and which leagues they represent.


```python
# %matplotlib inline
import pandas as pd
import sqlite3

pd.set_option('max_columns', 180)
pd.set_option('max_rows', 200000)
pd.set_option('max_colwidth', 5000)

game_log = pd.read_csv('game_log.csv')
park_codes = pd.read_csv('park_codes.csv')
person_codes = pd.read_csv('person_codes.csv')
team_codes = pd.read_csv('team_codes.csv')
```

    /dataquest/system/env/python3/lib/python3.4/site-packages/IPython/core/interactiveshell.py:2723: DtypeWarning: Columns (12,13,14,15,19,20,81,82,83,84,85,86,87,88,93,94,95,96,97,98,99,100,105,106,108,109,111,112,114,115,117,118,120,121,123,124,126,127,129,130,132,133,135,136,138,139,141,142,144,145,147,148,150,151,153,154,156,157,160) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)



```python
print('Explore game_log data')
print('\ngame_log data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=game_log.shape[0], cols=game_log.shape[1]))
print('\ngame_log columns')
for col in game_log.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of game_log*****\n')
print(game_log.head(3))
print('\n\n\n*****Last 3 rows of game_log*****\n')
print(game_log.tail(3))
```

    Explore game_log data
    
    game_log data set size
    	Rows: 171907
    	Cols: 161
    
    game_log columns
    	- date
    	- number_of_game
    	- day_of_week
    	- v_name
    	- v_league
    	- v_game_number
    	- h_name
    	- h_league
    	- h_game_number
    	- v_score
    	- h_score
    	- length_outs
    	- day_night
    	- completion
    	- forefeit
    	- protest
    	- park_id
    	- attendance
    	- length_minutes
    	- v_line_score
    	- h_line_score
    	- v_at_bats
    	- v_hits
    	- v_doubles
    	- v_triples
    	- v_homeruns
    	- v_rbi
    	- v_sacrifice_hits
    	- v_sacrifice_flies
    	- v_hit_by_pitch
    	- v_walks
    	- v_intentional_walks
    	- v_strikeouts
    	- v_stolen_bases
    	- v_caught_stealing
    	- v_grounded_into_double
    	- v_first_catcher_interference
    	- v_left_on_base
    	- v_pitchers_used
    	- v_individual_earned_runs
    	- v_team_earned_runs
    	- v_wild_pitches
    	- v_balks
    	- v_putouts
    	- v_assists
    	- v_errors
    	- v_passed_balls
    	- v_double_plays
    	- v_triple_plays
    	- h_at_bats
    	- h_hits
    	- h_doubles
    	- h_triples
    	- h_homeruns
    	- h_rbi
    	- h_sacrifice_hits
    	- h_sacrifice_flies
    	- h_hit_by_pitch
    	- h_walks
    	- h_intentional_walks
    	- h_strikeouts
    	- h_stolen_bases
    	- h_caught_stealing
    	- h_grounded_into_double
    	- h_first_catcher_interference
    	- h_left_on_base
    	- h_pitchers_used
    	- h_individual_earned_runs
    	- h_team_earned_runs
    	- h_wild_pitches
    	- h_balks
    	- h_putouts
    	- h_assists
    	- h_errors
    	- h_passed_balls
    	- h_double_plays
    	- h_triple_plays
    	- hp_umpire_id
    	- hp_umpire_name
    	- 1b_umpire_id
    	- 1b_umpire_name
    	- 2b_umpire_id
    	- 2b_umpire_name
    	- 3b_umpire_id
    	- 3b_umpire_name
    	- lf_umpire_id
    	- lf_umpire_name
    	- rf_umpire_id
    	- rf_umpire_name
    	- v_manager_id
    	- v_manager_name
    	- h_manager_id
    	- h_manager_name
    	- winning_pitcher_id
    	- winning_pitcher_name
    	- losing_pitcher_id
    	- losing_pitcher_name
    	- saving_pitcher_id
    	- saving_pitcher_name
    	- winning_rbi_batter_id
    	- winning_rbi_batter_id_name
    	- v_starting_pitcher_id
    	- v_starting_pitcher_name
    	- h_starting_pitcher_id
    	- h_starting_pitcher_name
    	- v_player_1_id
    	- v_player_1_name
    	- v_player_1_def_pos
    	- v_player_2_id
    	- v_player_2_name
    	- v_player_2_def_pos
    	- v_player_3_id
    	- v_player_3_name
    	- v_player_3_def_pos
    	- v_player_4_id
    	- v_player_4_name
    	- v_player_4_def_pos
    	- v_player_5_id
    	- v_player_5_name
    	- v_player_5_def_pos
    	- v_player_6_id
    	- v_player_6_name
    	- v_player_6_def_pos
    	- v_player_7_id
    	- v_player_7_name
    	- v_player_7_def_pos
    	- v_player_8_id
    	- v_player_8_name
    	- v_player_8_def_pos
    	- v_player_9_id
    	- v_player_9_name
    	- v_player_9_def_pos
    	- h_player_1_id
    	- h_player_1_name
    	- h_player_1_def_pos
    	- h_player_2_id
    	- h_player_2_name
    	- h_player_2_def_pos
    	- h_player_3_id
    	- h_player_3_name
    	- h_player_3_def_pos
    	- h_player_4_id
    	- h_player_4_name
    	- h_player_4_def_pos
    	- h_player_5_id
    	- h_player_5_name
    	- h_player_5_def_pos
    	- h_player_6_id
    	- h_player_6_name
    	- h_player_6_def_pos
    	- h_player_7_id
    	- h_player_7_name
    	- h_player_7_def_pos
    	- h_player_8_id
    	- h_player_8_name
    	- h_player_8_def_pos
    	- h_player_9_id
    	- h_player_9_name
    	- h_player_9_def_pos
    	- additional_info
    	- acquisition_info
    
    
    
    *****First 3 rows of game_log*****
    
           date  number_of_game day_of_week v_name v_league  v_game_number h_name  \
    0  18710504               0         Thu    CL1      NaN              1    FW1   
    1  18710505               0         Fri    BS1      NaN              1    WS3   
    2  18710506               0         Sat    CL1      NaN              2    RC1   
    
      h_league  h_game_number  v_score  h_score  length_outs day_night completion  \
    0      NaN              1        0        2         54.0         D        NaN   
    1      NaN              1       20       18         54.0         D        NaN   
    2      NaN              1       12        4         54.0         D        NaN   
    
      forefeit protest park_id  attendance  length_minutes v_line_score  \
    0      NaN     NaN   FOR01       200.0           120.0    000000000   
    1      NaN     NaN   WAS01      5000.0           145.0    107000435   
    2      NaN     NaN   RCK01      1000.0           140.0    610020003   
    
      h_line_score  v_at_bats  v_hits  v_doubles  v_triples  v_homeruns  v_rbi  \
    0    010010000       30.0     4.0        1.0        0.0         0.0    0.0   
    1    640113030       41.0    13.0        1.0        2.0         0.0   13.0   
    2    010020100       49.0    11.0        1.0        1.0         0.0    8.0   
    
       v_sacrifice_hits  v_sacrifice_flies  v_hit_by_pitch  v_walks  \
    0               0.0                0.0             0.0      1.0   
    1               0.0                0.0             0.0     18.0   
    2               0.0                0.0             0.0      0.0   
    
       v_intentional_walks  v_strikeouts  v_stolen_bases  v_caught_stealing  \
    0                  NaN           6.0             1.0                NaN   
    1                  NaN           5.0             3.0                NaN   
    2                  NaN           1.0             0.0                NaN   
    
       v_grounded_into_double  v_first_catcher_interference  v_left_on_base  \
    0                    -1.0                           NaN             4.0   
    1                    -1.0                           NaN            12.0   
    2                    -1.0                           NaN            10.0   
    
       v_pitchers_used  v_individual_earned_runs  v_team_earned_runs  \
    0              1.0                       1.0                 1.0   
    1              1.0                       6.0                 6.0   
    2              1.0                       0.0                 0.0   
    
       v_wild_pitches  v_balks  v_putouts  v_assists  v_errors  v_passed_balls  \
    0             0.0      0.0       27.0        9.0       0.0             3.0   
    1             1.0      0.0       27.0       13.0      10.0             1.0   
    2             2.0      0.0       27.0       12.0       8.0             5.0   
    
       v_double_plays  v_triple_plays  h_at_bats  h_hits  h_doubles  h_triples  \
    0             0.0             0.0       31.0     4.0        1.0        0.0   
    1             2.0             0.0       49.0    14.0        2.0        0.0   
    2             0.0             0.0       36.0     7.0        2.0        1.0   
    
       h_homeruns  h_rbi  h_sacrifice_hits  h_sacrifice_flies  h_hit_by_pitch  \
    0         0.0    2.0               0.0                0.0             0.0   
    1         0.0   11.0               0.0                0.0             0.0   
    2         0.0    2.0               0.0                0.0             0.0   
    
       h_walks  h_intentional_walks  h_strikeouts  h_stolen_bases  \
    0      1.0                  NaN           0.0             0.0   
    1     10.0                  NaN           2.0             1.0   
    2      0.0                  NaN           3.0             5.0   
    
       h_caught_stealing  h_grounded_into_double  h_first_catcher_interference  \
    0                NaN                    -1.0                           NaN   
    1                NaN                    -1.0                           NaN   
    2                NaN                    -1.0                           NaN   
    
       h_left_on_base  h_pitchers_used  h_individual_earned_runs  \
    0             3.0              1.0                       0.0   
    1            14.0              1.0                       7.0   
    2             5.0              1.0                       3.0   
    
       h_team_earned_runs  h_wild_pitches  h_balks  h_putouts  h_assists  \
    0                 0.0             0.0      0.0       27.0        3.0   
    1                 7.0             0.0      0.0       27.0       20.0   
    2                 3.0             1.0      0.0       27.0       12.0   
    
       h_errors  h_passed_balls  h_double_plays  h_triple_plays hp_umpire_id  \
    0       3.0             1.0             1.0             0.0     boakj901   
    1      10.0             2.0             3.0             0.0     dobsh901   
    2      13.0             3.0             0.0             0.0     mawnj901   
    
      hp_umpire_name 1b_umpire_id 1b_umpire_name 2b_umpire_id 2b_umpire_name  \
    0     John Boake          NaN            NaN          NaN            NaN   
    1   Henry Dobson          NaN            NaN          NaN            NaN   
    2     J.H. Manny          NaN            NaN          NaN            NaN   
    
      3b_umpire_id 3b_umpire_name lf_umpire_id lf_umpire_name rf_umpire_id  \
    0          NaN            NaN          NaN            NaN          NaN   
    1          NaN            NaN          NaN            NaN          NaN   
    2          NaN            NaN          NaN            NaN          NaN   
    
      rf_umpire_name v_manager_id v_manager_name h_manager_id  h_manager_name  \
    0            NaN     paboc101  Charlie Pabor     lennb101     Bill Lennon   
    1            NaN     wrigh101   Harry Wright     younn801      Nick Young   
    2            NaN     paboc101  Charlie Pabor     hasts101  Scott Hastings   
    
      winning_pitcher_id winning_pitcher_name losing_pitcher_id  \
    0           mathb101        Bobby Mathews          prata101   
    1           spala101          Al Spalding          braia102   
    2           prata101             Al Pratt          fishc102   
    
      losing_pitcher_name saving_pitcher_id saving_pitcher_name  \
    0            Al Pratt               NaN                 NaN   
    1        Asa Brainard               NaN                 NaN   
    2     Cherokee Fisher               NaN                 NaN   
    
      winning_rbi_batter_id winning_rbi_batter_id_name v_starting_pitcher_id  \
    0                   NaN                        NaN              prata101   
    1                   NaN                        NaN              spala101   
    2                   NaN                        NaN              prata101   
    
      v_starting_pitcher_name h_starting_pitcher_id h_starting_pitcher_name  \
    0                Al Pratt              mathb101           Bobby Mathews   
    1             Al Spalding              braia102            Asa Brainard   
    2                Al Pratt              fishc102         Cherokee Fisher   
    
      v_player_1_id v_player_1_name  v_player_1_def_pos v_player_2_id  \
    0      whitd102    Deacon White                 2.0      kimbg101   
    1      wrigg101   George Wright                 6.0      barnr102   
    2      whitd102    Deacon White                 2.0      kimbg101   
    
      v_player_2_name  v_player_2_def_pos v_player_3_id v_player_3_name  \
    0    Gene Kimball                 4.0      paboc101   Charlie Pabor   
    1     Ross Barnes                 4.0      birdd102   Dave Birdsall   
    2    Gene Kimball                 4.0      paboc101   Charlie Pabor   
    
       v_player_3_def_pos v_player_4_id v_player_4_name  v_player_4_def_pos  \
    0                 7.0      allia101     Art Allison                 8.0   
    1                 9.0      mcvec101       Cal McVey                 2.0   
    2                 7.0      allia101     Art Allison                 8.0   
    
      v_player_5_id v_player_5_name  v_player_5_def_pos v_player_6_id  \
    0      white104     Elmer White                 9.0      prata101   
    1      wrigh101    Harry Wright                 8.0      goulc101   
    2      white104     Elmer White                 9.0      prata101   
    
      v_player_6_name  v_player_6_def_pos v_player_7_id v_player_7_name  \
    0        Al Pratt                 1.0      sutte101     Ezra Sutton   
    1   Charlie Gould                 3.0      schah101   Harry Schafer   
    2        Al Pratt                 1.0      sutte101     Ezra Sutton   
    
       v_player_7_def_pos v_player_8_id v_player_8_name  v_player_8_def_pos  \
    0                 5.0      carlj102    Jim Carleton                 3.0   
    1                 5.0      conef101       Fred Cone                 7.0   
    2                 5.0      carlj102    Jim Carleton                 3.0   
    
      v_player_9_id v_player_9_name  v_player_9_def_pos h_player_1_id  \
    0      bassj101       John Bass                 6.0      selmf101   
    1      spala101     Al Spalding                 1.0      watef102   
    2      bassj101       John Bass                 6.0      mackd101   
    
      h_player_1_name  h_player_1_def_pos h_player_2_id h_player_2_name  \
    0   Frank Sellman                 5.0      mathb101   Bobby Mathews   
    1   Fred Waterman                 5.0      forcd101      Davy Force   
    2      Denny Mack                 3.0      addyb101        Bob Addy   
    
       h_player_2_def_pos h_player_3_id  h_player_3_name  h_player_3_def_pos  \
    0                 1.0      foraj101        Jim Foran                 3.0   
    1                 6.0      mille105    Everett Mills                 3.0   
    2                 4.0      fishc102  Cherokee Fisher                 1.0   
    
      h_player_4_id  h_player_4_name  h_player_4_def_pos h_player_5_id  \
    0      goldw101  Wally Goldsmith                 6.0      lennb101   
    1      allid101     Doug Allison                 2.0      hallg101   
    2      hasts101   Scott Hastings                 8.0      ham-r101   
    
      h_player_5_name  h_player_5_def_pos h_player_6_id h_player_6_name  \
    0     Bill Lennon                 2.0      caret101       Tom Carey   
    1     George Hall                 7.0      leona101    Andy Leonard   
    2       Ralph Ham                 5.0      ansoc101       Cap Anson   
    
       h_player_6_def_pos h_player_7_id h_player_7_name  h_player_7_def_pos  \
    0                 4.0      mince101      Ed Mincher                 7.0   
    1                 4.0      braia102    Asa Brainard                 1.0   
    2                 2.0      sagep101      Pony Sager                 6.0   
    
      h_player_8_id  h_player_8_name  h_player_8_def_pos h_player_9_id  \
    0      mcdej101  James McDermott                 8.0      kellb105   
    1      burrh101  Henry Burroughs                 9.0      berth101   
    2      birdg101      George Bird                 7.0      stirg101   
    
       h_player_9_name  h_player_9_def_pos additional_info acquisition_info  
    0       Bill Kelly                 9.0             NaN                Y  
    1  Henry Berthrong                 8.0            HTBF                Y  
    2       Gat Stires                 9.0             NaN                Y  
    
    
    
    *****Last 3 rows of game_log*****
    
                date  number_of_game day_of_week v_name v_league  v_game_number  \
    171904  20161002               0         Sun    LAN       NL            162   
    171905  20161002               0         Sun    PIT       NL            162   
    171906  20161002               0         Sun    MIA       NL            161   
    
           h_name h_league  h_game_number  v_score  h_score  length_outs  \
    171904    SFN       NL            162        1        7         51.0   
    171905    SLN       NL            162        4       10         51.0   
    171906    WAS       NL            162        7       10         51.0   
    
           day_night completion forefeit protest park_id  attendance  \
    171904         D        NaN      NaN     NaN   SFO03     41445.0   
    171905         D        NaN      NaN     NaN   STL10     44615.0   
    171906         D        NaN      NaN     NaN   WAS11     28730.0   
    
            length_minutes v_line_score h_line_score  v_at_bats  v_hits  \
    171904           184.0    000100000    23000002x       30.0     4.0   
    171905           192.0    000020200    00100360x       35.0     9.0   
    171906           216.0    000230020    03023002x       38.0    14.0   
    
            v_doubles  v_triples  v_homeruns  v_rbi  v_sacrifice_hits  \
    171904        0.0        0.0         0.0    1.0               0.0   
    171905        0.0        0.0         1.0    4.0               0.0   
    171906        1.0        1.0         2.0    7.0               1.0   
    
            v_sacrifice_flies  v_hit_by_pitch  v_walks  v_intentional_walks  \
    171904                0.0             0.0      2.0                  0.0   
    171905                0.0             0.0      4.0                  0.0   
    171906                0.0             0.0      3.0                  2.0   
    
            v_strikeouts  v_stolen_bases  v_caught_stealing  \
    171904           7.0             0.0                0.0   
    171905          11.0             0.0                1.0   
    171906          10.0             1.0                1.0   
    
            v_grounded_into_double  v_first_catcher_interference  v_left_on_base  \
    171904                     1.0                           0.0             4.0   
    171905                     0.0                           0.0             8.0   
    171906                     1.0                           0.0             8.0   
    
            v_pitchers_used  v_individual_earned_runs  v_team_earned_runs  \
    171904              7.0                       7.0                 7.0   
    171905              6.0                       8.0                 8.0   
    171906              7.0                      10.0                10.0   
    
            v_wild_pitches  v_balks  v_putouts  v_assists  v_errors  \
    171904             0.0      0.0       24.0        5.0       1.0   
    171905             0.0      0.0       24.0        2.0       2.0   
    171906             1.0      0.0       24.0       11.0       0.0   
    
            v_passed_balls  v_double_plays  v_triple_plays  h_at_bats  h_hits  \
    171904             0.0             0.0             0.0       39.0    16.0   
    171905             0.0             0.0             0.0       36.0    12.0   
    171906             0.0             1.0             0.0       30.0    10.0   
    
            h_doubles  h_triples  h_homeruns  h_rbi  h_sacrifice_hits  \
    171904        3.0        1.0         0.0    7.0               0.0   
    171905        2.0        0.0         1.0   10.0               0.0   
    171906        2.0        0.0         1.0   10.0               1.0   
    
            h_sacrifice_flies  h_hit_by_pitch  h_walks  h_intentional_walks  \
    171904                0.0             0.0      4.0                  1.0   
    171905                2.0             0.0      4.0                  0.0   
    171906                1.0             1.0      8.0                  0.0   
    
            h_strikeouts  h_stolen_bases  h_caught_stealing  \
    171904          11.0             2.0                1.0   
    171905           5.0             0.0                0.0   
    171906           3.0             2.0                0.0   
    
            h_grounded_into_double  h_first_catcher_interference  h_left_on_base  \
    171904                     0.0                           0.0            12.0   
    171905                     0.0                           0.0             8.0   
    171906                     1.0                           0.0             7.0   
    
            h_pitchers_used  h_individual_earned_runs  h_team_earned_runs  \
    171904              2.0                       1.0                 1.0   
    171905              3.0                       4.0                 4.0   
    171906              6.0                       7.0                 7.0   
    
            h_wild_pitches  h_balks  h_putouts  h_assists  h_errors  \
    171904             0.0      0.0       27.0        7.0       0.0   
    171905             0.0      0.0       27.0        7.0       0.0   
    171906             1.0      0.0       27.0       11.0       0.0   
    
            h_passed_balls  h_double_plays  h_triple_plays hp_umpire_id  \
    171904             0.0             1.0             0.0     knigb901   
    171905             0.0             1.0             0.0     cuzzp901   
    171906             0.0             1.0             0.0     tumpj901   
    
           hp_umpire_name 1b_umpire_id 1b_umpire_name 2b_umpire_id 2b_umpire_name  \
    171904   Brian Knight     westj901       Joe West     fleta901  Andy Fletcher   
    171905     Phil Cuzzi     ticht901  Todd Tichenor     vanol901  Larry Vanover   
    171906   John Tumpane     porta901    Alan Porter     onorb901   Brian O'Nora   
    
           3b_umpire_id   3b_umpire_name lf_umpire_id lf_umpire_name rf_umpire_id  \
    171904     danlk901    Kerwin Danley          NaN            NaN          NaN   
    171905     marqa901  Alfonso Marquez          NaN            NaN          NaN   
    171906     kellj901     Jeff Kellogg          NaN            NaN          NaN   
    
           rf_umpire_name v_manager_id v_manager_name h_manager_id h_manager_name  \
    171904            NaN     robed001   Dave Roberts     bochb002    Bruce Bochy   
    171905            NaN     hurdc001   Clint Hurdle     mathm001   Mike Matheny   
    171906            NaN     mattd001  Don Mattingly     baked002    Dusty Baker   
    
           winning_pitcher_id winning_pitcher_name losing_pitcher_id  \
    171904           moorm003           Matt Moore          maedk001   
    171905           broxj001     Jonathan Broxton          nicaj001   
    171906           schem001         Max Scherzer          brica001   
    
           losing_pitcher_name saving_pitcher_id saving_pitcher_name  \
    171904         Kenta Maeda               NaN                 NaN   
    171905        Juan Nicasio               NaN                 NaN   
    171906        Austin Brice          melam001       Mark Melancon   
    
           winning_rbi_batter_id winning_rbi_batter_id_name v_starting_pitcher_id  \
    171904              poseb001               Buster Posey              maedk001   
    171905              piscs001           Stephen Piscotty              voger001   
    171906              difow001                Wilmer Difo              koeht001   
    
           v_starting_pitcher_name h_starting_pitcher_id h_starting_pitcher_name  \
    171904             Kenta Maeda              moorm003              Matt Moore   
    171905          Ryan Vogelsong              waina001         Adam Wainwright   
    171906             Tom Koehler              schem001            Max Scherzer   
    
           v_player_1_id v_player_1_name  v_player_1_def_pos v_player_2_id  \
    171904      kendh001  Howie Kendrick                 7.0      turnj001   
    171905      jasoj001       John Jaso                 3.0      polag001   
    171906      gordd002      Dee Gordon                 4.0      telit001   
    
            v_player_2_name  v_player_2_def_pos v_player_3_id   v_player_3_name  \
    171904    Justin Turner                 5.0      seagc001      Corey Seager   
    171905  Gregory Polanco                 9.0      mccua001  Andrew McCutchen   
    171906      Tomas Telis                 2.0      pradm001      Martin Prado   
    
            v_player_3_def_pos v_player_4_id   v_player_4_name  \
    171904                 6.0      puigy001       Yasiel Puig   
    171905                 8.0      kangj001      Jung Ho Kang   
    171906                 5.0      yelic001  Christian Yelich   
    
            v_player_4_def_pos v_player_5_id  v_player_5_name  v_player_5_def_pos  \
    171904                 9.0      gonza003  Adrian Gonzalez                 3.0   
    171905                 5.0      joycm001       Matt Joyce                 7.0   
    171906                 8.0      bourj002      Justin Bour                 3.0   
    
           v_player_6_id  v_player_6_name  v_player_6_def_pos v_player_7_id  \
    171904      grany001  Yasmani Grandal                 2.0      pedej001   
    171905      hansa001      Alen Hanson                 4.0      fryee001   
    171906      scrux001   Xavier Scruggs                 7.0      hoodd001   
    
           v_player_7_name  v_player_7_def_pos v_player_8_id     v_player_8_name  \
    171904    Joc Pederson                 8.0      utlec001         Chase Utley   
    171905      Eric Fryer                 2.0      florp001      Pedro Florimon   
    171906     Destin Hood                 9.0      hecha001  Adeiny Hechavarria   
    
            v_player_8_def_pos v_player_9_id v_player_9_name  v_player_9_def_pos  \
    171904                 4.0      maedk001     Kenta Maeda                 1.0   
    171905                 6.0      voger001  Ryan Vogelsong                 1.0   
    171906                 6.0      koeht001     Tom Koehler                 1.0   
    
           h_player_1_id h_player_1_name  h_player_1_def_pos h_player_2_id  \
    171904      spand001     Denard Span                 8.0      beltb001   
    171905      carpm002  Matt Carpenter                 3.0      diaza003   
    171906      turnt001     Trea Turner                 8.0      reveb001   
    
           h_player_2_name  h_player_2_def_pos h_player_3_id h_player_3_name  \
    171904    Brandon Belt                 3.0      poseb001    Buster Posey   
    171905    Aledmys Diaz                 6.0      moliy001   Yadier Molina   
    171906      Ben Revere                 7.0      harpb003    Bryce Harper   
    
            h_player_3_def_pos h_player_4_id   h_player_4_name  \
    171904                 2.0      pench001      Hunter Pence   
    171905                 2.0      piscs001  Stephen Piscotty   
    171906                 9.0      zimmr001    Ryan Zimmerman   
    
            h_player_4_def_pos h_player_5_id   h_player_5_name  \
    171904                 9.0      crawb001  Brandon Crawford   
    171905                 9.0      peraj001    Jhonny Peralta   
    171906                 3.0      drews001      Stephen Drew   
    
            h_player_5_def_pos h_player_6_id h_player_6_name  h_player_6_def_pos  \
    171904                 6.0      pagaa001     Angel Pagan                 7.0   
    171905                 5.0      mossb001    Brandon Moss                 7.0   
    171906                 5.0      difow001     Wilmer Difo                 4.0   
    
           h_player_7_id h_player_7_name  h_player_7_def_pos h_player_8_id  \
    171904      panij002       Joe Panik                 4.0      gillc001   
    171905      gyorj001     Jedd Gyorko                 4.0      gricr001   
    171906      espid001  Danny Espinosa                 6.0      lobaj001   
    
            h_player_8_name  h_player_8_def_pos h_player_9_id  h_player_9_name  \
    171904  Conor Gillaspie                 5.0      moorm003       Matt Moore   
    171905   Randal Grichuk                 8.0      waina001  Adam Wainwright   
    171906     Jose Lobaton                 2.0      schem001     Max Scherzer   
    
            h_player_9_def_pos additional_info acquisition_info  
    171904                 1.0             NaN                Y  
    171905                 1.0             NaN                Y  
    171906                 1.0             NaN                Y  



```python
!cat game_log_fields.txt
```

    Field(s)  Meaning
        1     Date in the form "yyyymmdd"
        2     Number of game:
                 "0" -- a single game
                 "1" -- the first game of a double (or triple) header
                        including seperate admission doubleheaders
                 "2" -- the second game of a double (or triple) header
                        including seperate admission doubleheaders
                 "3" -- the third game of a triple-header
                 "A" -- the first game of a double-header involving 3 teams
                 "B" -- the second game of a double-header involving 3 teams
        3     Day of week  ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
      4-5     Visiting team and league
        6     Visiting team game number
              For this and the home team game number, ties are counted as
              games and suspended games are counted from the starting
              rather than the ending date.
      7-8     Home team and league
        9     Home team game number
    10-11     Visiting and home team score (unquoted)
       12     Length of game in outs (unquoted).  A full 9-inning game would
              have a 54 in this field.  If the home team won without batting
              in the bottom of the ninth, this field would contain a 51.
       13     Day/night indicator ("D" or "N")
       14     Completion information.  If the game was completed at a
              later date (either due to a suspension or an upheld protest)
              this field will include:
                 "yyyymmdd,park,vs,hs,len" Where
              yyyymmdd -- the date the game was completed
              park -- the park ID where the game was completed
              vs -- the visitor score at the time of interruption
              hs -- the home score at the time of interruption
              len -- the length of the game in outs at time of interruption
              All the rest of the information in the record refers to the
              entire game.
       15     Forfeit information:
                 "V" -- the game was forfeited to the visiting team
                 "H" -- the game was forfeited to the home team
                 "T" -- the game was ruled a no-decision
       16     Protest information:
                 "P" -- the game was protested by an unidentified team
                 "V" -- a disallowed protest was made by the visiting team
                 "H" -- a disallowed protest was made by the home team
                 "X" -- an upheld protest was made by the visiting team
                 "Y" -- an upheld protest was made by the home team
              Note: two of these last four codes can appear in the field
              (if both teams protested the game).
       17     Park ID
       18     Attendance (unquoted)
       19     Time of game in minutes (unquoted)
    20-21     Visiting and home line scores.  For example:
                 "010000(10)0x"
              Would indicate a game where the home team scored a run in
              the second inning, ten in the seventh and didn't bat in the
              bottom of the ninth.
    22-38     Visiting team offensive statistics (unquoted) (in order):
                 at-bats
                 hits
                 doubles
                 triples
                 homeruns
                 RBI
                 sacrifice hits.  This may include sacrifice flies for years
                    prior to 1954 when sacrifice flies were allowed.
                 sacrifice flies (since 1954)
                 hit-by-pitch
                 walks
                 intentional walks
                 strikeouts
                 stolen bases
                 caught stealing
                 grounded into double plays
                 awarded first on catcher's interference
                 left on base
    39-43     Visiting team pitching statistics (unquoted)(in order):
                 pitchers used ( 1 means it was a complete game )
                 individual earned runs
                 team earned runs
                 wild pitches
                 balks
    44-49     Visiting team defensive statistics (unquoted) (in order):
                 putouts.  Note: prior to 1931, this may not equal 3 times
                    the number of innings pitched.  Prior to that, no
                    putout was awarded when a runner was declared out for
                    being hit by a batted ball.
                 assists
                 errors
                 passed balls
                 double plays
                 triple plays
    50-66     Home team offensive statistics
    67-71     Home team pitching statistics
    72-77     Home team defensive statistics
    78-79     Home plate umpire ID and name
    80-81     1B umpire ID and name
    82-83     2B umpire ID and name
    84-85     3B umpire ID and name
    86-87     LF umpire ID and name
    88-89     RF umpire ID and name
              If any umpire positions were not filled for a particular game
              the fields will be "","(none)".
    90-91     Visiting team manager ID and name
    92-93     Home team manager ID and name
    94-95     Winning pitcher ID and name
    96-97     Losing pitcher ID and name
    98-99     Saving pitcher ID and name--"","(none)" if none awarded
    100-101   Game Winning RBI batter ID and name--"","(none)" if none
              awarded
    102-103   Visiting starting pitcher ID and name
    104-105   Home starting pitcher ID and name
    106-132   Visiting starting players ID, name and defensive position,
              listed in the order (1-9) they appeared in the batting order.
    133-159   Home starting players ID, name and defensive position
              listed in the order (1-9) they appeared in the batting order.
      160     Additional information.  This is a grab-bag of informational
              items that might not warrant a field on their own.  The field 
              is alpha-numeric. Some items are represented by tokens such as:
                 "HTBF" -- home team batted first.
                 Note: if "HTBF" is specified it would be possible to see
                 something like "01002000x" in the visitor's line score.
              Changes in umpire positions during a game will also appear in 
              this field.  These will be in the form:
                 umpchange,inning,umpPosition,umpid with the latter three
                 repeated for each umpire.
              These changes occur with umpire injuries, late arrival of 
              umpires or changes from completion of suspended games. Details
              of suspended games are in field 14.
      161     Acquisition information:
                 "Y" -- we have the complete game
                 "N" -- we don't have any portion of the game
                 "D" -- the game was derived from box score and game story
                 "P" -- we have some portion of the game.  We may be missing
                        innings at the beginning, middle and end of the game.
     
    Missing fields will be NULL.
    

### <font color=blue>game_log Data Set description</font>
  1.  Columns: 161
  1.  Rows: 171,907
  1.  It looks like the combination of the <font color=red>*date*, *v_game_number*</font>, & <font color=red>*h_game_number*</font> columns can be used to make a PRIMARY KEY.
  1.  Columns 1 - 19 describe the game numbers, teams, datetime, the statium, ect...
  1.  Columns 20 - 161 have metrics that describe game play such as hit, home runs, doubles, ect...


```python
print('Explore park_codes data')
print('\npark_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=park_codes.shape[0], cols=park_codes.shape[1]))
print('\npark_codes columns')
for col in park_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of park_codes*****\n')
print(park_codes.head(3))
print('\n\n\n*****Last 3 rows of park_codes*****\n')
print(park_codes.tail(3))
print('\n\n\n****Lets Compare Park Codes from game_log*****\n')
print(game_log['park_id'].head(10))
```

    Explore park_codes data
    
    park_codes data set size
    	Rows: 252
    	Cols: 9
    
    park_codes columns
    	- park_id
    	- name
    	- aka
    	- city
    	- state
    	- start
    	- end
    	- league
    	- notes
    
    
    
    *****First 3 rows of park_codes*****
    
      park_id                      name                            aka     city  \
    0   ALB01            Riverside Park                            NaN   Albany   
    1   ALT01             Columbia Park                            NaN  Altoona   
    2   ANA01  Angel Stadium of Anaheim  Edison Field; Anaheim Stadium  Anaheim   
    
      state       start         end league  \
    0    NY  09/11/1880  05/30/1882     NL   
    1    PA  04/30/1884  05/31/1884     UA   
    2    CA  04/19/1966         NaN     AL   
    
                                                notes  
    0  TRN:9/11/80;6/15&9/10/1881;5/16-5/18&5/30/1882  
    1                                             NaN  
    2                                             NaN  
    
    
    
    *****Last 3 rows of park_codes*****
    
        park_id                                 name  aka       city state  \
    249   WOR01   Agricultural County Fair Grounds I  NaN  Worcester    MA   
    250   WOR02  Agricultural County Fair Grounds II  NaN  Worcester    MA   
    251   WOR03       Worcester Driving Park Grounds  NaN  Worcester    MA   
    
              start         end league       notes  
    249  05/01/1880  09/29/1882     NL         NaN  
    250  08/17/1887  08/17/1887     NL  1 BSN game  
    251  10/30/1874  10/30/1874    NaN  1 BS1 game  
    
    
    
    ****Lets Compare Park Codes from game_log*****
    
    0    FOR01
    1    WAS01
    2    RCK01
    3    CHI01
    4    TRO01
    5    CLE01
    6    CIN01
    7    FOR01
    8    FOR01
    9    BOS01
    Name: park_id, dtype: object


### <font color=blue>park_codes Data Set description</font>
  1.  Columns: 9
  1.  Rows: 252
  1.  It looks like the <font color=red>*park_id*</font> column can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
  1.  All of the columns have basic information to describe each park


```python
print('Explore person_codes data')
print('\nperson_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=person_codes.shape[0], cols=person_codes.shape[1]))
print('\nperson_codes columns')
for col in person_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of person_codes*****\n')
print(person_codes.head(3))
print('\n\n\n*****Last 3 rows of person_codes*****\n')
print(person_codes.tail(3))
```

    Explore person_codes data
    
    person_codes data set size
    	Rows: 20494
    	Cols: 7
    
    person_codes columns
    	- id
    	- last
    	- first
    	- player_debut
    	- mgr_debut
    	- coach_debut
    	- ump_debut
    
    
    
    *****First 3 rows of person_codes*****
    
             id     last   first player_debut mgr_debut coach_debut ump_debut
    0  aardd001  Aardsma   David   04/06/2004       NaN         NaN       NaN
    1  aaroh101    Aaron    Hank   04/13/1954       NaN         NaN       NaN
    2  aarot101    Aaron  Tommie   04/10/1962       NaN  04/06/1979       NaN
    
    
    
    *****Last 3 rows of person_codes*****
    
                 id      last  first player_debut mgr_debut coach_debut ump_debut
    20491  zwild101  Zwilling  Dutch   08/14/1910       NaN  04/15/1941       NaN
    20492  zycht001      Zych   Tony   09/04/2015       NaN         NaN       NaN
    20493  thoma102  Thompson    NaN          NaN       NaN         NaN       NaN


### <font color=blue>person_codes Data Set description</font>
  1.  Columns: 7
  1.  Rows: 20494
  1.  It looks like the <font color=red>*id*</font> column can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
  1.  However, the relationship looks to be a bit more complex than in many cases.  There are a multidue of columns were the game_log data set refererences a persion via their id.  Any time a given statistic in a game is linked back to a specific person their person_codes id is utilized.
  1.  The person_codes columns provide the person's first and last names.  As well as their debut dates as a player, manager, coach, or ump.


```python
print('Explore team_codes data')
print('\nteam_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=team_codes.shape[0], cols=team_codes.shape[1]))

print(team_codes['team_id'].value_counts())
print(team_codes['team_id'].value_counts().shape)
print(team_codes[team_codes['team_id'] == 'MIL'])

print('\nteam_codes columns')
for col in team_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of team_codes*****\n')
print(team_codes.head(3))
print('\n\n\n*****Last 3 rows of team_codes*****\n')
print(team_codes.tail(3))
```

    Explore team_codes data
    
    team_codes data set size
    	Rows: 150
    	Cols: 8
    MIL    2
    TRO    1
    WSN    1
    KC2    1
    CL3    1
    SPU    1
    SLN    1
    BL1    1
    PHU    1
    CN1    1
    SL3    1
    NEW    1
    KCF    1
    MLU    1
    CIN    1
    BFN    1
    SDN    1
    IN2    1
    CH2    1
    LS2    1
    TRN    1
    KCU    1
    PH3    1
    FLO    1
    ML2    1
    ARI    1
    BFP    1
    PH4    1
    SL1    1
    DTN    1
    PTP    1
    HOU    1
    COL    1
    MID    1
    MLN    1
    LS1    1
    PRO    1
    LAA    1
    BRP    1
    ML3    1
    PHI    1
    BLF    1
    SE1    1
    CLP    1
    BS1    1
    BLA    1
    NYN    1
    BLU    1
    PHP    1
    BR1    1
    SFN    1
    WOR    1
    BL2    1
    SLA    1
    HR1    1
    WS9    1
    IND    1
    SEA    1
    LAN    1
    BR3    1
    ANA    1
    PIT    1
    CLE    1
    CL6    1
    SL5    1
    BR4    1
    TL1    1
    BRF    1
    IN1    1
    CL2    1
    BS2    1
    BAL    1
    PTF    1
    CN2    1
    WS2    1
    RC1    1
    SL2    1
    SR2    1
    PTU    1
    WS4    1
    WS6    1
    CNU    1
    IN3    1
    WS5    1
    WS8    1
    MIA    1
    CHP    1
    BSP    1
    CH1    1
    CHF    1
    PH2    1
    WSU    1
    TBA    1
    WS3    1
    KEO    1
    SLU    1
    SLF    1
    NY2    1
    CHN    1
    NY4    1
    CL5    1
    WIL    1
    KC1    1
    PHA    1
    HAR    1
    BUF    1
    CHU    1
    BL4    1
    NY1    1
    RC2    1
    SR1    1
    WS1    1
    ELI    1
    BRO    1
    NY3    1
    CAL    1
    MIN    1
    OAK    1
    CN3    1
    BSU    1
    MLA    1
    TEX    1
    TL2    1
    PHN    1
    NYA    1
    ATL    1
    PH1    1
    CHA    1
    BLN    1
    KCA    1
    BR2    1
    CL4    1
    CL1    1
    TOR    1
    DET    1
    RIC    1
    NH1    1
    KCN    1
    NYP    1
    BOS    1
    LS3    1
    WS7    1
    MON    1
    BSN    1
    FW1    1
    WAS    1
    PT1    1
    ALT    1
    SL4    1
    Name: team_id, dtype: int64
    (149,)
        team_id league  start   end       city nickname franch_id  seq
    112     MIL     AL   1970  1997  Milwaukee  Brewers       SE1    2
    113     MIL     NL   1998     0  Milwaukee  Brewers       SE1    3
    
    team_codes columns
    	- team_id
    	- league
    	- start
    	- end
    	- city
    	- nickname
    	- franch_id
    	- seq
    
    
    
    *****First 3 rows of team_codes*****
    
      team_id league  start   end     city         nickname franch_id  seq
    0     ALT     UA   1884  1884  Altoona  Mountain Cities       ALT    1
    1     ARI     NL   1998     0  Arizona     Diamondbacks       ARI    1
    2     BFN     NL   1879  1885  Buffalo           Bisons       BFN    1
    
    
    
    *****Last 3 rows of team_codes*****
    
        team_id league  start   end        city   nickname franch_id  seq
    147     WSN     NL   1892  1899  Washington   Senators       WS9    2
    148     WSU     UA   1884  1884  Washington  Nationals       WSU    1
    149     MIA     NL   2012     0       Miami    Marlins       FLO    2


### <font color=blue>team_codes Data Set description</font>
  1.  Columns: 8
  1.  Rows: 150
  1.  It looks like the <font color=red>*team_id*</font> and  <font color=red>*league*</font> columns can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
  1.  The relationship can be made between the team_codes.team_id column and the  game_log.v_name and game_log.v_league or game_log.h_name and game_log.h_league columns.
  1.  Furthermore, a recursive relationship exists using the franch_id.  It is necessary because it some franchises have have multiple entries if they've switched from one league to another.
    1.  I noticed this with MIL, however the Houston Astros are another team that has switch leagues, but that is not captured in this dataset.  Perhaps the data set is not up to date.
  1.  The team_codes has some basic info on each team:
    1.  Team foundation and terminations dates
    1.  league
    1.  Location
    1.  Nickname
    1.  I'm not sure what the seq columns is for.

## <font color=blue>02 Importing Data into SQLite</font>
  -  Recreate the <font color=red>*run_command()*</font> and <font color=red>*run_query()*</font> functions from the previous guided project, which you can use.
  -  Use <font color=red>*DataFrame.to_sql()*</font> to create tables for each of our dataframes in a new SQLite database, <font color=red>*mlb.db*</font>:
    -  The table name should be the same as each of the CSV filename without the extension, eg <font color=red>*game_log.csv*</font> should be imported to a table called <font color=red>*game_log*</font>.
  -  Using <font color=red>*run_command()*</font>, create a new column in the <font color=red>*game_log*</font> table called <font color=red>*game_id*</font>. The following game_log columns should be conconated:
    1.  <font color=red>*h_name*</font>
    1.  <font color=red>*date*</font> in the following format (yyyymmdd)
    1.  <font color=red>*number_of_game*</font>
    1.  Here's an example of the conconated column (Atlanta Braves - April 8, 1983 - Game 0):
      *  ATL198304080


```python
def run_query(query):
    with sqlite3.connect('mlb.db') as conn:
        return pd.read_sql_query(query, conn)

def run_command(command):
    with sqlite3.connect('mlb.db') as conn:
        conn.isolation_level = None # tells SQLite to autocommit any changes
        conn.execute(command)
        
def create_DF_table(df, tablename):
    with sqlite3.connect('mlb.db') as conn:
        conn.execute("DROP TABLE IF EXISTS {};".format(tablename))
        df.to_sql(tablename, conn, flavor='sqlite', index=False)

def show_tables():
    with sqlite3.connect('mlb.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [str('%s' % x) for x in cur.fetchall()]
    
def show_columns(tablename):
    # This work but it's too easy to over load Jupyter Notebook
    with sqlite3.connect('mlb.db') as conn:
        conn.isolation_level = None # tells SQLite to autocommit any changes
        column_query = conn.execute('SELECT * from {tab};'.format(tab=tablename))
        return [description[0] for description in column_query.description]
```


```python
create_DF_table(game_log, 'game_log')
create_DF_table(park_codes, 'park_codes')
create_DF_table(person_codes, 'person_codes')
create_DF_table(team_codes, 'team_codes')
```

    /dataquest/system/env/python3/lib/python3.4/site-packages/pandas/io/sql.py:525: FutureWarning: the 'flavor' parameter is deprecated and will be removed in a future version, as 'sqlite' is the only supported option when SQLAlchemy is not installed.
      _validate_flavor_parameter(flavor)



```python
tables = show_tables()
for t in tables:
    print(t)
```

    person
    park
    league
    appearance_type
    team
    game
    team_appearance
    person_appearance
    game_log
    park_codes
    person_codes
    team_codes



```python
run_command('ALTER TABLE game_log ADD COLUMN game_id TEXT;')

update_query = '''
UPDATE game_log 
SET game_id = h_name || date || number_of_game
WHERE game_id IS Null;
'''
run_command(update_query)
run_query('SELECT game_id, h_name, date, number_of_game \
                FROM game_log LIMIT 10;')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>game_id</th>
      <th>h_name</th>
      <th>date</th>
      <th>number_of_game</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FW1187105040</td>
      <td>FW1</td>
      <td>18710504</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WS3187105050</td>
      <td>WS3</td>
      <td>18710505</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RC1187105060</td>
      <td>RC1</td>
      <td>18710506</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CH1187105080</td>
      <td>CH1</td>
      <td>18710508</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TRO187105090</td>
      <td>TRO</td>
      <td>18710509</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CL1187105110</td>
      <td>CL1</td>
      <td>18710511</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CL1187105130</td>
      <td>CL1</td>
      <td>18710513</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>FW1187105130</td>
      <td>FW1</td>
      <td>18710513</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>FW1187105150</td>
      <td>FW1</td>
      <td>18710515</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BS1187105160</td>
      <td>BS1</td>
      <td>18710516</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>03 Looing for Normalization Opportunities</font>
  -  Looking at the various files, look for opportunities to normalize the data and record your observations in a markdown cell.
  
#### <font color=blue>The following are opportunities for normalization of our data:</font>
  -  In person_codes, all the debut dates will be able to be reproduced using game log data.
  -  In team_codes, the start, end and sequence columns will be able to be reproduced using game log data.
  -  In park_codes, the start and end years will be able to be reproduced using game log data. While technically the state is an attribute of the city, we might not want to have a an incomplete city/state table so we will leave this in.
  -  There are lots of places in game log where we have a player ID followed by the players name. We will be able to remove this and use the name data in person_codes
  -  In game_log, all offensive and defensive stats are repeated for the home team and the visiting team. We could break these out and have a table that lists each game twice, one for each team, and cut out this column repetition.
  -  Similarly, in game_log, we have a listing for 9 players on each team with their positions - we can remove these and have one table that tracks player appearances and their positions.
  -  We can do a similar thing with the umpires from game_log, instead of listing all four positions as columns, we can put the umpires either in their own table or make one table for players, umpires and managers.
  -  We have several awards in game_log like winning pitcher and losing pitcher. We can either break these out into their own table, have a table for awards, or combine the awards in with general appearances like the players and umpires.

## <font color=blue>04 Planning a Normalized Schema</font>

The best way to work visually with a schema diagram, just like the ones we've used so far in this course. Start by creating a diagram of the four existing tables and their columns, and then gradually create new tables that move the data into a more normalized state.

Some people like to do this on paper, others use diagramming tools like Sketch or Figma, others like using Photoshop or similar. Our recommendation is that the best way to do this is using a schema designing tool like [DbDesigner.net](https://dbdesigner.net/). This free tool allows you to create a schema and will create lines to show foreign key relations clearly.

#### <font color=blue>mlb DB Normalized Schema</font>

![mlb.db Schema](https://s3.amazonaws.com/dq-content/193/mlb_schema.svg)

## <font color=blue>05 Create Tables w/o Foreign Relations</font>
  -  Create the <font color=red>*person*</font> table with columns and primary key as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Insert the data from the <font color=red>*person_codes*</font> table.
    -  Write a query to display the first few rows of the table.
  -  Create the <font color=red>*park*</font> table with columns and primary key as shown in the schema diagram.
    -  Select the appropriate type based on the data
    -  Insert the data from the <font color=red>*park_codes*</font> table.
    -  Write a query to display the first few rows of the table.
  -  Create the <font color=red>*league*</font> table with columns and primary key as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Insert the data manually based on your research on the names of the six league IDs.
    -  Write a query to display the table.
  -  Create the <font color=red>*appearance_type*</font> table with columns and primary key as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Import and insert the data from <font color=red>*appearance_type.csv*</font>.
    -  Write a query to display the table.


```python
c1 = """
CREATE TABLE IF NOT EXISTS person (
    person_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
"""

c2 = """
INSERT OR IGNORE INTO person
SELECT
    id,
    first,
    last
FROM person_codes;
"""

q = """
SELECT * FROM person
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>aardd001</td>
      <td>David</td>
      <td>Aardsma</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aaroh101</td>
      <td>Hank</td>
      <td>Aaron</td>
    </tr>
    <tr>
      <th>2</th>
      <td>aarot101</td>
      <td>Tommie</td>
      <td>Aaron</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aased001</td>
      <td>Don</td>
      <td>Aase</td>
    </tr>
    <tr>
      <th>4</th>
      <td>abada001</td>
      <td>Andy</td>
      <td>Abad</td>
    </tr>
  </tbody>
</table>
</div>




```python
c1 = """
CREATE TABLE IF NOT EXISTS park (
    park_id TEXT PRIMARY KEY,
    name TEXT,
    nickname TEXT,
    city TEXT,
    state TEXT,
    notes TEXT
);
"""

c2 = """
INSERT OR IGNORE INTO park
SELECT
    park_id,
    name,
    aka,
    city,
    state,
    notes
FROM park_codes;
"""

q = """
SELECT * FROM park
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>park_id</th>
      <th>name</th>
      <th>nickname</th>
      <th>city</th>
      <th>state</th>
      <th>notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ALB01</td>
      <td>Riverside Park</td>
      <td>None</td>
      <td>Albany</td>
      <td>NY</td>
      <td>TRN:9/11/80;6/15&amp;9/10/1881;5/16-5/18&amp;5/30/1882</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ALT01</td>
      <td>Columbia Park</td>
      <td>None</td>
      <td>Altoona</td>
      <td>PA</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ANA01</td>
      <td>Angel Stadium of Anaheim</td>
      <td>Edison Field; Anaheim Stadium</td>
      <td>Anaheim</td>
      <td>CA</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ARL01</td>
      <td>Arlington Stadium</td>
      <td>None</td>
      <td>Arlington</td>
      <td>TX</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ARL02</td>
      <td>Rangers Ballpark in Arlington</td>
      <td>The Ballpark in Arlington; Ameriquest Fl</td>
      <td>Arlington</td>
      <td>TX</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
c1 = """
CREATE TABLE IF NOT EXISTS league (
    league_id TEXT PRIMARY KEY,
    name TEXT
);
"""

c2 = """
INSERT OR IGNORE INTO league
VALUES
    ("NL", "National League"),
    ("AL", "American League"),
    ("AA", "American Association"),
    ("FL", "Federal League"),
    ("PL", "Players League"),
    ("UA", "Union Association")
;
"""

q = """
SELECT * FROM league
"""

run_command(c1)
run_command(c2)
run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>league_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NL</td>
      <td>National League</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AL</td>
      <td>American League</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AA</td>
      <td>American Association</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FL</td>
      <td>Federal League</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PL</td>
      <td>Players League</td>
    </tr>
    <tr>
      <th>5</th>
      <td>UA</td>
      <td>Union Association</td>
    </tr>
  </tbody>
</table>
</div>




```python
c1 = "DROP TABLE IF EXISTS appearance_type;"

run_command(c1)

c2 = """
CREATE TABLE appearance_type (
    appearance_type_id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT
);
"""
run_command(c2)

appearance_type = pd.read_csv('appearance_type.csv')

with sqlite3.connect('mlb.db') as conn:
    appearance_type.to_sql('appearance_type',
                           conn,
                           index=False,
                           if_exists='append')

q = """
SELECT * FROM appearance_type;
"""

run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>appearance_type_id</th>
      <th>name</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>O1</td>
      <td>Batter 1</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>1</th>
      <td>O2</td>
      <td>Batter 2</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>2</th>
      <td>O3</td>
      <td>Batter 3</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>3</th>
      <td>O4</td>
      <td>Batter 4</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>4</th>
      <td>O5</td>
      <td>Batter 5</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>5</th>
      <td>O6</td>
      <td>Batter 6</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>6</th>
      <td>O7</td>
      <td>Batter 7</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>7</th>
      <td>O8</td>
      <td>Batter 8</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>8</th>
      <td>O9</td>
      <td>Batter 9</td>
      <td>offense</td>
    </tr>
    <tr>
      <th>9</th>
      <td>D1</td>
      <td>Pitcher</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>10</th>
      <td>D2</td>
      <td>Catcher</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>11</th>
      <td>D3</td>
      <td>1st Base</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>12</th>
      <td>D4</td>
      <td>2nd Base</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>13</th>
      <td>D5</td>
      <td>3rd Base</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>14</th>
      <td>D6</td>
      <td>Shortstop</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>15</th>
      <td>D7</td>
      <td>Left Field</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>16</th>
      <td>D8</td>
      <td>Center Field</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>17</th>
      <td>D9</td>
      <td>Right Field</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>18</th>
      <td>D10</td>
      <td>Unknown Position</td>
      <td>defense</td>
    </tr>
    <tr>
      <th>19</th>
      <td>UHP</td>
      <td>Home Plate</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>20</th>
      <td>U1B</td>
      <td>First Base</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>21</th>
      <td>U2B</td>
      <td>Second Base</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>22</th>
      <td>U3B</td>
      <td>Third Base</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>23</th>
      <td>ULF</td>
      <td>Left Field</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>24</th>
      <td>URF</td>
      <td>Right Field</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MM</td>
      <td>Manager</td>
      <td>manager</td>
    </tr>
    <tr>
      <th>26</th>
      <td>AWP</td>
      <td>Winning Pitcher</td>
      <td>award</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ALP</td>
      <td>Losing Pitcher</td>
      <td>award</td>
    </tr>
    <tr>
      <th>28</th>
      <td>ASP</td>
      <td>Saving Pitcher</td>
      <td>award</td>
    </tr>
    <tr>
      <th>29</th>
      <td>AWB</td>
      <td>Winning RBI Batter</td>
      <td>award</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PSP</td>
      <td>Starting Pitcher</td>
      <td>pitcher</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>06 Adding The Team and Game Tables</font>
  -  Create the team <font color=red>*table*</font> with columns, primary key, and foreign key as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Insert the data from the <font color=red>*team_codes*</font> table.
    -  Write a query to display the first few rows of the table.
  -  Create the <font color=red>*game table*</font> with columns, primary key, and foreign key as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Insert the data from the <font color=red>*game_log*</font> table.
    -  Write a query to display the first few rows of the table.


```python
c1 = """
CREATE TABLE IF NOT EXISTS team (
    team_id TEXT PRIMARY KEY,
    league_id TEXT,
    city TEXT,
    nickname TEXT,
    franch_id TEXT,
    FOREIGN KEY (league_id) REFERENCES league(league_id)
);
"""

c2 = """
INSERT OR IGNORE INTO team
SELECT
    team_id,
    league,
    city,
    nickname,
    franch_id
FROM team_codes;
"""

q = """
SELECT * FROM team
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team_id</th>
      <th>league_id</th>
      <th>city</th>
      <th>nickname</th>
      <th>franch_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ALT</td>
      <td>UA</td>
      <td>Altoona</td>
      <td>Mountain Cities</td>
      <td>ALT</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ARI</td>
      <td>NL</td>
      <td>Arizona</td>
      <td>Diamondbacks</td>
      <td>ARI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BFN</td>
      <td>NL</td>
      <td>Buffalo</td>
      <td>Bisons</td>
      <td>BFN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BFP</td>
      <td>PL</td>
      <td>Buffalo</td>
      <td>Bisons</td>
      <td>BFP</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BL1</td>
      <td>None</td>
      <td>Baltimore</td>
      <td>Canaries</td>
      <td>BL1</td>
    </tr>
  </tbody>
</table>
</div>




```python
c1 = """
CREATE TABLE IF NOT EXISTS game (
    game_id TEXT PRIMARY KEY,
    date TEXT,
    number_of_game INTEGER,
    park_id TEXT,
    length_outs INTEGER,
    day BOOLEAN,
    completion TEXT,
    forefeit TEXT,
    protest TEXT,
    attendance INTEGER,
    legnth_minutes INTEGER,
    additional_info TEXT,
    acquisition_info TEXT,
    FOREIGN KEY (park_id) REFERENCES park(park_id)
);
"""

c2 = """
INSERT OR IGNORE INTO game
SELECT
    game_id,
    date,
    number_of_game,
    park_id,
    length_outs,
    CASE
        WHEN day_night = "D" THEN 1
        WHEN day_night = "N" THEN 0
        ELSE NULL
        END
        AS day,
    completion,
    forefeit,
    protest,
    attendance,
    length_minutes,
    additional_info,
    acquisition_info
FROM game_log;
"""

q = """
SELECT * FROM game
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>game_id</th>
      <th>date</th>
      <th>number_of_game</th>
      <th>park_id</th>
      <th>length_outs</th>
      <th>day</th>
      <th>completion</th>
      <th>forefeit</th>
      <th>protest</th>
      <th>attendance</th>
      <th>legnth_minutes</th>
      <th>additional_info</th>
      <th>acquisition_info</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FW1187105040</td>
      <td>18710504</td>
      <td>0</td>
      <td>FOR01</td>
      <td>54</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>200</td>
      <td>120</td>
      <td>None</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WS3187105050</td>
      <td>18710505</td>
      <td>0</td>
      <td>WAS01</td>
      <td>54</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>5000</td>
      <td>145</td>
      <td>HTBF</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RC1187105060</td>
      <td>18710506</td>
      <td>0</td>
      <td>RCK01</td>
      <td>54</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1000</td>
      <td>140</td>
      <td>None</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CH1187105080</td>
      <td>18710508</td>
      <td>0</td>
      <td>CHI01</td>
      <td>54</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>5000</td>
      <td>150</td>
      <td>None</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TRO187105090</td>
      <td>18710509</td>
      <td>0</td>
      <td>TRO01</td>
      <td>54</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>3250</td>
      <td>145</td>
      <td>HTBF</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>07 Adding the Team Appearance Table</font>
  -  Create the <font color=red>*team_appearance*</font> table with columns, primary key, and foreign keys as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Insert the data from the <font color=red>*game_log*</font> table, using a <font color=red>*UNION*</font> clause to combine the data from the column sets for the home and away teams.
    -  Write a query to verify that your data was inserted correctly.


```python
c1 = """
CREATE TABLE IF NOT EXISTS team_appearance (
    team_id TEXT,
    game_id TEXT,
    home BOOLEAN,
    league_id TEXT,
    score INTEGER,
    line_score TEXT,
    at_bats INTEGER,
    hits INTEGER,
    doubles INTEGER,
    triples INTEGER,
    homeruns INTEGER,
    rbi INTEGER,
    sacrifice_hits INTEGER,
    sacrifice_flies INTEGER,
    hit_by_pitch INTEGER,
    walks INTEGER,
    intentional_walks INTEGER,
    strikeouts INTEGER,
    stolen_bases INTEGER,
    caught_stealing INTEGER,
    grounded_into_double INTEGER,
    first_catcher_interference INTEGER,
    left_on_base INTEGER,
    pitchers_used INTEGER,
    individual_earned_runs INTEGER,
    team_earned_runs INTEGER,
    wild_pitches INTEGER,
    balks INTEGER,
    putouts INTEGER,
    assists INTEGER,
    errors INTEGER,
    passed_balls INTEGER,
    double_plays INTEGER,
    triple_plays INTEGER,
    PRIMARY KEY (team_id, game_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);
"""

run_command(c1)

c2 = """
INSERT OR IGNORE INTO team_appearance
    SELECT
        h_name,
        game_id,
        1 AS home,
        h_league,
        h_score,
        h_line_score,
        h_at_bats,
        h_hits,
        h_doubles,
        h_triples,
        h_homeruns,
        h_rbi,
        h_sacrifice_hits,
        h_sacrifice_flies,
        h_hit_by_pitch,
        h_walks,
        h_intentional_walks,
        h_strikeouts,
        h_stolen_bases,
        h_caught_stealing,
        h_grounded_into_double,
        h_first_catcher_interference,
        h_left_on_base,
        h_pitchers_used,
        h_individual_earned_runs,
        h_team_earned_runs,
        h_wild_pitches,
        h_balks,
        h_putouts,
        h_assists,
        h_errors,
        h_passed_balls,
        h_double_plays,
        h_triple_plays
    FROM game_log

UNION

    SELECT    
        v_name,
        game_id,
        0 AS home,
        v_league,
        v_score,
        v_line_score,
        v_at_bats,
        v_hits,
        v_doubles,
        v_triples,
        v_homeruns,
        v_rbi,
        v_sacrifice_hits,
        v_sacrifice_flies,
        v_hit_by_pitch,
        v_walks,
        v_intentional_walks,
        v_strikeouts,
        v_stolen_bases,
        v_caught_stealing,
        v_grounded_into_double,
        v_first_catcher_interference,
        v_left_on_base,
        v_pitchers_used,
        v_individual_earned_runs,
        v_team_earned_runs,
        v_wild_pitches,
        v_balks,
        v_putouts,
        v_assists,
        v_errors,
        v_passed_balls,
        v_double_plays,
        v_triple_plays
    from game_log;
"""

run_command(c2)

q = """
SELECT * FROM team_appearance
WHERE game_id = (
                 SELECT MIN(game_id) from game
                )
   OR game_id = (
                 SELECT MAX(game_id) from game
                )
ORDER By game_id, home;
"""

run_query(q)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team_id</th>
      <th>game_id</th>
      <th>home</th>
      <th>league_id</th>
      <th>score</th>
      <th>line_score</th>
      <th>at_bats</th>
      <th>hits</th>
      <th>doubles</th>
      <th>triples</th>
      <th>homeruns</th>
      <th>rbi</th>
      <th>sacrifice_hits</th>
      <th>sacrifice_flies</th>
      <th>hit_by_pitch</th>
      <th>walks</th>
      <th>intentional_walks</th>
      <th>strikeouts</th>
      <th>stolen_bases</th>
      <th>caught_stealing</th>
      <th>grounded_into_double</th>
      <th>first_catcher_interference</th>
      <th>left_on_base</th>
      <th>pitchers_used</th>
      <th>individual_earned_runs</th>
      <th>team_earned_runs</th>
      <th>wild_pitches</th>
      <th>balks</th>
      <th>putouts</th>
      <th>assists</th>
      <th>errors</th>
      <th>passed_balls</th>
      <th>double_plays</th>
      <th>triple_plays</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SLU</td>
      <td>ALT188404300</td>
      <td>0</td>
      <td>UA</td>
      <td>15</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ALT</td>
      <td>ALT188404300</td>
      <td>1</td>
      <td>UA</td>
      <td>2</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BSU</td>
      <td>WSU188409250</td>
      <td>0</td>
      <td>UA</td>
      <td>2</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WSU</td>
      <td>WSU188409250</td>
      <td>1</td>
      <td>UA</td>
      <td>10</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>08 Adding the Person Appearance Table</font>
  -  Create the <font color=red>*person_appearance*</font> table with columns, primary key, and foreign keys as shown in the schema diagram.
    -  Select the appropriate type based on the data.
    -  Insert the data from the <font color=red>*game_log*</font> table, using <font color=red>*UNION*</font> clauses to combine the data from the columns for managers, umpires, pitchers, and awards.
    -  Use a loop with string formatting to insert the data for offensive and defensive positions from the <font color=red>*game_log*</font> table.
    -  Write a query to verify that your data was inserted correctly.


```python
c0 = "DROP TABLE IF EXISTS person_appearance"

run_command(c0)

c1 = """
CREATE TABLE person_appearance (
    appearance_id INTEGER PRIMARY KEY,
    person_id TEXT,
    team_id TEXT,
    game_id TEXT,
    appearance_type_id,
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (appearance_type_id) REFERENCES appearance_type(appearance_type_id)
);
"""

c2 = """
INSERT OR IGNORE INTO person_appearance (
    game_id,
    team_id,
    person_id,
    appearance_type_id
) 
    SELECT
        game_id,
        NULL,
        hp_umpire_id,
        "UHP"
    FROM game_log
    WHERE hp_umpire_id IS NOT NULL    

UNION

    SELECT
        game_id,
        NULL,
        [1b_umpire_id],
        "U1B"
    FROM game_log
    WHERE "1b_umpire_id" IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        [2b_umpire_id],
        "U2B"
    FROM game_log
    WHERE [2b_umpire_id] IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        [3b_umpire_id],
        "U3B"
    FROM game_log
    WHERE [3b_umpire_id] IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        lf_umpire_id,
        "ULF"
    FROM game_log
    WHERE lf_umpire_id IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        rf_umpire_id,
        "URF"
    FROM game_log
    WHERE rf_umpire_id IS NOT NULL

UNION

    SELECT
        game_id,
        v_name,
        v_manager_id,
        "MM"
    FROM game_log
    WHERE v_manager_id IS NOT NULL

UNION

    SELECT
        game_id,
        h_name,
        h_manager_id,
        "MM"
    FROM game_log
    WHERE h_manager_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score > v_score THEN h_name
            ELSE v_name
            END,
        winning_pitcher_id,
        "AWP"
    FROM game_log
    WHERE winning_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score < v_score THEN h_name
            ELSE v_name
            END,
        losing_pitcher_id,
        "ALP"
    FROM game_log
    WHERE losing_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score > v_score THEN h_name
            ELSE v_name
            END,
        saving_pitcher_id,
        "ASP"
    FROM game_log
    WHERE saving_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score > v_score THEN h_name
            ELSE v_name
            END,
        winning_rbi_batter_id,
        "AWB"
    FROM game_log
    WHERE winning_rbi_batter_id IS NOT NULL

UNION

    SELECT
        game_id,
        v_name,
        v_starting_pitcher_id,
        "PSP"
    FROM game_log
    WHERE v_starting_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        h_name,
        h_starting_pitcher_id,
        "PSP"
    FROM game_log
    WHERE h_starting_pitcher_id IS NOT NULL;
"""

template = """
INSERT INTO person_appearance (
    game_id,
    team_id,
    person_id,
    appearance_type_id
) 
    SELECT
        game_id,
        {hv}_name,
        {hv}_player_{num}_id,
        "O{num}"
    FROM game_log
    WHERE {hv}_player_{num}_id IS NOT NULL

UNION

    SELECT
        game_id,
        {hv}_name,
        {hv}_player_{num}_id,
        "D" || CAST({hv}_player_{num}_def_pos AS INT)
    FROM game_log
    WHERE {hv}_player_{num}_id IS NOT NULL;
"""

run_command(c1)
run_command(c2)

for hv in ["h","v"]:
    for num in range(1,10):
        query_vars = {
            "hv": hv,
            "num": num
        }
        run_command(template.format(**query_vars))
```


```python
print(run_query("SELECT COUNT(DISTINCT game_id) games_game FROM game"))
print(run_query("SELECT COUNT(DISTINCT game_id) games_person_appearance FROM person_appearance"))

q = """
SELECT
    pa.*,
    at.name,
    at.category
FROM person_appearance pa
INNER JOIN appearance_type at on at.appearance_type_id = pa.appearance_type_id
WHERE PA.game_id = (
                   SELECT max(game_id)
                    FROM person_appearance
                   )
ORDER BY team_id, appearance_type_id
"""

run_query(q)
```

       games_game
    0      171907
       games_person_appearance
    0                   171907





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>appearance_id</th>
      <th>person_id</th>
      <th>team_id</th>
      <th>game_id</th>
      <th>appearance_type_id</th>
      <th>name</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1646114</td>
      <td>steab101</td>
      <td>None</td>
      <td>WSU188409250</td>
      <td>UHP</td>
      <td>Home Plate</td>
      <td>umpire</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1646116</td>
      <td>murnt101</td>
      <td>BSU</td>
      <td>WSU188409250</td>
      <td>MM</td>
      <td>Manager</td>
      <td>manager</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1646115</td>
      <td>crane101</td>
      <td>BSU</td>
      <td>WSU188409250</td>
      <td>PSP</td>
      <td>Starting Pitcher</td>
      <td>pitcher</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1646118</td>
      <td>scanm801</td>
      <td>WSU</td>
      <td>WSU188409250</td>
      <td>MM</td>
      <td>Manager</td>
      <td>manager</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1646117</td>
      <td>dailh101</td>
      <td>WSU</td>
      <td>WSU188409250</td>
      <td>PSP</td>
      <td>Starting Pitcher</td>
      <td>pitcher</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>09 Removing the Original Tables</font>
  -  Drop the tables we created to hold our unnormalized data:
    -  <font color=red>*game_log*</font>
    -  <font color=red>*park_codes*</font>
    -  <font color=red>*team_codes*</font>
    -  <font color=red>*person_codes*</font>


```python
show_tables()
```




    ['person',
     'park',
     'league',
     'team',
     'game',
     'team_appearance',
     'game_log',
     'park_codes',
     'person_codes',
     'team_codes',
     'appearance_type',
     'person_appearance']




```python
tables = [
    "game_log",
    "park_codes",
    "team_codes",
    "person_codes"
]

for t in tables:
    c = '''
    DROP TABLE {}
    '''.format(t)
    
    run_command(c)

show_tables()
```




    ['person',
     'park',
     'league',
     'team',
     'game',
     'team_appearance',
     'appearance_type',
     'person_appearance']


