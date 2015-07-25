# lulzbot Telegram Bot - <a href="https://telegram.me/lulzbot">@lulzbot</a>

> This bot is using Telegram bot API. It has lot of features. The concept is driven from IRC bot. Custom keyboard is only used for games like "HotOrNot". Rest of the stuff is purely command based.

Version: 0.0.1


##Features
----------


| Commands argument  	    | *Function*								   | **Example**     			|
| --------------------------| ---------------------------------------------| ---------------------------|
| /help			  		    | Displays list of Commands                    | /help	      				|
| /google keyword           | Google search by keyword					   | /google terminator			|
| /wiki keyword		  	    | Lookup for wikipedia article 				   | /wiki Anaconda				|
| /github username	  	    | Get recent activity of user 				   | /github Bhavyanshu 		|
| /translate from to "strng"| Microsoft translate						   | /translate en hi "I'm good"|
| /insta username           | Get posts of instagram user 				   | /insta magnumphotos		|
| /hon			  		    | Get random Instagram post and start HotOrNot | /hon or /hotornot 			|
| /tw username              | Get tweets of twitter user 				   | /tw nasa					|
| /yt keyword string	    | Search youtube for video 					   | /yt Iron Maiden			|
| /cats			  		    | Get a random cat pic 						   | /cats						|
| /weather city,state       | Get weather update for city 				   | /weather paris				|
| /giphy keyword            | Get gif from giphy 						   | /gif awesome				|
| /calc expression          | Calculate math expressions 				   | /calc 2+2 					|


> Note that some features of the actual bot @lulzbot registered on telegram will be missing from here. Like bot administration commands and commands meant for my own personal use. However, they do not break this code nor do they in any way affect the working on this code. They are completely unrelated modules. On request, I can explain how you can write bot administration commands for Telegram bot API.

##How to use
------------
1. First open data/config.ini file and add all the required API keys from various social media sites. For telegram token, contact @BotFather on telegram and create a new bot there. @BotFather will reply provide you the token once the bot is created.
2. Then you need to make sure you have all the required dependencies. **Python 2.7 is required**.

        $ pip install -r requirements.txt

3. For debugging, run using `python bot.py`. If there is a crash, it won't restart.
4. For production mode, run `./botmon.sh` which will restart bot if it crashes. 

##LICENSE
---------

> Copyright (C) 2015  Bhavyanshu Parasher

> This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

> This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

> You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

##Contribute
------------

> Create an issue if you find any bug. If you want to improve something, send a pull request.
