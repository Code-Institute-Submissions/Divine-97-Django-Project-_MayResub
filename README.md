BAKEAHOLIC BLISS
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643919077/static/css/Image_03-02-2022_at_20.07_y0ukvs.jpg">

DESCRIPTION

This is a website for baking recipes that provides users with different recipes including Vegan and Gluten-free. The blog allows users to view and interact by liking and commenting on posts by signing up and creating an account. The aim of this blog is to provide content/posts to help baking easy for the users. The blog provides all the ingredients and steps required for the baking process.

Check out the website here.

USER STORIES

Site User Goals:

As a Site User I can like or unlike a post so that I can interact with the content
As a Site User I can leave comments on a post so that I can be involved in the conversation
As a Site User I can register an account so that I can comment and like
As a Site User/Admin I can view comments on an individual post so that I can read the conversation
As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral
As a Site User I can view a list of posts so that I can select one to read
As a Site User I can learn more about the site the purpose of the web app


Site Owner Goals:

As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
As a Site Admin I can create draft posts so that I can finish writing the content later
As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
As a Site User/Admin I can view comments on an individual post so that I can read the conversation
As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral


FEATURES

* NAVIGATION BAR
The nav bar is featured on all pages of the website and is fixed to the top right. When clicked on, each link will bring the user to the respective page, and will also show a line below the links so they are visible whe you hover over them.

* HOME PAGE
The home page has an image on the right side of the page which is one of the recipes i have on the website, and it also has the the heading Bakeaholic Bliss. The home page is basically a page that i wanted to just talk about what the users should expect of the blog, basically just a brief explanation about what the blog is about and letting them know that they need to created an account or register so they are able to like and comment on our posts.

* RECIPES PAGE
This page consits of 9 recipes, at the top of the page i have a welcoming message to the page. As each page can displays 6 posts only, users can navigate to the "NEXT" page to view more recipes. There is also a "PREV" button which users can alternatively click on if they want to go back and look at the previous recipes. Each post is displayed in a card style with an image, author, date, title and like count. A Style has been applied so the user can hover over the text for the posts which will underline to indicate that this can be selected. Once selected the users is able to see all information about ingredients and steps to take when baking.

* BLOG POST

Accessed once the user selects a recipe post from the 'Home' or 'Search' page. Recipe title and image displayed at the top 
Content is then followed by the ingredient list and method steps. Further below is the comment section which users can view even if not logged in. Comment section is available and displayed for logged in users who can submit a comment. This is then sent for approval which is a feature only the Admin can access. Alert is displayed to indicate the comment has been sent for approval. Approved comments can be viewed on the post.




* REGISTER PAGE
This page is accessed from the nav bar by clicking on the Register page, once the page loads, users have a choice to sign up to the website. Users will be asked to provide their user name, an email which is optional, and a password will be rquired to sign up to the website.

* LOGIN PAGE
This page is also accessed from the nav bar by clicking on the Login page. Existing users can enter their username and password and click on the login button. Once this is done, the user is then taken to the homepage and an alert pops up showing the user has successfully signed in. If the user inputs the wrong username or password, a message will displayed saying that the username or password is incorrect.

*LOGOUT PAGE
The page is accessed from the nav bar only if the user is logged in. Once the users clicks on the logout button, they are directed to a the sign out page to confirm if they want to log out.  Once the user is signed out they are redirected to the home page an alert will appear showing that the user has looged out

* FOOTER PAGE
All icons are include links to relevant social media which are at the bottom of every page and will open a new tab once clicked on. All icon links work on all pages.

* OTHER FEATURES
Admin can approve and delete comments on posts that users choose to comment on. Also only the admin can create posts on the blog.

* FEATURES TO IMPLEMENT
In the future I would like users to edit and delete their comments.
I also would like to notify users who already have signed up to get alert either through email when theres a new post/recipe. 
I would also like users to be able to post their own recipes but with the admins approval just to ensure the content is appropriate for the website.

* TECHNOLOGIES USED
HTML, CSS, PYTHON, JAVASCRIPT, HEROKU POSTGRESS, Font Awesome, Cloudinary

TESTING
* CSS
No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F8000-divine97-djangoproject-58ws0zudzzz.ws-eu30.gitpod.io%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

* HTML
No erros were found on the home page
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643931786/static/css/5AA0643D-7BFA-4E9C-AE44-70DB04E358A1_yb4ucx.jpg">

No errors were found on the register page
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643931786/static/css/5AA0643D-7BFA-4E9C-AE44-70DB04E358A1_yb4ucx.jpg">

No errors were found on the Login page
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643933705/static/css/C665DAB9-45BC-467D-85A9-03027E28AF42_uhjjg0.jpg">

No errors were found on Logout page
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643933810/static/css/A9144D12-0286-4370-A1EF-7D4C86ACAB63_gsuokt.jpg">

