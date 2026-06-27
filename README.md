# Milestone 3: Virtual Memorial and Tribute Space

<figure>
    <img src="assets/amiresponsive.webp"
         alt="Laurie Irvine Memorial loading on a monitor, laptop, tablet and phone">
</figure>


## In Loving Memory - Virtual Memorial & Tribute Space

### Project Overview & Context

This web application has been developed for Milestone 3 of the Code Institute Level 5 Diploma in Web Application Development. The brief was to develop and implement a responsve, full-stack, database-back web application using Python, Django framework and a relational database. 

I have created a private virtual memorial and tribute space dedicated to the memory of my late father. It provides an interface where family, friends and community can easily read a shared timeline of condolences, submit their own text-based tributes and light a virtual candle.


You can view the deployed application here [Laurie Irvine Memorial](https://web-production-721e.up.railway.app/)


![Github Last Commit]( https://img.shields.io/github/last-commit/MrsG33k/CI-MS3-Tribute)
![Github language count](https://img.shields.io/github/languages/count/MrsG33k/CI-MS3-Tribute)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)


* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### Target Audience
Family members, friends, neighbours, colleagues wishing to share condolences and memories or light a virtual candle.

### User Stories

#### First Time Visitor goals
* As a First Time Visitor, I want to see a clean timeline of tributes and memories left by others without having to navigate a complicated website layout.

* As a First Time Visitor, I want to easily find and fill out a simple guestbook form with my name, relationship and a personal memory without being forced to create an account.

* As a First Time Visitor, I want to light a virtual candle alongside my message so that I can show my support


#### Returning Visitor goals
* As a Returning Visitor, I want to revisit the page and see an updated total counter of how many virtual candles have been lit, so that I can see the ongoing support from friends and family over time.

* As a Returning Visitor, I want to search for a specific tribute by a particular person, or a keyword so that I can read the story and share others memories.

* As a Returning Visitor, who has already left a memory, I want to ensure that nobody else can accidentally edit or delete it from the front end. 

## Design


### Colour Scheme

This is a deeply personal project paying tribute to my dad who was a massive Chelsea FC fan. I decided from the start that I wanted to include the colours from the Chelsea FC logo into the design. This included Blue, White and Gold. 
<br>
<img src ="assets/colourpalette.webp" alt="Colour palette of Blue, Gold and off white for the website" width="500" align="left">
<img src="assets/chelsealogo.webp" alt="Chelsea FC logo" width ="300">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
I used [coolors](https://coolors.co/) to create my colour palette.
These colours have been used in the following way:
* I have used `#034694` as the button backgrounds and the card accent colours.
* I have used `#034694` as the text colour and the header / footer colours.
* I have used `#eea925` as accents between sections and the text for the footer. `
* I have used `#fff` for the header text, to stand out against the blue background, the background for the candles lit count.

For this project I used CSS styles for colours throughout the project. Instead of hard-coding hex codes in the various styles I declared the colour palette as global variables in the `root:` selector. This made sense for many reasons, primarily because the colours need only be declared once. Any follow up changes or tweaks to colours can be made in one place and updated throughout.

By using `var` to insert the value of a variable it also means I can give them semantic meaning. So instead of a variety of different Hex code, I instead have `var(--accent-colour)` which is brilliant for readability throughout.  
 

### Typography

I used [Google Fonts](https://fonts.google.com/) for this project. 

* For headings / titles I used <strong>Oswald</strong>. I chose this font as I wanted a sans-serif clean looking font that was easy to read but still strong and stylish.

  <img src="assets/fontoswald.webp" alt="The Oswald font spelling In Loving Memory">
  <hr>
  <br>
* For the main body text, I wanted to include a sans serif font for readability so I used <strong>Inter</strong>. 

   <img src="assets/fontinter.webp" alt="The inter font spelling Leave a Tribute">

  <hr>
  <br>
* For the footer text, I wanted to include a calligraphy style font, so it read like we were leaving a signature at the bottom, but I didn't want anything to intricate that would be difficult to read, so I went with <strong>Alex Brush</strong>. 

   <img src="assets/fontalexbrush.webp" alt="The Alex Brush font spelling Love from Carol">

### Imagery

* Logo / Header - For the logo, I wanted a simple image of my dad at his favourite place, Stamford Bridge. I used a photo I had taken back in 2023 and used [Photopea](http://www.Photopea.com) to remove the background. 

   <img src="assets/dadoriginal.webp" alt="Photo of a man in a football stadium sat on the players bench" width="200">  
   Before editing
   <br>
  
    <img src="assets/dadcutout.webp" alt="Photo of a man in a football kit, with the background removed." width="150">  
    After editing
    <br>
<br>
<br>

* Emojis - For all of the other imagery on the website I have used the standard emojis:
  * Candle: 🕯️
  * Football: ⚽
  * Search: 🔍
  * Padlock: 🔒



### Wireframes
Wireframes were created using [Canva](https://www.canva.com)


#### Desktop
<figure>
    <img src="assets/desktop1.webp" width='800'
         alt="Desktop wireframe of the top of memorial page">
    <figcaption>This shows the view on page load - You will see the header with photo of Laurie, the left hand will contain the form to write the tribute, with the right hand side acting as a display of all tributes left.</figcaption>
</figure>
<figure>
    <img src="assets/desktop2.webp" width='800'
         alt="Desktop wireframe of the bottom of the memorial page">
    <figcaption>This shows the view when scrolling to the bottom - The right hand side will continue to show the display of tributes left, with a bold footer at the bottom with a signature from the family and admin portal login for maintenance of the tributes left.</figcaption>
</figure>



#### Mobile
<figure>
    <img src="assets/mobile1.webp" width='300'
         alt="Mobile wireframe on page load">
    <figcaption>This shows the view on mobile on page load. It's important that users can see whe the memorial is for and be presented with the form to leave a tribute clearly.</figcaption>
</figure>

<figure>
    <img src="assets/mobile2.webp" width='300'
         alt="Mobile wireframe on scroll">
    <figcaption>This shows the view on mobile on page scroll. It shows all of the tributes left before reaching the footer at the bottom containing the family signature and admin login portal.</figcaption>
</figure>



## Features
The Virtual Memorial and Tribute space contains the following features:

* index.html - The primary view template which serves as both the tribute timeline feed and the form submission handling.
* /admin - The Django admin portal which allows registered users to edit and delete tributes as necessary.


### Favicon
The page has a a favicon of a candle image. This was chosen to make it obvious that the website was a memorial - as traditionally candles are used as a symbol.
<img src="assets/favicon.webp" width="400" alt="Screenshot of webpage address bar showing favicon">


### Header
The page has a header section containing a cutout photo of Laurie Irvine against a textured background. The name of the tribute page is visualised in a bold font <strong>In loving memory of Laurie Irvine</strong> Below the text is a poem to remember Laurie. The last thing on the header is a count of the number of candles lit. 
<br>
<img src="assets/header.webp" width="600" alt="Screenshot of website header">

### Footer
The page has a simple footer section containing a gold signature of the family, followed by a link to the admin portal login. 
<img src="assets/footer.webp" width="600" alt="Screenshot of website footer">

### Index.html
* The left hand grid (Using .col-4 flex) - Leave a Tribute form - This will allow users to leave a tribute and if they want to light a virtual candle in memory of Laurie Irvine.

<figure>
    <img src="assets/addtribute.webp" width='300'
         alt="The add tribute section of the webpage">
    <figcaption>This shows the section for adding a tribute on the desktop view</figcaption>
</figure>

* The right hand grid (Using .col-8 flex) - View the Tributes - This will allow users to scrol, search and view any tributes left. 
  * A search bar - to search for any particular keywords.
  * The name of the person who left the tribute
  * The relationship
  * Whether they lit a candle
  * The tribute content itself
  * The date/time the tribute was left

<figure>
  <img src="assets/readtribute.webp" width='500'
        alt="The read tribute section of the webpage">
  <figcaption>This shows the section for searching and reading a tribute on the desktop view</figcaption>
</figure>

<br>
<img src="assets/amiresponsiveindex.webp" width="600" align="center" alt="Am I responsive view of the index loading on a tablet, screen, phone">
<br>


### /admin

The admin allow registered users to log into the Django admin panel to maintain the tributes left. 
<figure>
  <img src="assets/adminlogin.webp" width='400'
        alt="The admin login page">
  <figcaption>This shows the view when a user arrives at the admin portal</figcaption>
</figure>
<br>
<figure>
  <img src="assets/adminloggedin.webp" width='400'
        alt="The admin view once logged in">
  <figcaption>This shows the view when a user successfully logs in to the admin portal</figcaption>
</figure>
<br>
<figure>
  <img src="assets/adminmemorialview.webp" width='400'
        alt="The admin memorial view of posts">
  <figcaption>This shows the view of all of the tributes currently left</figcaption>
</figure>
<br>
<figure>
  <img src="assets/adminactions.webp" width='400'
        alt="The admin memorial view of a single tribute">
  <figcaption>This shows the view of how the admin can edit / delete a particular tribute.</figcaption>
</figure>

### Future Implementations

* **Media Attachments** I would like to expand the tribute form further to allow users to upload media alongside their tribute. This is primarily looking at photographs, but could be video files, audio files and documents. This would involve using Djangos `FileField` or `ImageField` models and also incorporating cloud media storage to store the assets uploaded.

* **User led edits / deletes** The current admin login allows family members to edit and delete entries. I would like to explore giving users the option to create an account which would then allow them the options to edit or delete their entries. 

* **Light / Dark system mode toggle** To aid with accessibility a toggle control to allow users to choose between light and dark mode would allow users to instantly switch the layout to suit their needs / devices. This could be implemented using some Javascript and adding alternate colours to the current CSS files.


### Accessibility

Throughout this project, I have aspired to make it as accessible as possible to ensure all family, friends, and other users can easily navigate the page.

#### Design
I deliberately chose a clean, high-contrast design throughout the project. The off-white background colour (`#F4F4F9`) was carefully selected to be gentler on the eyes than a stark, pure white background. Keeping the interface minimal and avoiding cluttered design patterns aids visitors with visual or cognitive impairments. 

The UI has been built using a mobile-first approach, ensuring that elements stack cleanly. It features large, touch-friendly interactive targets at all points of engagement (such as the form inputs and the search button). The navigation loop is exceptionally simple; because it is a single-page wall layout with a dedicated backend dashboard link, visitors can scroll fluidly without any complex menus or login required.

#### Coding
I have used semantic HTML structures and descriptive ARIA labels throughout to fully support those using assistive technologies, keyboard navigation, and screen readers.

| Element | ARIA / Semantic Attribute | Purpose |
| :--- | :--- | :--- |
| Interactive Form Controls | `required`, clear `<label for="...">` linking | Ensures screen readers announce exact field expectations for names and messages. |
| Global Candle Counter | Semantic wrapper with clear text description | Automatically announces the changing candle metrics cleanly to visually impaired users. |
| Search Bar Input | `type="search"` and `aria-label="Search"` | Signals to assistive technologies that this block functions as an interactive filtering tool rather than standard text. |
| Administrative Links | Decorative iconography separate from link tags | Guarantees screen readers speak the literal destination (e.g., "Family Admin Portal Access") instead of reading aloud structural symbol characters. |

## Database Schema & Entity Relationship Diagram (ERD)

Whilst the primary tribute interaction relies on a custom data model (`tracker_memorialpost`), the application's backend architecture utilises a relational framework by interfacing with Django's core authentication tables to secure administrative privileges for the relevant family users.

Below is the Entity Relationship Diagram representing the active database schema hosted on Railway:

<figure>
    <img src="assets/dberd2.webp" alt="Entity Relationship Diagram showing the custom tracker_memorialpost and Django Auth User tables">
    <figcaption>Entity Relationship Diagram (ERD) mapping out the tracker_memorialpost and Django Auth User tables.</figcaption>
</figure>

#### Design Justification: Why the Tables Aren't Directly Linked

The `tracker_memorialpost` table intentionally remains unlinked by a direct **Foreign Key (FK)** relationship to the `auth_user` table. This design pattern was a deliberate architectural choice based on the project's user requirements and  user experience (UX) goals:

1. **Authentication-Free Tribute Postings:** The aim of the tribute page is to allow family, friends, and ex-colleagues to quickly leave a tribute message or light a virtual candle *without* the need to create an account or login registration. 

2. **Decoupling Public Inputs from family admin profiles:** Because standard visitors do not have corresponding rows inside the `auth_user` table, forcing a Foreign Key constraint on the `author_name` or `user_id` would break database integrity, making it impossible for public users to save records. 

3. **Administrative Isolation:** The `auth_user` and `django_session` tables exist separately to manage authenticating and tracking active administrative sessions. The staff accounts use Django's underlying object-relational mapping (ORM) privilege layers to gain access to the row manipulation controls (Update/Delete) over `tracker_memorialpost` within the administrative workspace, removing the need for a rigid database-level schema link.

### Database Architecture & CRUD Realization

This project fully implements standard relational database CRUD (Create, Read, Update, Delete) architecture using Django Views, a PostgreSQL database model, and an administrative user interface:

| Operation | Target Feature | Implementation Details |
| :--- | :--- | :--- |
| **CREATE** | Tribute Form | Visitors submit entries via a front-end form using a `POST` method. This saves input strings (`author_name`, `relationship`, `tribute_text`) and boolean values (`light_candle`) directly into the PostgreSQL database. |
| **READ** | The Memorial Wall Feed | Django queries records from the backend and passes them to the template via a context dictionary (`tributes`), rendering them in reverse-chronological order. |
| **LOCATE** | Dynamic Search Filter | Users can isolate specific entries instantly. The view captures URL parameters using `request.GET.get('q')` and runs database filter lookups using `Q` objects to filter fields case-insensitively. |
| **UPDATE** | Family Administrative Portal | Authorized family members can securely modify the names, relationship labels, or content of any tribute via the built-in admin workspace. |
| **DELETE** | Content Curation Controls | Spammed, duplicated, or erroneous messages can be instantly and permanently removed from the server by family users via the secure backend layout. |



## Technologies Used

* **Languages:** HTML5, CSS3, Python
* **Frameworks:** Django, Bootstrap 5
* **Database:** PostgreSQL
* **Hosting:** Railway

### Libraries & Programs Used


* [Canva](https://www.canva.com/online-whiteboard/wireframes/) - Used to create wireframes.

* [Git](https://git-scm.com/) - For version control.

* [Github](https://github.com/) - To save and store the files for the website.

* [VS Code](https://code.visualstudio.com/) - IDE used to create the site.

* [Google Fonts](https://fonts.google.com/) - Google fonts were used to import the 'Oswald', 'Inter' and 'Alex Brush' fonts into the project.

* [To WebP](https://towebp.io/) - Used to convert images to WebP format.

* [Photopea](https://www.photopea.com/) - Used to edit and create graphics for the project

* [Favicon.io](https://favicon.io/) - Used to create the favicon based on the logo

* [dbdiagram.io](https://dbdiagram.io/) - Used to create the Entity Relationship Diagram



## Deployment & Local Development


### Deployment to Railway

The application is deployed to **Railway** linked to a live **PostgreSQL** relational database using the following steps:

1. Log into the [Railway](https://www.railway.com) Dashboard, or create a new account
2. From the dashboard - Create a New Project and choose to deploy from a GitHub repository. (This will require you to link your Github account to your Railway account)
3. Inside that project click on **+ Add** and create a Database > PostgreSQL (This will then spinup a new database for you)
4. Set up the required environment variable key-value tokens within the Railway variables panel:
   * `SECRET_KEY`: Your private Django security string.
   * `DEBUG_VALUE`: Set to `False` in production environments.
   * `DATABASE_URL`: Automatically generated by mapping your associated PostgreSQL database instance link.
5. Configure the deployment start command to run asset compiling BEFORE executing the WSGI container:
  `python manage.py collectstatic --noinput && gunicorn core_project.wsgi`
6. Commit any changes to your main branch on your GitHub Repository. Railway will automatically pick up the push, initialize the container build sequence, run migrations, and publish the live web URL.

Railway also has their own guide on how to deploy which can be found [here](https://docs.railway.com/quick-start#deploying-your-project---from-github)

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Cloning the GitHub Repository

By cloning the Github Repository we make a copy of the original repository on a local computer allowing you to interact with files directly in an editor, such as VS Code. 

1. On GitHub, navigate to your fork of the repository.
2. Click the green **Code** button located above the file directory.
3. Copy the URL string provided (HTTPS or SSH alternative).
4. Open your local machine's terminal window, navigate to where you want the project to live, and enter the following git command:
   ```bash
   git clone [https://github.com/MrsG33k/CI-MS3-Tribute.git](https://github.com/MrsG33k/CI-MS3-Tribute.git)
5. Navigate into the newly created folder
   ```bash
   cd CI-MS3-Tribute
6. Intitialise your Python Virtual Environment layer (.venv) and run the setup parameters locally:
   ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    python3 manage.py migrate
    python3 manage.py runserver

## Testing
Please refer to [TESTING.md](TESTING.md) file for all testing carried out.

### Solved Bugs / Issues

| No | Feature | Issue | Fix |
| :--- | :--- | :--- | :--- |
| 1 | Tribute Wall | When adding a tribute, the entries nest rather than showing as indivdual entries. <img src="assets/bug1nesting.webp" align="left" alt="Screenshot of nesting tributes" width="200"> | The for loop to display the entries was missing a closing div tag, which was causing the loop to not work correctly |
| 2| Header Section| After changing the initial header image, the image appeared to be floating, rather than lying flush against the gold border. <img src="assets/bug2floating.webp" align="left" alt="Screenshot of image of floating header" width="200"> | I changed the flexbox grid ratio slightly to give the image more space and forced a zero margin / padding at the bottom of the image <img src="assets/bug2fix.webp" align="left" alt="Screenshot of the fixed image placement" width="200"> |
| 3| Header Section| After making the changes for Bug 2, on inspection it appeared that the new grid spacing, made the image shrink significantly on tablet modes. Making the text larger, and the image insignificant.  <img src="assets/bug3shrink.webp" align="left" alt="Screenshot of image of floating header" width="200"> | I decided to make use of Bootstraps responsive layout (col-md-6 , col-lg-5) to ensure the memorial image scales fluidly and sits flush against the gold border across all device viewports.  <img src="assets/bug3fix.webp" align="left" alt="Screenshot of the fixed image placement" width="200"> |
| 4| Deployment| The deployed application  on Railway was throwing a ``` FATAL: password authentication failed for user "postgres" ``` error on startup. | To begin with I checked that the database credentials matched the environment variables and used Railways password reset to force a resync/redeployment to check this wasn't the issue. After looking on the Railway forums for similar queries, I eventually realised it was the ``` dj_database_url ``` import that was causing the issue. I am still not entirely sure why it was causing the issue, i can only assume a character or similar was causing slicing issues when reading the string. After removing the ```dj_database_url ``` I resorted to using the Django DATABASES setting to explicitly read Railway's individual environment variables using ```os.environ.get() ``` which was in the official Railway Django deployment guide  |
| 5| Deployment| Once the application was functioning correctly, I turned the ``` DEBUG = True ``` to use a toggled format that keeps it True in development, but False once in production. ```DEBUG = os.environ.get('DEBUG_VALUE', 'True') == 'True'```. This threw up a new problem whereby Django wasn't picking up any of the images or styling, and would give a Server Error (500) with the Railway logs showing ```UserWarning: No directory at: /app/staticfiles/.``` | I spent some time looking at the Whitespace documentation (see link in credits). It turns out, that despite Whitenoise being configured correctly, Railway itself hadn't created the ```/app/staticfiles/``` directory inside the container. Therefore I needed to update the Start Command inside the Railway dashboard to tell it to execute Djangos asset compilation command BEFORE launching Gunicorn. This was achieved by updating the start command in Railway Deploy to ```python manage.py collectstatic --noinput && gunicorn core_project.wsgi```  |


## Credits

- [Deploying Django to Railway](https://www.youtube.com/watch?v=A4Pn2lEdoLQ&start=0): YouTube video by Coding Entrepreneurs to help with issues when deploying Django to Railway App.
- [Railway User Guides](https://docs.railway.com/guides/django): Railway official guides to support deploying Django app to Railway.
- [Whitespace with Django](https://whitenoise.readthedocs.io/en/stable/django.html): Used to help fix issue with styling / images not displaying on production app.
- [Django Lookups with Q objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#complex-lookups-with-q-objects): Used when implementing the search functionality 
- [Django Search Tutorial](https://learndjango.com/tutorials/django-search-tutorial): Used alongside the link above when implementing the search bar functionality  



### Code Used
- [CSS3 Patterns Gallery](https://projects.verou.me/css3patterns/#carbon): Design by Atle Mo and code by Sebastien Grosjean. Modified for the blue header.



###  Media


- [https://shields.io/](https://shields.io/) - To create the badges on the README introduction
- [https://www.flaticon.com/free-icon/candle_2146319?term=candle&page=1&position=12&origin=search&related_id=2146319](https://flaticon.com) - Image of a candle used for the Favicon by JustIcon


### Acknowledgments

This project is a deeply personal tribute, and its successful implementation would not have been possible without the invaluable support, feedback, and encouragement of family and friends:

* **Michael Whittaker:** For providing technical troubleshooting assistance during the initial deployment phase to Railway, and for thorough cross-device compatibility testing to ensure a seamless responsive user experience.
* **Elaine Hopkins:** For offering insightful design feedback that directly helped shape and polish the final grid layout and structural header aesthetics.
* **My Mum and Sister:** For their heartfelt collaboration, guidance, and continuous involvement throughout the creative process, specifically in choosing the typography, refining the wording of the page, and selecting the perfect header photograph to honor our dad's memory.