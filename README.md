# PP5_api (bjjconnect) - Backend


[**BJJConnect**](https://pp5-bjj-api-2269f4220822.herokuapp.com/) uses [Django Rest Framework](https://www.django-rest-framework.org) to serve as its API to interface with its frontend [React](https://www.npmjs.com) JavaScript library. 

This project evolved out of a project, which centred around a fictional BJJ autisiasts to share events and posts  '**[BJJconnect](https://bjj-fcb7bcc1efc9.herokuapp.com/)**'.



- **[Click Here](https://bjj-fcb7bcc1efc9.herokuapp.com/)** to see the deployed website. 

- To view the frontend repository on Github **[Click Here](https://github.com/SamOBrienOlinger/spoodle-space-pp5)**. 

## **Summary**
  This social platform provides Users with an opportunity to connect and share photographs, and even information about owning, training and taking care of a breed of dog called Cockapoos, one of Ireland's newest, most popular and much-loved dog breeds. 
  
  Unlike many other social networking platforms, this project offers Users a unique way to create and participate in their own community of likeminded people with a shared identity that self-sustains itself. A fundamental intended outcome is to produces a sense of belonging that cannot be found elsewhere.    

The site is designed to engage as wide a range as possible of millions of potential Users around the world, including:

* families, couples and individuals who already have a Cockapoo or two that are eager to learn more about the history and nature of the breed of their fun furry companions. 

* folks who would like to find out more about taking care of their dog so their hairy little buddy stays happy and healthy. 

* anyone considering opening their home to a new companion of this breed of dog and are hoping to gather more information to help make their decision. 

 * Cockapoo owners who enjoy connecting with other Cockapoo owners by sharing funny stories,  photographs and videos of their adventures.

* Anyone who is looking for some support and/or who can provide otyher with support related to any challenges they are facing with the behaviour of their loved little clowns!  


Given the site goals outlined here, enhancing the UI and UX to achieve the project's most important goals required prioritising the way backend data connected with the front-end application. 

## Contents

- [User Stories](#user-stories)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

### [User Stories](#user-stories)

  **Navigation and authentication**

  - Navigation: As a user, I can view a navbar from every page so that I can navigate easily between pages.
  - Routing: As a user, I can navigate through pages quickly so that I can view content seamlessly without page refresh.
  - Authentication - Sign up: As a user, I can create a new account so that I can access all the features for signed-up users.
  - Authentication - Sign in: As a user, I can sign in to the app so that I can access functionality for logged-in users.
  - Authentication - Logged in Status: As a user, I can tell if I am logged in or not so that I can log in if I need to.
  - Authentication - Refreshing access tokens: As a user, I can maintain my logged-in status until I choose to log out so that my user experience is not compromised.
  - Navigation: Conditional rendering - As a logged-out user, I can see sign-in and sign-up options so that I can sign in/sign up.
  - Avatar: As a user, I can view users' avatars so that I can easily identify users of the application.

  **Profile**

  - Profile page: As a user, I can view other users' profiles so that I can see their posts and learn more about them.
  - Most followed profiles: As a user, I can see a list of the most followed profiles so that I can see which profiles are popular.
  - As a user, I can view data about other users, such as the number of posts, follows, and users followed so that I can learn more about them.
  - Follow/Unfollow a user: As a logged-in user, I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed.
  - View all posts by a specific user: As a user, I can view all the posts by a specific user so that I can catch up on their latest posts or decide I want to follow them.
  - Update username and password: As a logged-in user, I can update my username and password so that I can change my display name and keep my profile secure.

  **Posting, liking, dislikeing  and commenting on images**

  - Create posts: As a logged-in user, I can create posts with images.
  - View a post: As a user, I can view the details of a single post so that I can learn more about it.
  - Like a post: As a logged-in user, I can like a post so that I can show my support for the posts that interest me.
  - Post page: As a user, I can view the posts page so that I can read the comments about the post.
  - Edit post: As a post owner, I can edit my post title and description so that I can make corrections or update my post after it was created.
  - Create a comment: As a logged-in user, I can add comments to a post so that I can share my thoughts about the post.
  - Comment date: As a user, I can see how long ago a comment was made so that I know how old a comment is.
  - View comments: As a user, I can read comments on posts so that I can read what other users think about the posts.
  - Delete comments: As an owner of a comment, I can delete my comment so that I can control the removal of my comment from the application.
  - Edit a comment: As an owner of a comment, I can edit my comment so that I can fix or update my existing comment.

 

### [Entity Relationship Diagram](#entity-relationship-diagram)

- Built-in Django models were used for this project and the strucure of the intial relationship digram has been changed when application was tested withthe frontend.

# Models

### Post

The Post model is designed to contain all the relevant information regarding a post within the system.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| created_at     | DateTimeField | auto_now_add=True                                   |
| updated_at     | DateTimeField | auto_now=True                                       |
| title          | CharField     | max_length=255                                      |
| content        | TextField     | blank=True                                          |
| image          | ImageField    | upload_to='images/', default='../default_post.jpg'  |
| image_filter   | CharField     | max_length=32, choices=Post.image_filter_choices    |

### Event

The Event model allows for creating and managing events within the system.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| created_at     | DateTimeField | auto_now_add=True                                   |
| updated_at     | DateTimeField | auto_now=True                                       |
| description    | TextField     |                                                     |
| date           | DateField     |                                                     |
| time           | TimeField     |                                                     |
| location       | CharField     | max_length=200                                      |
| image          | ImageField    | upload_to='images/', default='../default_event.jpg' |

### Comment

The Comment model allows users to create comments on posts.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| post           | ForeignKey    | Post, on_delete=models.CASCADE                      |
| created_at     | DateTimeField | auto_now_add=True                                   |
| updated_at     | DateTimeField | auto_now=True                                       |
| content        | TextField     |                                                     |

### EventComment

The EventComment model allows users to create comments on events.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| event          | ForeignKey    | Event, on_delete=models.CASCADE                     |
| created_at     | DateTimeField | auto_now_add=True                                   |
| updated_at     | DateTimeField | auto_now=True                                       |
| content        | TextField     |                                                     |

### Profile

The Profile model extends the default User model with additional data.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | OneToOneField | User, on_delete=models.CASCADE                      |
| created_at     | DateTimeField | auto_now_add=True                                   |
| updated_at     | DateTimeField | auto_now=True                                       |
| name           | CharField     | max_length=255, blank=True                          |
| belt_color     | CharField     | choices=Profile.belt_choices, default='white'       |
| gi_or_no_gi    | CharField     | choices=Profile.gi_or_no_gi_choices, null=True      |
| years_trained  | IntegerField  | default=0                                           |
| profile_image  | ImageField    | upload_to='images/', default='../default_profile.jpg' |
| introduction   | TextField     | null=True, blank=True                               |
  
### Follower

The Follower model tracks the follow relationships between users.

| Database Value | Field Type    | Field Argument                                         |
| -------------- | ------------- | ------------------------------------------------------ |
| owner          | ForeignKey    | User, related_name='following', on_delete=models.CASCADE |
| followed       | ForeignKey    | User, related_name='followed', on_delete=models.CASCADE |
| created_at     | DateTimeField | auto_now_add=True                                      |

### PostLike

The PostLike model is used to store likes for a post by users.

| Database Value | Field Type    | Field Argument                                     |
| -------------- | ------------- | -------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                     |
| post           | ForeignKey    | Post, related_name='post_likes', on_delete=models.CASCADE |
| created_at     | DateTimeField | auto_now_add=True                                  |

### EventLike

The EventLike model is used to store likes for an event by users.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| event          | ForeignKey    | Event, related_name='event_likes', on_delete=models.CASCADE |
| created_at     | DateTimeField | auto_now_add=True                                   |

### PostDislike

The PostDislike model is used to store dislikes for a post by users.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| post           | ForeignKey    | Post, related_name='post_dislikes', on_delete=models.CASCADE |
| created_at     | DateTimeField | auto_now_add=True                                   |

### EventDislike

The EventDislike model is used to store dislikes for an event by users.

| Database Value | Field Type    | Field Argument                                      |
| -------------- | ------------- | --------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                      |
| event          | ForeignKey    | Event, related_name='event_dislikes', on_delete=models.CASCADE |
| created_at     | DateTimeField | auto_now_add=True        


### [Technologies](#technologies)

- #### Languages

  -  [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- #### Frameworks, Libraries, Programs and Services Used
  - [Django:](https://www.djangoproject.com/)

  - [Django Rest Frameworks](https://www.django-rest-framework.org/).

  - [Git:](https://git-scm.com/)

  - [GitHub:](https://github.com/)

  - [PostgreSQL:](https://www.postgresql.org/)

  - [ElephantSQL:](https://www.elephantsql.com/)

  - [Heroku:](https://heroku.com/)
  
 ### [Testing](#testing)

  - ## Manual Testing

| Application    | Endpoint                     | Expected Result                                      | Pass/Fail |
| -------------- | ---------------------------- | ---------------------------------------------------- | --------- |
| Post           | /posts/                      | List all posts ordered by date.                      | Pass      |
| Post           | /posts/<int:pk>/             | Retrieve a single post's details.                    | Pass      |
| Post           | /posts/<int:pk>/edit         | Edit a post by the owner.                            | Pass      |
| Post           | /posts/<int:pk>/delete       | Delete a post by the owner.                          | Pass      |
| Event          | /events/                     | List all events ordered by date.                     | Pass      |
| Event          | /events/<int:pk>/            | Retrieve a single event's details.                   | Pass      |
| Event          | /events/<int:pk>/edit        | Edit an event by the owner.                          | Pass      |
| Event          | /events/<int:pk>/delete      | Delete an event by the owner.                        | Pass      |
| Comment        | /comments/                   | List all comments on posts by date.                  | Pass      |
| Comment        | /comments/<int:pk>/          | Retrieve a single comment's details.                 | Pass      |
| Comment        | /comments/<int:pk>/edit      | Edit a comment by the owner.                         | Pass      |
| Comment        | /comments/<int:pk>/delete    | Delete a comment by the owner.                       | Pass      |
| EventComment   | /event-comments/             | List all comments on events by date.                 | Pass      |
| EventComment   | /event-comments/<int:pk>/    | Retrieve a single event comment's details.           | Pass      |
| EventComment   | /event-comments/<int:pk>/edit| Edit an event comment by the owner.                  | Pass      |
| EventComment   | /event-comments/<int:pk>/delete | Delete an event comment by the owner.             | Pass      |
| Follower       | /followers/                  | List all follower relationships.                     | Pass      |
| Follower       | /followers/<int:pk>/delete   | Delete a follower relationship by the user.          | Pass      |
| PostLike       | /post-likes/                 | List all likes on posts.                             | Pass      |
| PostLike       | /post-likes/<int:pk>/delete  | Delete a like on a post by the owner.                | Pass      |
| EventLike      | /event-likes/                | List all likes on events.                            | Pass      |
| EventLike      | /event-likes/<int:pk>/delete | Delete a like on an event by the owner.              | Pass      |
| PostDislike    | /post-dislikes/              | List all dislikes on posts.                          | Pass      |
| PostDislike    | /post-dislikes/<int:pk>/delete | Delete a dislike on a post by the owner.           | Pass      |
| EventDislike   | /event-dislikes/             | List all dislikes on events.                         | Pass      |
| EventDislike   | /event-dislikes/<int:pk>/delete | Delete a dislike on an event by the owner.        | Pass      |
For further details of testing carried out on the React frontend relevant to verifying the backend functionality, please visit the **[frontend repository README.md file]()**



**Fixed Bugs**

  A new instance needed to be created and connected to the API to correct issues from previose submition. The env.py file and Heroku Config Vars were updated accordingly. 

### [Deployment](#deployment) 

Creating a database using ElephantSQL was first required. The following steps were taken to do this: 

- login to ElephantSQL.

- click 'Create new instance' on the dashboard.

- name the 'plan' and select the 'Tiny Turtle' option.

- select 'select region' and choose the nearest data centre to your location.

- click 'Review'.

- then go to the ElephantSQL dashboard and click on the 'database instance name' for this project.

- copy the ElephantSQL database URL to your clipboard.

- Return to the Heroku dashboard.


This project was deployed through Heroku using the following steps:

- Log into Heroku
- Select 'Create New App' from your dashboard
- Choose an app name
- Select the appropriate region based on your location
- Click 'Create App'

- On your dashboard, click the 'Deploy' tab
- Locate 'Deployment Method' and choose 'GitHub'
- locate your repository then click 'Connect'

- Click the 'Settings' tab
- Open the 'Config Vars' and click 'Reveal Config Vars'

- The following environment variables need to be added and match the same values in your env.py file:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY

- install psycopg2 and dj-database-urlth libraries to handle database connection.
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS:
  - set allowed_origins

- gitignore the env.py file
- generate a requirements.txt file

once all the variables are in place, choose the main branch and click 'Deploy Branch'.
Once the build is finished, click 'Open App' located at the top of the page. 

### [Credits](#credits)

  - Code Institute's [Moments](https://github.com/Code-Institute-Solutions/moments) module.

