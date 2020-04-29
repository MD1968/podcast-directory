# [Data-Centric Development Podcast Collection Application](https://podcast-directory.herokuapp.com/)

I have created this podcast collection using the Python framework Flask and MongoDB for the Data-Centric Development module of the Code Institute Full Stack Web Development diploma. This application allows users to add, edit or delete podcasts. Users can browse the podcasts on the homepage.

## UX

Having completed the third section of the course we received a suggestion was made to create a favourite podcast site. However, as I do not cook, I wanted to find an alternative. Having recently got into the joy of listening to podcasts I decided to create a site to contain a list of some good examples.

From looking at other sites for Podcast collections I knew I wanted to display the podcast information on a 'card' so that its information looks as clean as possible. 

I took inspiration for the colour scheme from [Color-Hex](https://www.color-hex.com/color-palette/827)

## User Stories

- A user wants to view a podcast: They can view the podcasts on the Homepage. The user can click on a card and see the podcasts description, photo, and a link to the podcaster provider website.

- A user would like to add a podcast: 
   
  - They should choose to login from the CTA buttons in the navbar (or side menu if viewing on mobile)
  - They are redirected to a manage podcast screen, they can choose the 'Add Podcast' option under the navbar
  - The user is navigated to a form in which they can fill in the necessary information about their podcast
  - The form has validation, so all fields must be filled in before the 'Add' button will work
  - Once they have completed all fields and clicked on Add the data will be posted to the database and they will redirected back to manage podcast page, where their podcast will be displayed in the lister view

- A user wants to edit a podcast:
  - They should choose to login from the CTA buttons in the navbar (or side menu if viewing on mobile)
  - They are redirected to a manage podcast screen, they can choose the 'Edit Podcast' option under the selected podcast
  - The user is navigated to a form in which they can fill in the necessary information about their podcast
  - The form has validation, so all fields must be filled in before the 'Add' button will work.
  - Once they have completed all fields and clicked on Add the data will be updated on the database and they will redirected back to manage podcast page, where their podcast will be displayed in the lister view.

- A user wants to delete a podcast:
  - They should choose to login from the CTA buttons in the navbar (or side menu if viewing on mobile)
  - They are redirected to a manage podcast screen, they can choose the 'DEL' option under the selected podcast
  - If the user clicks the DEL button located below the podcast of their choice. The podcast data will be deleted and the user will be returned to the manage podcast screen. The podcast will be removed from the list.   

- A user wants to view a podcast:
  - On the homepage, the user can click on a podcast card to view the name, description link and image.
  
- Contact:
  - The users should choose to Contact from the CTA buttons in the navbar (or side menu if viewing on mobile)
  - They are taken toma form in where they can fill in the necessary information for their message
  - Once the forms data has been validated the user can click on the Send button to send the message
  - The user will then be redirected to a message sent confirmation


## Wireframes have been created using Balsamiq

They can be located in the wireframes folder.

## Features (CRUD)

- Create, Add podcast

- Read, Podcast data displayed on the Homepage and within the cards.

- Update, Edit existing podcast data

- Delete, Delete existing podcast data

- Contact website author
 
### Existing Features

### Features Left to Implement

## Technologies Used

- [Flask](http://flask.pocoo.org/)
    - The project uses **Flask** , a Python micro framework to provide a functional and lightweight core for the application

- [Jinja2](http://jinja.pocoo.org/docs/2.10/)
    - This app uses the **Jinja2** for the front-end templating of the routes outlined in the app.py file. 
    - Modelled on Django's templating style, **Jinja2** is scalable and modular to allow for reusable components

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - HTML used for the **structure** of the page templates

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - The language used to apply styles to each page for styling of the components (e.g. colour schemes, fonts, images)
    
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - I have used Javascript in the add/edit podcast forms to power the logic behind the 'Add Ingredient' and 'Remove Ingredient' buttons. I have also used this to create a validation error for the Materialize select component as there is a known issue with this component showing error messages.
    - JS has also been used to power the sliding side menu action on smaller screen sizes
    
- [Materialize](https://materializecss.com/)
    - I have used Materialize throughout the project to create navbars, side menus, input types in forms and icons
   
- [MongoDB](https://mlab.com/welcome/)
    - I have used MLab to implement a **database** in this project. This is where all of the user, podcast and category data is stored.

### TESTING:

I have tested this project on the most common browsers: Chrome, Edge, Firefox. Testing was completed using a locally hosted webserver to confirm all links and formatting were working correctly. Also, I have tested the content using a Google Pixel 4x, Nokia, Apple iPhone and IPad, and the developer kit built into Chrome.

During my testing, I have manually checked all the links and buttons for functionality.

I have used the inspect option with income to check the layout for all of the screen size options.

Also, on my Pixel 4xl and Galaxy S10 and Samsung Galaxy tablets. 

I have also used the kind help of my family and friends to test the application.

They have checked for content, spelling and grammar issues and links and button functionality. Their comments and feedback are very appreciated.

I have also used Microsoft word to double-check the spelling and grammar used within the project.

The excellent application Grammarly has also been used throughout this project.

I have used <a href="https://validator.w3.org/">HTML Validator</a> to validate the HTML code and corrected all the major error or warning messages.

I have also uploaded the CSS file to <a href="https://jigsaw.w3.org/css-validator/">CSS <a>

I have also used my family and friends to test the site on as many different devices as possible.

## Deployment

This application is hosted on Heroku at:  https://podcast-directory.herokuapp.com/ In order to deploy this app to heroku, I added a [Procfile](https://github.com/MD1968/podcast-directory/blob/master/Procfile) which tells heroku the language of the app and the name of the file that needs to be run - in this case this was [app.py](https://github.com/MD1968/podcast-directory/blob/master/app.py)
I then set up a [requirements.txt](https://github.com/MD1968/podcast-directory/blob/master/requirements.txt) file which holds the dependencies that this app requires in order to run. Both the Procfile an requirements.txt file are committed to the repository and pushed to Heroku.

I had to set up some environment variables inside Heroku in order for the app to appear on the live URL. The following are configured under Settings -> Reveal Config Vars
  - IP: 0.0.0.0
  - PORT: 5000
  - MONGO_URI: This is set in the env.py file for use locally, but needs to be set in the config vars in heroku. It takes the format of mongodb://<db_user>:<db_password>@mongodb0.example.com:<port>/<db_name>

#### Run app locally
  - Clone this repository using ``` $ git clone <https://github.com/charlotteskinner90/dcd-milestone-project-podcast-hub.git> ```
  - Install dependencies required for the app to run from the requirements.txt file by running the following command in the terminal ```pip install -r requirements.txt```
  - Set your environment variables i.e. IP: 127.0.0.1 and PORT: 5000 to view the site in the browser.
  - Set debug to True at the very bottom of app.py when running locally, set to False when deployed to production.
  - Run the code in an IDE of your choice ```python app.py```
  - Follow the database instructions below to set up a database to use with this app.

#### Database setup
  - Create a MongoDB database in MLab named 'podcasts'
   - Set the MONGO_URI as an app.config in the env.py file.

#### Deploying to Heroku
  - If you would like to deploy your own version to Heroku, first make sure that you have a Heroku account.
  - Log in to your Heroku account on the CLI ``` $ heroku login ```
  - Clone the repository ``` $ heroku git:clone -a podcast-collection ``` then ``` $ cd podcast-collection ```
  - Make your changes
  - Set the aforementioned environment variables in the Config Vars section of Heroku (under Settings) before deployment
  - Deploy to Heroku using git:
    - ``` $ git add . ```
    - ``` $ git commit -m "commit message" ```
    - ``` $ git push heroku master ```

### INFLUENCES:
I have also used various projects from the Code Institute Submissions GitHub repository for inspiration.
 <a href="https://github.com/Code-Institute-Submissions" > Code Institute Submissions</a>


### Acknowledgements:
Thank you to everyone who has helped me with this project.

Including:
* My dear friends and family for their help with the testing of the project.
* My girlfriend for her patience shown whilst I was working to the project completed.
* My course mentor for his excellent guidance and feedback.
