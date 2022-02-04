BAKEAHOLIC BLISS
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643919077/static/css/Image_03-02-2022_at_20.07_y0ukvs.jpg">

DESCRIPTION
This is a website for baking recipes that provides users with different recipes including Vegan and Gluten-free. The blog allows users to view and interact by liking and commenting on posts by signing up and creating an account. The aim of this blog is to provide content/posts to help baking easy for the users. The blog provides all the ingredients and steps required for the baking process.

Check out the website here.

FEATURES

NAVIGATION BAR
The nav bar is featured on all pages of the website and is fixed to the top right. When clicked on, each link will bring the user to the respective page, and will also show a line below the links so they are visible whe you hover over them.

HOME PAGE
The home page has an image on the right side of the page which is one of the recipes i have on the website, and it also has the the heading Bakeaholic Bliss. The home page is basically a page that i wanted to just talk about what the users should expect of the blog, basically just a brief explanation about what the blog is about and letting them know that they need to created an account or register so they are able to like and comment on our posts.

RECIPES PAGE
This page consits of 9 recipes, at the top of the page i have a welcoming message to the page. As each page can displays 6 posts only, users can navigate to the "NEXT" page to view more recipes. There is also a "PREV" button which users can alternatively click on if they want to go back and look at the previous recipes. Each post is displayed in a card style with an image, author, date, title and like count. A Style has been applied so the user can hover over the text for the posts which will underline to indicate that this can be selected. Once selected the users is able to see all information about ingredients and steps to take when baking.

BLOG POST



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
<img src="https://res.cloudinary.com/dpm3pthvb/image/upload/v1643933810/static/css/A9144D12-0286-4370-A1EF-7D4C86ACAB63_gsuokt.jpg">

* Python
To test the Python code, I used the PEP8 Online Validation Service.

All files passed through the validator and no issues were detected with the exception of the settings.py. This was due to the rows in question being too long, however as these are auto generated by Django or the link name being too long these were not amended and left as they are.



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


* CREDITS



I would like to thank Tutor support for all their help.
My Mentor Chris Quinn

