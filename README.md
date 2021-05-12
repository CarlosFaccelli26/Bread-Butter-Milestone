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
  - All project has been tested manually for me and friends which I share the link of the website.
1. Main Page:
2. Login Page:
   - ![Login Template](static/images/screenshots/login_template.png)
   ![Login Temaplate 1](static/images/screenshots/login_template1.png)
   As we can see the Login page will consist in a simple form with a backgorund of black and white, playing with the color of text to give a nice contrast.
   ![Valid Login](static/images/screenshots/valid_login.png)
   If user type the correct credentials will be redirect to the main page with a message letting know the user that he was successfully logged in.
   ![Invalid Login](static/images/screenshots/invalid_login.png)
   If user use a credentials that doesn't exist or just an typing error the form won't be submitted and the user will be redirect to the login page with a massage describing that username or password are incorrect and he must try again.
3. Register Page:
   - ![Register Tempalte](static/images/screenshots/register_template.png)
   ![Register Template 1](static/images/screenshots/register_template2.png)
   Register page wil be basicly the same layout than login page, same contrast between black orange and white.
   ![Check Errors](static/images/screenshots/register_check.png)
   If user doesn't accomplish the pattern of the input field, the form when submitted will give an error displaying the error in a message with a red text. Same if the user try to register with a email already in use in the database, it is not possible to register with an email already registered.
   ![Check errors 1](static/images/screenshots/register_check1.png)
   If password doesn't match the form won't be submitted and the user won't be register. Password must match to user be able to register on the webiste.
   ![Register Success](static/images/screenshots/register_success.png)
   Once the user has filled all the inputs and inputs are correct and no errors are showed the user will be successfully registered. User will be redirect to the login page with a message describing that registration was a success.
4. Adding sandwich:
   - ![Add Sandwich Template](static/images/screenshots/add_sandwich_template.png)
   ![Add Sandwich Tempalte 1](static/images/screenshots/add_sandwich_template1.png)
   Add sandwich page will consist in a form with pretty much the same layout than register and login page. The only different will be that the form will have more fields to fill up.
   ![Check Errors](static/images/screenshots/add_sandwich_check.png)
   ![Check Errors1](static/images/screenshots/add_sandwich_check1.png)
   ![Check Errors2](static/images/screenshots/add_sandwich_check2.png)
   ![Check Errors3](static/images/screenshots/add_sandwich_check3.png)
   ![Check Errors4](static/images/screenshots/add_sandwich_check4.png)
   ![Check Errors5](static/images/screenshots/add_sandwich_check5.png)
   ![Check Error6](static/images/screenshots/edd_sandwich_check6.png)
   All these images test how each input will behave if the input has not been filled. All field must be filled to submit the form and the sandwich will be added.
   ![Sandwich Added](static/images/screenshots/sandwich_added.png)
   If all the fields are filled and show no errors the form will redirect the user to the main page and show a message wich contain the text describing that the sandwich has been added.
5. Edit Sandwich:
   - ![Edit Sandwich Template](static/images/screenshots/edit_sandwich_template.png)
   ![Edit Sandwich Template1](static/images/screenshots/edit_sandwich_form.png)
   Edit sandwich template will have a form same layout of add sandwich template. With the diffrerence of all the fills will be populated with the data that was used to add the sandwich, so the user won't waste time filling up all the fields again and then submit the form.
   ![Edit Sandwich Success](static/images/screenshots/sandwich_updated_message.png)
   Once the user has updated the sandwich the form will redirect the user to the sandwich tempalte with a message with a text describing the action that the user has realized.
6. Individual Sandwich:
   - ![Sandwich Template](static/images/screenshots/individual_sandwich.png)
   Sandwich template will display a single sandwich with all the details of the sandwich. In these case the sandwich was created by the same user. This is because there is two buttons which give two different actions. One is to update the sandwich the other to delete it. Only to the user that has created the sandwich will appear the two buttons.
   ![Sandwich Template1](static/images/screenshots/individual_sandwich1.png)
   As we can see in the page the two buttons doesn't appear, that is because the user didn't create the sandwich, for these reason user can't edit or delete the sandwich. If user type the route to edit or delete the sandwich the page will show an error [403](https://en.wikipedia.org/wiki/HTTP_403) customize. Next will be attached the screenshot will describe these error.
   ![Error Handler](static/images/screenshots/error_handler.png)
   As we can see if the user try to delete or update a sandwich that the user hasn't created the page will show the error with a link to go back to the main page.
7. Search From:
   - ![Check Search Form](static/images/screenshots/check_search_input.png)
   Search form is located on the main page at the bottom of the page, below the navbar. If user doesn't fill the input the form won't be submitted.
   ![Fail Results](static/images/screenshots/search_result_fail.png)
   If user filled the form and submit it but the webiste doent't find the sandwich that the user is looking for the page will show a massage describing the there is no results for that search.
   ![Show Results](static/images/screenshots/show_search_results.png)
   If user fill the input and the website has the sandwich that the user is looking for the website will display the sandwich bellow the carousel on the main page.
8. Delete Sandwich:
   - ![Modal](static/images/screenshots/modal_popup.png)
   If user wants to delete the sandwich, if the user was the creator of the sandwich will be able to see two buttons, one for update and the other to delete. If user clicks on delete button a modal will popup with two buttons and a text asking the user if the user is sure about deleting the sandwich. The buttons will have the actions of delete the sandwich or close the modal.
   ![Delete Success](static/images/screenshots/sandwich_deleted.png)
   If the user deletes the sandwich user will be redirect to the main page with a flash message describing the action the the user has just make.
9. Limiting Acces:
   - ![Info Message](static/images/screenshots/login_message_info.png)
   If user is not currently logged in and try to access any page or functionality that require to be logged in, the user will be redirect to the login page with a message asking the user to login to gain access to the page.

# Deployment
Project was stored on [GitHub]() and deploy on [Heroku](). This change due the previous milestone project is due [GitHub]() does not support backend code however [Heroku]() it allows to deploy code base on backend.
First of all I created a repo on [GitHbu]() as i show in the next picture.
![New Github Repo]()
Once the repo is created we create a new app on [Heroku]():
![Creating New App](static/images/screenshots/creating_new_app.png)
After we created the app, we must choose the region that we are currently living in and the name of the app:
![Region and Name](static/images/screenshots/app_and_region.png)
After we create the app give a name and provide the region that we are currently in we'll find a dashboard in which the first step is to connect the app with the repo on [GitHub]():
![GitHub Connect](static/images/screenshots/connect_github_repo.png)
We must be sure that the name that we include to connect the github repo match with name of the repo on github otherwise it won't find any repo with the name provided:
![Github Connect 1](static/images/screenshots/connect_github_repo1.png)
Once we connect the github repo with heroku we can click on settings.
![Settings](static/images/screenshots/settings.png)
After clicking on settings we scroll down until we find a button, if we click on that button it will reveal some variables that we need to fill up with the variables that we provide in the code of the project for example: Secret Key for flask, name of the database, the URI etc....
![Configuration Variables](static/images/screenshots/configuration_of_variables.png)

# Credits
  1. Flask Login, Flask Wtf, Modal [Corey Schafer]()
  2. Flask Paginate [Darilli Games](https://github.com/DarilliGames/flaskpaginate/blob/master/app.py)
  3. Back to top button [W3S School](https://www.w3schools.com/howto/)
  4. Animations [CSS Tricks](https://www.html-code-generator.com/css/animation-generator)
  4. Thanks to my mentor [Rahul]()
  