# url_shortener
## By Kelvin, Menelaos
The Awesome URL shortener website for shortening your long urls! They are stored in the database so when you next visit this site you can get redirected to the link by typing the short url in the address bar of the home page.
## Installation and Usage

### Installation
- Clone or download the repo
- `cd` into it
- Run `pipenv shell` to create a shell
- `pipenv install` to install all the dependencies
- `pipenv run dev` to run in developer mode

### Usage
- Navigate to `localhost:5000`
- Enter the url you want shortened and click submit
- Your url should appear below the form. put that url in your navigation bar and you are ready to go!
- Note: when restarting the server the database table gets dropped. Use the routes /all to view all saved urls currently in the database.
