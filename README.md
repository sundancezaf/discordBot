# discordBot

This Discord Bot was made to get Covid-19 statistics.

Invite bot here: [invite](https://discord.com/api/oauth2/authorize?client_id=731054408091041793&permissions=0&scope=bot).

All commands need to have "." as the prefix for them to work. Ex: for the command "stateTotal", the full 
command is: `.stateTotal [state]`. You replace `[state]` with the name of the state. \
If the state is two words you will need to place it in quotation marks. Ex: `.stateTotal "North Carolina"`




| Commands |  Actions |
|----------|----------
| commandList | sends user a DM with the list of commands |
| firsEvent [state]  | give the date of the first case |
| stateTotal [state] | gives total number of cases for that state. |
| pastCases [state] [number]| gives number of cases for the past number of days specified |
| stateDeaths [state] | gives total number of deaths for that state |
| totalCases | gives total number of cases for the US |
| totalDeaths | gives total number of deaths for the US |

** This project is a continuation of the Covid-Statistics project. Data used comes from [the NYTimes](https://github.com/nytimes/covid-19-data).

**This project's data is updated daily in the actual code
