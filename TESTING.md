# Testing

Back to [README.md](README.md)<br>

## Table of contents
* [User Story and Feature Testing](#user-story-and-feature-testing)
* [Browser Testing](#browser-testing)
* [Code Validation](#code-validation)
* [Bugs](#bugs)


## User Story and Feature Testing
### EPIC | User Navigation
#### Content Navigation
 _As a Site User I can navigate easily around site contents so that I know if it meets my neeeds._

- Navigation bar is visible on every page of the website and fully responsive on different screen sizes.

![Navigation Bar](documentation/readme_images/navigation-bar.png)<br>
- Arrow at the end of each page help users to navigate easily to the top especially in the home page.

![Arrow](documentation/readme_images/arrow-top.png)<br><br>


#### Site Pagenation
* _As a Site User I can view paginated list of reciepes so that easily select one to view._

- On clicking on any recipe category will display a list of recipes. Each page has 6 recipe and the other recipes displayed on the next page that can be displayed on clicking on the next button. 

![Navigation Bar](documentation/readme_images/next-btn.png)<br><br>

### EPIC | User Profile
#### Account Registration
 _As a Site User I can register an account so that I can comment and like._

- Navigation bar is visible on every page of the website and fully responsive on different screen sizes.

![Navigation Bar](documentation/readme_images/navigation-bar.png)<br>
- Arrow at the end of each page help users to navigate easily to the top especially in the home page.

![Arrow](documentation/readme_images/arrow-top.png)<br><br>

#### Account Registration
 _As a Site User I can register an account so that I can comment and like._

* Users can see _Register_ link in the navbr, when clicked user will be navigate to sign-up page to fill the required information.

#### Log in / out
 _As a Site User I can log in/ out so that I keep my account secure._

* After the user register an account, _log-in_ and _log-out_ links can be accessed.

#### Log in Status
 _As a Site user I can see my status if I logged in or out so that I can interact with contents by leaving comments , like and bookmark recipes._

* Once the user logged in, the user name will be diplayed in the home page, my bookmarke and my recipes pages. 

![Username](documentation/readme_images/user-name.png)<br>

* Also the user will see Add recipe and profile dropdown links after logged-in.
* The user can see comment form, so can leave a comment.
* The user can like/dislike and bookmarke recipes.
* If the user click on like or bookmarke buttons without logging-in, the user will be rdeirect to log-in page to log-in.



#### View Bookmarked recipes
 _As a Logged-in User I can view my bookmarked recipes in my profile so that I can find them easily each time I need them._

* Logged-in users can access profile dropdown menu. So the user can open bookmark page and view all bookmarked recipes.

#### View My Published Recipes
 _As a Site User I can view my published recipes so that I can manage all my added recipes from my profile._

 * Logged-in can access my recipes page and view all his own published recipes.


### EPIC | Recipe Mangagement
#### Mange User Recipe
 _As a Site User I can add my own recipe so that I can share it with other users._

* Logged-in users can add their own recipes and have access to them by editing or deleting.
* The user will get confirmation message to notified that the recipe has been created,updated or deleted successfully. 

![My-Recipes Page](documentation/readme_images/my-recipes.png)<br>

####  Admin Managment.
 _As a Site Admin I can create, read, update and delete recipes so that I can manage my site content and share recipes with other users._

* Site admin has the access all CRUD features from the backend.

### EPIC | Recipe Interaction
#### View Recipeslist
 _As a Site User I can view a list of recipes so that I can select one to read._

* All users can view recipes lists for any category on any time.

#### View Recipe
 _As a Site User I can click on a recipe post so that I can read full recipe details._

* All users can show all the detailes of any recipe separately.

#### View Comments
 _As a Site User/Admin I can view comments on an individual recipe so that I can read the conversation._

* All users can read the comment on each recipe. So, csn get an impression of the recipe before applying it.

#### Comment on a recipe
 _As a Site User I can leave comments on a recipe so that I can be involved in the conversation._

* Looged in users can leave a comment on a specific recipe, so he can write his review or experience for this recipe.

#### View Likes
 _As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular._

* All users can see the how many likes on each recipe. Therfore, he can easily find out the most delicious recipe and try it.

#### Like / Unlike Recipe
 _As a Site User I can like or unlike recipe so that I can interact with the content._

* Logged in users can like/dislike a specific recipe.

#### Add bookmark
 _As a Site User I can bookmark recipe so that I can save it in my profile._

* Logged in users can save any recipe they liked inthe bookmark page so can return to in needed.

### EPIC | Site Management
#### Approve Comments
 _As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments._

* All the published comment were approved only by the site admin.

## Browser Testing
The website was tested on different browsers for assuring the features work accordingly.
* Chrome
* Edge
* Firefox
* Opera

* On Firefox when hovering on the recipe name, name should be underline but on firefox the name display with double underlines.

## Code Validation
### HTML
The html code of the website was validated using [W3 Markup Validator](https://validator.w3.org/).<br>
The validation have the following outcome:<br><br>

![html-validate](documentation/readme_images/html-validate.png)<br><br>


The pages that have been tested:
* Base
* Home
* Dinner
* Sweets
* Coctailes
* Add Recipe
* My Bookmarkes
* My Recipes
* Login/Log out/Register
* Recipe Detail
* Delete Recipe
* Edit Recipe
* Delete Comment

### CSS
The CSS code was validated using [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/) with no errors.<br>

![CSS-validate](documentation/readme_images/css-validator.png)<br><br>

### Javascript
The Javascript code was validated using using [JsHint](https://jshint.com/)<br>
I have validate two functions as the following:

![Javascript-validate](documentation/readme_images/js-validator.png)<br><br>

In the begening I get these warning the following warnings, and fixed using change datatype from let to var to be available througt the function.
![Javascrit-validate](documentation/readme_images/js-error.png)<br><br>

### Python
The [PEP8](http://pep8online.com/) Validator Service was used to validate the following Python files in the project to ensure there is no syntax errors in the project.

![python-validate](documentation/readme_images/python-validator.png)<br><br>

## Device Testing
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone SE, iPhoneXR, iPhone 12 Pro iPad, and iPad Air to ensure responsiveness on different screen sizes.

## Manual Testing

### Site Navigation
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Name (logo area) | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Browse Recipes Link   | Click      | Open Browse Recipes Page                                           | Pass      |
| Add Recipe Link       | Click      | Open Add Recipe Form                                               | Pass      |
| Add Recipe Link       | Display    | Only visible if user in session                                    | Pass      |
| My Meal Plan Link     | Click      | Open My Meal Plan page                                             | Pass      |
| My Meal Plan Link     | Display    | Only visible if user in session                                    | Pass      |
| My Account Dropdown   | Click      | Open My Account dropdown                                           | Pass      |
| My Account Dropdown   | Display    | Text changes to username with profile icon when user is in session | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| My Recipes Link       | Click      | Open My Recipes page                                               | Pass      |
| My Recipes Link       | Display    | Only visible if user in session                                    | Pass      |
| My Bookmarks Link     | Click      | Open My Bookmarks page                                             | Pass      |
| My Bookmarks Link     | Display    | Only visible if user in session                                    | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user in session                                    | Pass      |
| All Nav Links         | Hover      | lighten text                                                        | Pass      
|                       |            |                                                                    |           |
| Mobile View           |            |                                                                    |           |
| Hamburger Menu        | Responsive | Display when screen size reduces to medium size                       | Pass      |
| My Account Dropdown   | Responsive | Contents move into hamburger menu when screen size reduces to medium           | Pass      |
| Site Name (logo area) | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Browse Recipes Link   | Click      | Open Browse Recipes Page                                           | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| Add Recipe Link       | Click      | Open Add Recipe Form                                               | Pass      |
| Add Recipe Link       | Display    | Only visible if user in session                                    | Pass      |
| My Meal Plan Link     | Click      | Open My Meal Plan page                                             | Pass      |
| My Recipes Link       | Click      | Open My Recipes page                                               | Pass      |
| My Recipes Link       | Display    | Only visible if user in session                                    | Pass      |
| My Bookmarks Link     | Click      | Open My Bookmarks page                                             | Pass      |
| My Bookmarks Link     | Display    | Only visible if user in session                                    | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user in session                                    | Pass      |
|                       |            |                                                                    |           |
| Footer                |            |                                                                    |           |
| All links             | Click      | Open in new tab and to correct location                            | Pass      |

### Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Hero 'Sign Up' Button | Click   | Open Sign up page               | Pass      |
| Hero 'Sign Up' Button | Display | Not visible if user in session  | Pass      |
| Hero 'Create" Button  | Click   | Open Add Recipe page            | Pass      |
| Hero 'Create" Button  | Display | Only visible if user in session | Pass      |

### Browse Recipes Page
| Element     | Action                  | Expected Result                                                                         | Pass/Fail |
|-------------|-------------------------|-----------------------------------------------------------------------------------------|-----------|
| Recipe Card | Display correct content | Display correct image, recipe title and cooktime                                        | Pass      |
| Recipe Card | Click                   | Clicking anywhere inside the recipe card takes you to the correct recipe's detail page. | Pass      |
| Recipe Card | Pagination              | Site will paginate 8 recipe cards to a page                                             | Pass      |
| Recipe Card | Order                   | Recipes are sorted by newest to oldest                                                  | Pass      |
| Recipe Card | Hover                   | Add gold border                                                                         | Pass      |
### Recipe Detail Page

| Element                        | Action              | Expected Result                                                                                                         | Pass/Fail |
|--------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Recipe Content                 | Display             | Display correct recipe image, title, author, prep time, cook time, description, ingredients and method                  | Pass      |
| Add to Meal Plan button        | Click               | Meal Plan modal pops up                                                                                                 | Pass      |
| Add to Meal Plan button        | Display             | Button only visible if user in session                                                                                  | Pass      |
| Bookmark button (Outline)      | Click               | Clicking the outlined bookmark changes it to a solid bookmark                                                           | Pass      |
| Bookmark button (Outline)      | Click               | Recipe is added to the user's bookmarks page                                                                            | Pass      |
| Bookmark button (Outline)      | Click               | Success message appears informing the user that the recipe has been added to their bookmarks                            | Pass      |
| Bookmark button (Outline)      | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Bookmark button (Solid)        | Click               | Clicking the solid bookmark changes it back to an outlined bookmark                                                     | Pass      |
| Bookmark button (Solid)        | Click               | Recipe is removed from the user's bookmarks page                                                                        | Pass      |
| Bookmark button (Solid)        | Click               | Success message appears informing the user that the recipe has been removed from bookmarks                              | Pass      |
| Bookmark button (Solid)        | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Bookmark button                | Display             | Button only visible if user in session                                                                                  | Pass      |
| Update recipe button           | Click               | Opens Update Recipe Form                                                                                                | Pass      |
| Update recipe button           | Display             | Button only visible if user is the author                                                                               | Pass      |
| Delete recipe button           | Click               | Opens Delete Recipe confirmation page                                                                                   | Pass      |
| Delete recipe button           | Display             | Button only visible if user is the author                                                                               | Pass      |
| User Comments                  | Display             | Displays correct name date time and comment body                                                                        | Pass      |
| User Comments                  | Display             | Comments are ordered oldest to newest                                                                                   | Pass      |
| Update comment button          | Display             | Button only visible if user is the comment author                                                                       | Pass      |
| Update comment button          | Click               | Opens Update Comment Form                                                                                               | Pass      |
| Update comment form            | Leave empty         | On submit: form won't submit                                                                                            | Pass      |
| Update comment form            | Leave empty         | Error message displays                                                                                                  | Pass      |
| Update comment submit button   | Click               | Form submit - page updates and comment displays in comments section with correct content                                | Pass      |
| Update comment submit button   | Click               | Success message appears informing the user that the comment has been updated                                            | Pass      |
| Update comment submit button   | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Update comment form            | Access              | If a user tries to edit another user's comment (by changing the url) they receive a 403 error.                          | Pass      |
| Update comment form            | Access              | If a user tries to edit a comment (by changing the url) without being signed in they are redirected to the login page   | Pass      |
| Delete comment button          | Display             | Button only visible if user is the comment author                                                                       | Pass      |
| Delete comment button          | Click               | Opens delete comment confirmation page                                                                                  | Pass      |
| Confirm delete button          | Click               | Comment is removed from comment section                                                                                 | Pass      |
| Confirm delete button          | Click               | Success message appears informing the user that the comment has been deleted                                            | Pass      |
| Confirm delete button          | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Confirm delete button          | Click               | Redirect user back to recipe page                                                                                       | Pass      |
| Cancel delete button           | Click               | Redirect user back to recipe page                                                                                       | Pass      |
| Delete comment                 | Access              | If a user tries to delete another user's comment (by changing the url) they receive a custom 403 error.                 | Pass      |
| Delete comment                 | Access              | If a user tries to delete a comment (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Add comment Form               | Display             | Form only visible if user in session                                                                                    | Pass      |
| Add comment Form submit button | Leave empty               | On submit: form won't submit                                                                                            | Pass      |
| Add comment Form submit button | Leave empty               | Error message displays                                                                                                  | Pass      |
| Add comment Form submit button | Filled in               | Form submit - page updates and comment displays in comments section with correct content                                | Pass      |
| Add comment Form submit button | Click               | Success message appears informing the user that the comment has been added                                              | Pass      |
| Add comment Form submit button | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
|                                |                     |                                                                                                                         |           |
| Meal plan model                |                     |                                                                                                                         |           |
| Modal cancel button            | Click               | Close modal                                                                                                             | Pass      |
| Days drop down menu            | Click               | Display list of the days of the week                                                                                    | Pass      |
| Days drop down menu            | Click               | Default day is Monday                                                                                                   | Pass      |
| Add to Meal Plan submit button | Click               | Form Submit                                                                                                             | Pass      |
| Add to Meal Plan submit button | Click               | Correct recipe is added to the user's Meal Plan page for the correct day                                                | Pass      |
| Add to Meal Plan submit button | Click               | Success message appears telling the user that the recipe has been added to their meal plan                              | Pass      |
| Add to Meal Plan submit button | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Add to Meal Plan submit button | Click               | If meal plan item already exists for that day, the success message tells the user that meal plan has been updated       | Pass      |
| Add to Meal Plan submit button | Click               | Modal closes                                                                                                            | Pass      |
| Meal Plan modal                | Click outside modal | Close modal                                                                                                             | Pass      |
### Add Recipe Page
| Element                       | Action                | Expected Result                                                                                                     | Pass/Fail |
|-------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------|-----------|
| Add Recipe                    | Access                | If a user tries to add a recipe (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Form Text Input (if required) | Leave blank           | On Submit: Warning appears, form won't submit                                                                       | Pass      |
| Form Text Input (if required) | Just input whitespace | On Submit: Form won't submit                                                                                        | Pass      |
| Recipe Title                  | Duplicate Entry       | On Submit: Warning appears, form won't submit                                                                       | Pass      |
| Form image select button      | Click                 | Open device storage                                                                                                 | Pass      |
| Form image select button      | Display               | Chosen image name displayed once selected                                                                           | Pass      |
| Form image select button      | Display               | Default image is used if no image is selected                                                                       | Pass      |
| Cancel button                 | Click                 | Redirect to Browse Recipes page                                                                                     | Pass      |
| Add Recipe button(form valid) | Click                 | Form submit                                                                                                         | Pass      |
| Add Recipe button(form valid) | Click                 | Redirect to Recipe detail page for new recipe with all information displaying correctly                             | Pass      |
| Add Recipe button(form valid) | Click                 | Success message appears informing the user that the recipe has been created                                         | Pass      |
| Add Recipe button(form valid) | Click                 | Success message fades after 3 seconds                                                                               | Pass      |
### Update Recipe Page
| Element            | Action  | Expected Result                                                                                                         | Pass/Fail |
|--------------------|---------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Update Recipe      | Access  | If a user tries to edit another user's recipe (by changing the url) they receive a custom 403 error. (forbidden access) | Pass      |
| Update Recipe      | Access  | If a user tries to edit a recipe (by changing the url) without being signed in they are redirected to the login page    | Pass      |
| Update Recipe Form | Display | Form has all the fields filled out with the original content                                                            | Pass      |
| Update Button      | Click   | Updated recipe is saved                                                                                                 | Pass      |
| Update Button      | Click   | Success message appears telling the user that the recipe has been successfully updated                                  | Pass      |
| Update Button      | Click   | Success message fades after 3 seconds                                                                                   | Pass      |
| Update Button      | Click   | User is redirected back to the current recipe page                                                                      | Pass      |
| Cancel Button      | Click   | User is redirected back to the current recipe page                                                                      | Pass      |
### Confirm Delete Recipe Page
| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| Delete recipe | Access | If a user tries to delete another user's recipe (by changing the url) they receive a custom 403 error.                 | Pass      |
| Delete recipe | Access | If a user tries to delete a recipe (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Delete Button | Click  | Recipe is deleted and removed from user recipes page                                                                   | Pass      |
| Delete Button | Click  | Success message appears telling the user that the recipe has been successfully deleted                                 | Pass      |
| Delete Button | Click  | User is redirected back to the My recipes page                                                                         | Pass      |
| Cancel Button | Click  | Redirect to current recipe page                                                                                        | Pass      |

### My Recipes Page
| Element         | Action               | Expected Result                                                                                                  | Pass/Fail |
|-----------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| My Recipes Page | Access               | If a user tries to access this page (by changing url) without being signed in they are redirected to the Login page | Pass      |
| My Recipes Page | Display              | Only displays the recipes that the user is the author for                                                        | Pass      |
| Recipe Card     | Show Status          | Show if recipe is draft                                                                             | Pass      |
| Recipe Card     | Card Content Display | Display correct image, recipe title and cooktime                                                                 | Pass      |
| Recipe Card     | Click                | Clicking anywhere inside the recipe card takes you to the correct recipe's detail page.                          | Pass      |
| Recipe Card     | Pagination           | Site will paginate 8 recipe cards to a page                                                                      | Pass      |
| Recipe Card     | Order                | Recipes are sorted by newest to oldest                                                                           | Pass      |
| Recipe Card     | Hover                | Display gold border                                                                                              | Pass      |
### My Bookmarks Page

| Element           | Action               | Expected Result                                                                                                  | Pass/Fail |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| My Bookmarks Page | Access               | If a user tries to access this page (by changing url) without being signed in they are redirected the Login page | Pass      |
| My Bookmarks Page | Display              | Only the recipes the user has book marked are shown                                                              | Pass      |
| Recipe Card       | Card Content Display | Display correct image, recipe title and cook time                                                                | Pass      |
| Recipe Card       | Click                | Clicking anywhere inside the recipe card takes you to the correct recipe's detail page.                          | Pass      |
| Recipe Card       | Pagination           | Site will paginate 8 recipe cards to a page                                                                      | Pass      |
| Recipe Card       | Order                | Recipes are sorted by newest to oldest                                                                           | Pass      |
| Recipe Card       | Hover                | Display gold border                                                                                              | Pass      |
### My Meal Plan Page
| Element           | Action               | Expected Result                                                                                                  | Pass/Fail |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| My Meal Plan Page | Access               | If a user tries to access this page (by changing url) without being signed in they are redirected the Login page | Pass      |
| Meal Plan card    | Order                | Cards are ordered from Monday to Sunday                                                                          | Pass      |
| Meal Plan card    | Card Content Display | If populated: Display correct image, recipe title                                                                | Pass      |
| Meal Plan card    | Card Content Display | If unpopulated: display placeholder image and 'Add Recipe'                                                       | Pass      |
| Meal Plan card    | Click                | If populated: clicking anywhere inside the recipe card takes you to the detailed page for that recipe            | Pass      |
| Meal Plan card    | Click                | If unpopulated:  clicking anywhere inside the recipe card takes you to the browse recipes page                   | Pass      |
| Meal Plan card    | Hover                | Display gold border                                                                                              | Pass      |

### Django All Auth Pages
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Sign Up                    |                                           |                                            |           |
| Log in link                | Click                                     | Redirect to login page                     | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert correct format                     | On submit: form submit                     | Pass      |
| Username field             | Insert duplicate username                 | On submit: form won't submit               | Pass      |
| Username field             | Insert duplicate username                 | Error message displays                     | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty                               | On submit: form submit                     | Pass      |
| Email field                | Insert duplicate email                    | On submit: form won't submit               | Pass      |
| Email field                | Insert duplicate email                    | Error message displays                     | Pass      |
| Password field             | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Password field             | Insert incorrect format                   | Error message displays                     | Pass      |
| Password field             | Passwords don't match                     | On submit: form won't submit               | Pass      |
| Password field             | Passwords don't match                     | Error message displays                     | Pass      |
| Password field             | Insert correct format and passwords match | On submit: form submit                     | Pass      |
| Sign Up button(form valid) | Click                                     | Form submit                                | Pass      |
| Sign Up button(form valid) | Click                                     | Redirect to home page                      | Pass      |
| Sign Up button(form valid) | Click                                     | Success message confirming login appears   | Pass      |
| Sign Up button(form valid) | Click                                     | Success message fades after 3 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log in                     |                                           |                                            |           |
| Sign up link               | Click                                     | Redirect to sign up page                   | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert wrong username                     | On submit: form won't submit               | Pass      |
| Username field             | Insert wrong username                     | Error message displays                     | Pass      |
| Password field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Password field             | Leave empty                               | Error message displays                     | Pass      |
| Password field             | Insert wrong password                     | On submit: form won't submit               | Pass      |
| Password field             | Insert wrong password                     | Error message displays                     | Pass      |
| Login button(form valid)   | Click                                     | Form submit                                | Pass      |
| Login button(form valid)   | Click                                     | Redirect to home page                      | Pass      |
| Login button(form valid)   | Click                                     | Success message confirming login appears   | Pass      |
| Login button(form valid)   | Click                                     | Success message fades after 3 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log Out Confirmation       |                                           |                                            |           |
| Logout button              | Click                                     | Redirect to homepage                       | Pass      |
| Logout button              | Click                                     | Success message confirming log out appears | Pass      |
| Logout button              | Click                                     | Success message fades after 3 seconds      | Pass      |

## Bugs 
error: Uncaught TypeError: Cannot read properties of null (reading 'defaultPrevented')
sol: if(messages != null)

https://developer.chrome.com/docs/lighthouse/performance/render-blocking-resources/
performance

draft chice 404 error


Back to [README.MD](README.MD)<br>
 