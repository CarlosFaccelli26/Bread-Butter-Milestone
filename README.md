# Bread And Butter **Milestone Project**

You can see the live project [Here]()
Bread and Butter is a project which function is to create update delete and read [CRUD]() functionality.
The idea is based on my work, currently I'm working in a Spar more especific in the deli sector, where I prepare sandwiches for costumers among others stuff.

# User Experience
## User Stories
  * **As a User of the website**
    - I want to have an easily navigaton

  * **As a First costumer**
    - I want the ability to register and login easely
    - Be able to see some of the sandwiches on the main page
    - Be able to add, delete or update sandwiches

  * As a Owner
    - Have a eye catching website

# Design
  * **Color Scheme**
    - Main colors used throught the website are white, black, and orange
    - Font used:

# Technologies and Libraries
  - **Technologies Used**
    1. [HTML]()
        - Used to create the content of the website.
    2. [CSS]()
        - Used to give the attractive design of the website.
    3. [JavaScript]()
        - Used to make the website interactive.
    4. [Python]()
       - Used to handle the backend of the webiste
    5. [MongoDb]()
       - Database to store information about users and sandwiches that has been added
  - **Libraries Used**
    1. [Boostrap]()
        - Userd To create a nice layout clear layout
    2. [Font Awesome]()
        - Used to create a more attractive typography
    3. [Flask]()
        - Framework that works with python, all project is based on Flask
    4. [Flask Login]()
        - Dependency of Flask. Used to handle log in functionality
    4. [Heroku]()
        - Platform used to deploy the project
    5. [Git]()
        - Used to version control of the project
    6. [GitHub]()
        - Used to stored the project
    7. [Balsamiq]()
       - Used to create the mockup which will be the base of the live project
    8. [Flask WTF]()
       - Used to create forms on python and rendering on the templates.

# Features
  1. Responsive on all devices
  2. Description Section by Section

# Testing
Project was tested on validators online such as:
  - [HTML Validator]()
    - [View]()
  - [CSS Validator]()
    - [View]()
  - [Javascript Validator]()
    - [View]()

# Testing UX Stories
1. As a First costumer:
   - **I want the ability to register and login easely**
     - The website provides an easy process to log in or register. With just a fews fields to fill the user will be available to login or register.
       Once the user complete the registration form if it is correct will display an alert with the message of "**Registration successfully. You are able to login.**". Same process for the login page, there will be a form which the user has to fill, if all the details are correct the user will have the ability to navigate through the website and add content to the project if he desire.
    - **Be able to see some of the sandwiches on the main page**
      - To navigate through the main page it will not be required to be logged in. The user will see a search form to find any sandwich that the user wants to look for. Scrolling down fill find a carousel displaying three sandwiches the some user has added, and last there will be displayed 8 sandwiches for the user to see. There will be a button that will change depends on the numbers of sandwiches that the website has, if there is 8 or less the button will display "*wanna add a sandwich?*" and if there is more than 8 the button will change the text to "*Wanna See More?*". Each button depends on the number of sandwiches will lead to a new page that will required to be logged in, so users that are not register or not logged in won't be able to see the content.
    - **Be able to add, delete or update sandwiches**
      - Project handle all the [CRUD]() functionality wich are: *Create*, *Read*, *Update*, *Delete*. Users has to be logged in to realize any of these functionalities.
        - **Create**: Create consist in create content to the project. In this case will be add sandiches to the website.
        This will be accomplish throught a form, once again the user has to be logged in to see the content. The form will have many fields to fill, these fields are key information of the sandwich that the users wants to add for example the name of the sandiwich, description, ingredients, image, duration etc... Once all the fields are filled if there is nothig wrong the sandwich will be added to the website and will be visible on the main page if there is no more than 8 sandwiches or in the other case will be located in a new page called All sandwiches.
        - **Read**: Read is the ability to read the content stored on the database and displyed on the website in a nice way.
        On this website all users logged in or not will be available to see sandwiches, in case that the user wants to see all sandwiches added from different users the user has to be logged in.
        Users can see each sandwiches if they want. But only if they are logged in.
        - **Update**: Update will be the ability to change any info about the sandwich that the user created. Users won't be able to change info of a sandwich that they didn't add, the only user capable of change info is the one who created it. Once again will be a form with all the details already displayed on the form so the user doesn't have to fll each of the field again. And from there the user decide wich field wants to change or add more info to the field.
        - **Delete**: Delete like the word says, gives the user the capacity to delete a sandwich. Again only the user who created the sandwich will be able to delete it. 

2. As a Owner
  - **Have a eye catching website**
    - The project has a nice contrast of colors it goes between black orange and white. It gives a good appearance and a nice looking. It has a few animations so it doesn't feel like a static page with no movements.

3. As a User of the website
  - **I want to have an easily navigaton**
    - Website has an easy navigation. Each button will have a descriptive text that will give the user a hint of what the user will be able to do after the user clicks on the button. Website doesn't have any unnecessary complexity to navigate so the user won't be fustrated to looking for something and wasting time.

# Testing Project


# Deployment

# Credits
  1. Flask Login, Flask Wtf, Modal [Corey Schafer]()
  2. Flask Paginate [Darilli Games](https://github.com/DarilliGames/flaskpaginate/blob/master/app.py)
  3. Back to top button [W3S School](https://www.w3schools.com/howto/)
  4. Animations [CSS Tricks](https://www.html-code-generator.com/css/animation-generator)
  4. Thanks to my mentor [Rahul]()
  