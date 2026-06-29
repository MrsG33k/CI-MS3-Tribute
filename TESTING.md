# Virtual Memorial and Tribute Space -  Testing

<figure>
    <img src="assets/amiresponsive.webp"
         alt="Laurie Irvine Memorial loading on a monitor, laptop, tablet and phone">
</figure>

You can view the deployed application here [Laurie Irvine Memorial](https://web-production-721e.up.railway.app/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Lighthouse](#lighthouse)
  * [Accessible Web](#accessile-web)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along.


- - -

## AUTOMATED TESTING

### Code Validation Profiles

**[W3C Validator](https://validator.w3.org/)** was used to validate the HTML on the website. 

* [index.html](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fweb-production-721e.up.railway.app%2F) - Passed.

**[W3C Jigsaw CSS Validation Software](https://jigsaw.w3.org/css-validator/validator)** was used to validate the CSS on the website.
* index.html - Passed
        <p>
            <a href="https://jigsaw.w3.org/css-validator/check/referer">
                <img style="border:0;width:88px;height:31px"
                    src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
                    alt="Valid CSS!" />
            </a>
        </p>
<br>

**Python Code Quality Compliance** was used to test the python files in the application.
This was achieved as follows:
1. ````bash
    pip install flake8

2. ````bash
    flake8 tracker/

Flake8 will check against PEP8 guidelines to enforce clean styling, spacing conventions and prevent unexecuted code syntax blocks. As part of this testing I created a **.flake8** file. This was used to exclude any Boilerplate code and later on to exclude two E501 (line too long) errors from settings.py and models.py - these were excluded as there was no way to split the string across multiple lines. Other than the aforementioned errors - there were no further errors in the .py files.

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.


#### index.html

The initial result of the scan was 97 for Performance and 96 for Accessibility.
<figure>
    <img src="assets/lighthouse1.webp"
         alt="Scores for the lighthouse indexing on chrome dev tools">
</figure>

* **Performance Issues:** Bringing down this score were external libraries affecting the rendering time for the page load. The Bootstrap, Google Fonts and also the HTMX that is used on the Search were all included in this list. There is not a lot I can do myself to fix this, and shouldn't cause too much detriment to the performance.. One of the other issues was the size of the header image laurieheader.webp. 
<figure>
    <img src="assets/lighthouseimage.webp" width="600px"
         alt="A screenshot of the warning of the image size on chrome dev tools">
</figure>

To resolve the issue I opened the image back into Photopea and reduced the whole image size before exporting once again as a .webp file at reduced size and dimensions. 

* **Accessibility Issues:** Bringing down this score was a contrast issue on the font on the badge displaying the relationship on the memorial wall. It was using Bootstraps text-muted, which is a light grey. I changed it to text-secondary - A darker colour. Below is the before and after of the colour contrast

<figure>
    <img src="assets/lighthousecontrast.webp"
         alt="A screenshot of the warning of the contrast issues on chrome dev tools">
</figure>
<figure>
    <img src="assets/lighthousecontrastfix.webp"
         alt="A screenshot of the warning of the contrast issues on chrome dev tools">
</figure>

After performing these minor changes, the revised lighthouse results was much healthier:

<figure>
    <img src="assets/lighthouse2.webp"
         alt="Scores for the lighthouse indexing on chrome dev tools">
</figure>


### Accessible Web
Accessible web extension was used to check the website. 

#### Index.html

Two compliance warnings were flagged regarding the application's secondary text elements. 
<figure>
    <img src="assets/accessible1.webp" height="100px"
         alt="Screenshot of 2 warnings with the accessibility, one moderate, one minor">
</figure>

* **Issue 1:** Bootstrap's default secondary and muted text classes (`.text-secondary` and `.text-muted`) render in a light grey (`#6c757d`). When placed against white or off-white backgrounds, this output only achieves a contrast ratio of **4.68:1**. which fails the strict **WCAG 2.2 AAA enhanced contrast standard** which requires a minimum ratio of **7:1** for regular text body elements.
* **The Resolution:** A higher contrast colour (`#4d4d4d`) was added to the CSS to override the default colours within Bootstrap. This satisfies the **7:1** ratio requirement.


* **Issue 2:** The validator identified an "orphaned" layout segment. The charity donation callout section (`<section class="donation-banner">`) was added directly between`</header>` and `<main>` tags. Because this element sat completely exposed outside of a designated 'HTML5 structural landmark block', screen readers flagged it as a non-contained barrier.
* **The Resolution:** The structural nesting architecture inside `tracker/templates/tracker/index.html` was changed. The primary `<main>` landmark element was expanded upward to include the banner section.

Once these two issues were resolved the same scan was repeated, this time with no errors.
<figure>
    <img src="assets/accessible2.webp" width="500px"
         alt="Screenshot of a message saying there are no accessibility issues with the website. ">
</figure>

- - -
<br><br>

## MANUAL TESTING

### Testing User Stories

| Goals / User Stories | How are they achieved? | Status |
| :--- | :--- | :--- |
| **First Time Visitor:** I want to see a clean timeline of tributes and memories left by others without having to navigate a complicated website layout. | The application uses Bootstrap to create a clean, modern single-page layout. Django queries all records from the PostgreSQL database and passes them to the template via a context loop (`{% for tribute in tributes %}`). Tributes are displayed in a responsive, vertical grid that automatically handles content scaling across all desktop, tablet, and mobile breakpoints. | **PASSED** |
| **First Time Visitor:** I want to easily find and fill out a simple tribute form with my name, relationship and a personal memory without being forced to create an account. | Anyone is able to leave a tribute without having to sign up or create an account. The tribute input form sits prominently in the left-hand column on desktop layouts (and cascades directly below the header on mobile devices). Data validation is handled  by the browser (`required` fields) before processing secure `POST` database injections. | **PASSED** |
| **First Time Visitor:** I want to light a virtual candle alongside my message so that I can show my support. | The tribute form features a custom Bootstrap toggle switch element labeled "Light a virtual candle for Laurie". On submission, this passes a boolean `True` value to the database model's `light_candle` field. When rendered on the memorial wall feed, an active toggle conditionally displays a glowing candle (`🕯️`) within that specific tribute card view. | **PASSED** |
| **Returning Visitor:** I want to revisit the page and see an updated total counter of how many virtual candles have been lit, so that I can see the ongoing support from friends and family over time. | The header area features a dynamic badge displaying `{{candle_count}}`. The underlying Django view uses a database aggregation query (`MemorialPost.objects.filter(light_candle=True).count()`) to calculate the exact sum of all records where a candle was lit. This counter updates in real time upon page loads, allowing returning visitors to see ongoing support over time. | **PASSED** |
| **Returning Visitor:** I want to search for a specific tribute by a particular person, or a keyword so that I can read the story and share others memories. | A dedicated search bar is integrated directly above the memorial wall feed. It makes use of **HTMX text field interception**  as a user types. The backend filters records using case-insensitive complex `Q` objects on both the `author_name` and `tribute_text` fields, instantly isolating matching memories without the page needing to refresh. | **PASSED** |
| **Returning Visitor:** As a user who has already left a memory, I want to ensure that nobody else can accidentally edit or delete it from the front end. | The Memorial Wall layout is entirely read-only for database records. Data manipulation is absent from the frontend UI and is securely isolated behind Django's built-in `django.contrib.auth` authentication portal (`/admin`). The only people who will have the ability to edit or delete a memory are administrator accounts set up using the Django auth user tables. | **PASSED** |


- - -
<br>
<br>

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Lenovo Yoga 7i
* Mobile Devices:
  * Samsung S23 Pro
  * Pixel 9a
  * iPhone 14

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. 



### Manual Functional Testing


##### Tribute Form Submission & Data Validation

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Empty Required Name Field| Submission is blocked and a validation warning tooltip displays asking you to fill out the field. No database record is created.|1. Left "Your name" field entirely blank <br> 2. Populated the other fields. <br>3. Clicked "Share Memory" |The form did not submit. The tooltip highlighted the field saying "Please fill out this field" | PASS |
| Empty Required Message Field | Submission is blocked and a validation warning tooltip displays asking you to fill out the field. No database record is created. | 1. Left "Your Memory or Message" field entirely blank <br> 2. Populated the other fields. <br>3. Clicked "Share Memory"  | The form did not submit. The tooltip highlighted the field saying "Please fill out this field" | PASS  |
| Share a Memory Submission without candle | The form successfully submits using a `POST` method. The page reloads, the form is reset, the new tribute appears at the top of the wall. | 1. Populated all of the text fields <br> 2. Left "light a virtual candle" switch toggled off. <br>3. Clicked "Share Memory". | The page successfully reloaded and the form cleared. The new tribute card rendered instantly at the top of the timeleed feed WITHOUT a candle icon | PASS |
| Share a Memory Submission with candle | The form successfully submits using a `POST` method. The page reloads, the form is reset, the new tribute appears at the top of the wall. | 1. Populated all of the text fields <br> 2. Toggled "light a virtual candle" switch on. <br>3. Clicked "Share Memory". | The page successfully reloaded and the form cleared. The new tribute card rendered instantly at the top of the timeline feed WITH a candle icon. The total number of candles lit in the header section increased by 1. | PASS |


#### Search & Filtering the Memorial Wall

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| Keyword Filter - With result | HTMX intercepts typing and filters the timeline container down to matching rows instantly - without a page refresh. | 1. Located the search bar input<br>2. Typed "Michael" and pause typing | The HTMX successfully fired a request. The timeline container updated smoothly to isolate one matching record | PASS |
| Keyword Filter - Without result | HTMX intercepts typing and upon there being no matches it swaps the timeline with a custom empty-state fallback with the search criteria and a button to view all tributes. | 1. Located the search bar input<br>2. Typed "Jennie" and pause typing | The timeline container updated to display "No matching memories found. We couldn't find any memories matching "jennie". Try searching again." and displayed a button to "View All Memories" | PASS |
| View All Memories - Button Test | The "No matching memories found...." is replaced by the Memorial Wall tributes and the search bar is cleared. | Click the button | The page refreshed and the memorial wall with all of the tributes was displayed in full | PASS |
| Delete Search Criteria | As each character is deleted, the filtering updates to reflect the matching rows instantly, and when all characters are removed all entries are displayed in order. | 1. Type the word "post"<br> 2. Two posts are returned. <br>3.Delete the letters "T, S, O" <br> 4. Three posts are returned <br> 5. Delete the letter "P" <br> 6. All entries are now returned in order | Following the testing in order, the word POST returned two posts, The letter P returned three posts and with all characters deleted it returned all posts. | PASS |


#### 3. Family Admin Portal Access

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| Direct admin link access | If a user tries to directly access the `/admin/` server path link it will force a redirect back to the login portal (Assuming they are not already logged in)| 1. Ensure you are logged out of any active admin sessions <br> 2. Attempt to navigate directly to the path `https://web-production-721e.up.railway.app/admin/` | The direct URL redirects to the Django administrative login screen | PASS |
| Failed admin Sign-in Attempt| If the user enters an incorrect username/password they will be given an error message.| 1. Navigate to the Admin access link <br> 2. Type an invalid username / password (i.e. test / test) <br>3. Click "Log In" | Upon entering the username/password "test" the following error message was displayed *"Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."*| PASS |
| Successful admin Sign-in Attempt | Session succeeds. The dashboard opens, with site administration for the Memorial Posts. The footer on the main webpage updates to show active session with user name and direct links to "Manage and Delete Tributes" and "Log Out" | 1. Navigate to the Admin access link. <br> 2.Type a valid username/password <br> 3. click "Log In" <br> 4. Refresh the main memorial page to check the footer | Successfully logged into the admin dashboard. Refreshed the homepage to view the updated footer with controls | PASS |
| Admin: Update a record | Once a tribute has been modified the updates are saved inside the PostgreSQL database and instantly reflected on the Memorial Wall. | 1. Click on the words "Memorial Posts" from the main admin dashboard <br> 2. Click on the top post author_name = "Form Test" <br> 3. Change the author_name to "Doctor Who" <br> 4. Click "Save" | A confirmation message appeared within the admin dashboard to confirm that the updates have been saved. Refreshing the main webpage and navigate to the memorial wall, the top post now has the author name of "Doctor Who" | PASS |
| Admin: Delete a record | Once a tribute has been deleted, the record row is permanently dropped from the database table. The Memorial wall feed will update to reflect the tribute being deleted. | 1. Click on the words "Memorial Posts" from the main admin dashboard. <br> 2. Click on the top post author_name = "Doctor Who" <br> 3. Click the red "Delete" button <br> 4. A warning will appear asking you if you are sure you want to delete the post <br> 5. Click "Yes, I'm sure"| A confirmation message appeared within the main admin dashboard to confirm the post was deleted successfully. Refreshing the main webpage and navigating to the memorial wall shows that the top post is now deleted | PASS |



####  Links

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| Donation Website Link | The link target opens in an external tab without closing the memorial page tab. | 1. Scroll down to the charity support banner section.<br>2. Click on the "Donate via Givewheel" button link. | The Givewheel portal successfully opened in a completely separate browser tab. | **PASS** |