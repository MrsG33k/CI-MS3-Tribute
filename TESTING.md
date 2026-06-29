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
    <img src="assets/lighthouseimage.webp"
         alt="A screenshot of the warning of the image size on chrome dev tools">
</figure>

To resolve the issue I opened the image back into Photopea and reduced the whole image size before exporting once again as a .webp file at reduced size and dimensions. 

* **Accessibility Issues:** Bringing down this score was a contrast issue on the font on the badge displaying the relationship on the memorial wall. It was using Bootstraps text-secondary, which is a muted grey. I changed it to text-secondary - A darker colour. Below is the before and after of the colour contrast

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
    <img src="assets/accessible1.webp"
         alt="Screenshot of 2 warnings with the accessibility, one moderate, one minor">
</figure>

* **Issue 1:** Bootstrap's default secondary and muted text classes (`.text-secondary` and `.text-muted`) render in a light grey (`#6c757d`). When placed against white or off-white backgrounds, this output only achieves a contrast ratio of **4.68:1**. which fails the strict **WCAG 2.2 AAA enhanced contrast standard** which demands a minimum ratio of **7:1** for regular text body elements.
* **The Resolution:** A higher contrast colour (`#4d4d4d`) was added to the CSS to override the default colours for Bootstrap. This satisfies the **7:1** ratio. 


* **Issue 2:** The validator identified an "orphaned" layout segment. The charity donation callout section (`<section class="donation-banner">`) was added directly between`</header>` and `<main>` tags. Because this element sat completely exposed outside of a designated 'HTML5 structural landmark block', screen readers flagged it as a non-contained barrier.
* **The Resolution:** The structural nesting architecture inside `tracker/templates/tracker/index.html` was changed. The primary `<main>` landmark element was expanded upward to encapsulate the banner section completely.

Once these two issues were resolved the same scan was repeated, this time with no errors.
<figure>
    <img src="assets/accessible2.webp"
         alt="Screenshot of a message saying there are no accessibility issues with the website. ">
</figure>

- - -

## MANUAL TESTING

### Testing User Stories

`First Time Visitors`

| Goals | How are they achieved? |
| :--- | :--- |
| As a First Time Visitor, I want to see a clear 'How to Play' guide when the page loads so that I can understand the game mechanics before starting my first round. | On landing on the webpage the user is presented with a "How to Play" button which displays instructions for playing the game. |
| As a First Time Visitor, I want to be able to easily identify the guess map and the 'Submit' button so that I can play the game without confusion | The map is the focal point of game.html taking up 2/3 of the space. The submit button is a large button that is visible to users on desktop and mobile.|
| As a First Time Visitor accessing the site on my phone, I want the interface to stack vertically so that all the interactive elements remain accessible and nothing is obscured. | All elements stack on mobile, with the map being on top, followed by the location image and then the submit button. The header also reduces in size to maximise the element display. |


`Returning Visitors`

|  Goals | How are they achieved? |
| :--- | :--- |
| As a Returning Visitor, I want a 'Play again' button that resets the game state and picks a new random location. | Once a user has completed the game they are presented with the option to start a new game |
| As a Returning Visitor, I want the game to feel different each time, by providing a range of different locations for me to guess the location of. | There are 5 rounds per game, and 10 locations in total. The game will prevent the same location being chosen twice. Future developments will add to the number of locations. |
| As a Returning Visitor, I want a 'Play again' button that resets the game state and picks a new random location. | Once a user has completed the game they are presented with the option to start a new game |
| As a Returning Visitor, I want the game to remember my "Theme" settings so that the app feels personalised to me every time I return.  | This part wasn't achieved in the project. I wanted to include a dark/light mode toggle, but I ended up moving this to future developments instead.  |


- - -

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

One issue that was identified was that the how to play modal pop up didn't always scroll when on mobile view. I did recreate this issue and fixed by changing the modal overflow and overscroll in CSS.

<figure>
    <img src="assets/images/howtomodalscroll.gif"
         alt="gif showing the modal not scrolling on mobile" width="250">
</figure>


#### Home.html

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Sites title /logo | Link directs the user back to the home page | Clicked title | Home page reloads | Pass |
| How to play button | Displays the modal with the instructions on how to play the game | Clicked on button | Modal with instructions on how to play opens | Pass |
| Modal close button | Closes the modal | Clicked on close button | Modal closed | Pass |
| Start Adventure | Directs the user to the game page | Clicked on button | Game page opens to display the difficulty selections | Pass |
| All buttons - hover effect | All blue buttons with white text should change to gold buttons with black text on hover | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |


#### Game.html

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Sites title / logo | Link directs the user back to the home page | Clicked title | Directed back to home page | Pass |
| All buttons - hover effect | All blue buttons with white text should change to gold buttons with black text on hover | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |
| Hint Button | Displays the modal with the hint for the location | Clicked on button | Modal with instructions on how to play opens | Pass |
| Modal close button | Closes the modal | Clicked on close button | Modal closed | Pass |
| Map loading | Map loads with Bad Wolf Studios as the location | loaded the game page | Map loaded with Bad Wolf Studios as the location | Pass |
| Submit Button pre marker | Displays the modal explaining you can't submit before placing a marker | Click submit before placing a marker | Modal with instructions opens | Pass |
| Submit Button post marker | Display a modal with the location name, distance from the location and the score | Click submit after placing a marker | Modal with results opens | Pass |
| Score | Score increments after each round | Playing at least one round | Score updated from 0 to the score gained | Pass |
| Round | Round increments from 0 of 5 to 1 of 5 until it reaches 5 | Playing at least one round | Round updated from 0 of 5 to 1 of 5 | Pass |



#### Game.html - End of game

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| End of Round 5 modal | After round 5 the modal should give you a total score and button to play another game | Completed 5 rounds | Modal opened with total score and button to play another game | Pass |
| New Game 'Play Again?' | On clicking 'Play Again?' the score / rounds should reset and map go back to default state | Play 5 rounds and click 'Play Again?' at end | Game reset score to 0, rounds to 0 and map reset | Pass |
| New Game 'Exit to Menu' | On clicking 'Exit to Menu' the player is taken back to index.html | Play 5 rounds and click 'Exit to Menu' at end | index.html loads | Pass |

 


#### 404 Error Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Sites title / logo | Link directs the user back to the home page | Clicked title | Directed back to home page | Pass |
| All buttons - hover effect | All blue buttons with white text should change to gold buttons with black text on hover | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |
| Hover on image - Desktop| The image rotates and glows | Hovered on image | Image rotated and glowed | Pass |
| Return Home button | Takes the player to index.html | Clicked on button | index.html loaded | Pass |