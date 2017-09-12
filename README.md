Ethereum Bot
===================
**Ethereum Bot** is a simple bot of Telegram that will allow us to consult at all times our mine statistics of our Pool.


Pool available
--------------

We can use this bot to consult the mining statistics of:

 - [Ethermine](https://ethermine.org/)
 - [Ethpool](http://ethpool.org/)


Features
-------------
With the following bot we will be able to visualize:

 - Hashrates
 - Active Workers
 - Unpaid
 - Money generated ($,€)
 - Current Ethereum price


Getting Started
-------------
### Installation
For installation, the first thing we will do is to install the **pyTelegramBotAPI** library.

    $ sudo pip install pyTelegramBotAPI

The following will be cloned our Github repository:

    $ git clone https://github.com/RafaMunoz/Ethereum_Bot.git
    $ cd Ethereum_Bot

We will edit the Settings section with our data.

    $ sudo nano ethbot.py


 For example:

    # -------------------- SETTINGS --------------------
    # Your Ethereum wallet.
    wallet = "0x947edcaa3c9b63e3ccf2d5e148bf62674f519f34"
    
    # Telegram bot Token.
    token = "378572660:AAHaLn4NylzJuv4kl4XusEtG3LeDqafjA75"
    
    # List with the telegram id of the allowed users.
    id_admins = [15288736, 16278436]
    
    # Your Pool. 0 = Ethermine | 1 = Ethpool
    pool = 0
    # --------------------------------------------------


Finally we execute the script and we can go to our bot of Telegram and consult our statistics:

    $ sudo python ethbot.py