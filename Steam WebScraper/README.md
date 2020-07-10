# Steam_WebScraper
<p align="center">
    <a href="https://github.com/SVijayB/Steam_WebScraper"><img src="assets/images/Logo.PNG" alt="Logo" border="0"></a>
    <br>A simple App to monitor prices on the Steam market
</p>

<br>

---

## Motivation

This application was built to monitor Steam market value changes of all `CSGO` Items. It was an attempt at learning the basics of `Web Scraping`

It helps in obtaining an item at a lower price than normal. i.e., It notifies the user when the product value decreases below the desired price. Hence saving money and time that goes wasted on waiting for the prices to fall.

## Usage

<p align="center">
    <img src="assets/images/Main SS.PNG" alt="SS" border="0">
</p>

Run `Update.py` file present in the `src` folder.<br>
This is to update your local data (Item skin names). 

Once the update is completed, run the `Steam_WebScraper.py` file present in the `src` folder.

Now, just follow the instructions provided by the application.

**NOTE** : Update your local data using the `Update.py` file after every new CSGO case releases in order to view all the latest skins.

### Gmail Notification 
In case you want to be notified via mail when price falls down, follow the below steps : 
- Create a Gmail Account, if you don't have one already.
- Sign into your Google account.
- Next, go to your Google account <a href="https://myaccount.google.com/security">Security Settings</a>.
- Click on the <a href="https://myaccount.google.com/u/3/lesssecureapps">Less secure app access</a> setting.
- Set Allow less secure apps to **ON**
- Next, Open your [Gmail](https://www.gmail.com/) account.
- Click on Gmail Settings.
- Now, click on the Forwarding and POP/IMAP tab.
- Under POP download section, Click on Enable POP for all mail.
- Under IMAP access section, Click on Enable IMAP.