The Recipe page had a few errors that I was not able to correct
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643934669/static/css/6252FBC8-9A48-424A-AD84-C18C31510ABE_dab8va.jpg">

* Python
To test the Python code, I used the PEP8 Online Validation Service.

All files passed through the validator and no issues were detected with the exception of the settings.py. This was due to the rows in question being too long, however as these are auto generated by Django or the link name being too long these were not amended and left as they are.

* Admin Only User Story Testing

This section tests the user stories for the Admin only functions of the website.

The admin section is accessed by entering 'admin/' at the end of the url for the website. This displayed the login page for the admin from which they can login.
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643965818/5EFFB147-56C4-43FA-8FB0-FB8DBA9B1E63_hhpgbu.jpg">

The site admin has various actions available to be able to manage the website such as:

Delete users
Create/edit/delete posts and drafts
Approve and delete comments
From the home section of the admin page, by selecting the Users link under 'Authentication and Authorization' the admin can view the lists of users currently signed up to the website. The admin also has the permission to delete the users by selecting the username and from the drop down selecting the delete user option.

From the home section, the admin can also view comments added by users some of which are pending approval. This is accessed from the Comments link under the 'Blog' section. Approved comments are indicated with a green tick under the Approved column. Comments pending approval have the red cross icon. To approve the comment the admin has to tick the unapproved comment from the list, then from the action drop down select the 'Approve comments' option. By clicking Go button this will proceed to carry out the action to approve the selected comment. Once the comment has been approved the red cross icon will now become a green tick icon to indicate that the comment has now been approved. The approved comment can also be viewed on the website now.
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643969884/F4F99747-2DC6-4ABE-B46A-211EA09FBDD7_yzusgx.jpg">

Alternatively selecting the 'Delete selected comments' action will proceed to delete the comment selected. Users will also no longer be able to view the comment on the website.

From the home section, the admin can also view the posts on the website, create new posts and edit/delete any existing ones. This can be accessed from the Posts link under the 'Blog' section. By selecting this link, this will display all the current posts submitted on the website.
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643969707/82505AFF-1783-4927-9A9C-BB45D15D3DA3_msr1sf.jpg">

The admin can also click on an existing posts by selecting the post tile to view the editor. From this section the admin can edit the posts content, and also has the option to delete the post or to save the changes.
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643970117/C85A813A-BB3D-4C49-8220-D9FBA1DF874F_mk2e6w.jpg">

The admin can also create new posts by selecting the Add Post + button. This will open up the editor page which will allow the fields to be populated. The status of the post can also be toggled between Draft or Published. The Published posts can then be viewed on the website, whereas Draft posts cannot.

These particular admin only permissions cannot be accessed by any other users, and users cannot edit or delete comments or posts or access another users account.

The following user stories have been achieved from this section:

* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
* As a Site Admin I can create draft posts so that I can finish writing the content later
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
* As a Site Admin I can prevent unauthorised users from having access so that they cannot access admin content or other users' profiles



This section tests the user stories for the Admin only functions of the website.

The admin section is accessed by entering 'admin/' at the end of the url for the website. This displayed the login page for the admin from which they can login.

* DEPLOYMENT
The project was developed using GitPod and was deployed via the GitHub repository to Heroku.

The following steps were followed to deploy this project:

From the Heroku dashboard, select 'New' in the top right-hand corner.
Click 'Create new app'.
Enter the app name and choose region as Europe.
Click 'Create app'.
Select the 'Settings' tab, and scroll down to 'Buildpacks'.
Add 'Python' and save changes.
Scroll down to 'Config Vars' section, and add the 'KEY' and 'VALUE' for the CLOUDINARY_URL, DATABASE_URL and SECRET_KEY to run the app.
At the top of the page, click on the 'Deploy' section.
Select Github as deployment method.
Select 'Connect to Github', and locate the repository name and click on 'Connect' to link my Heroku app to my Github repository code.
To add the Postgres Database, click on the 'Resources' tab.
Under Add-ons, search for 'Heroku Postgres', click on the search result for this.
Select the 'Hobby Dev-Free' option and click submit order form which will add this to the Add-ons section.
Scroll further down, select 'Enable Automatic Deploys' and then select 'Deploy Branch' to deploy project.
After it has successfully deployed a 'view' button appears on screen and when clicked opens the deployed application.


CREDITS

* All my images, ingedients and methods for baking the recipes on my webiste were taken from [(BBC GOOD FOOD)](https://www.bbcgoodfood.com/)

* A large part of this project code was used and inspired from the Code Institute's I Think Therefore I Blog walkthrough to be able to build a base skeleton project. Please note some of the borrowed code has been customised by me to fit this project. I have also added my own code for additional functions for the project.

* I would like to thank Tutor support for all their help.
* My Mentor Chris Quinn

