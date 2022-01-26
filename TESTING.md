# Testing Documentation

[Return to Readme.md](https://github.com/CristianBuca/MS3_TopShelf/blob/main/README.md)

Link to Live Site can be found [HERE](https://ms3-top-shelf.herokuapp.com/)


## HTML Validation

### HTML validation was carried out with [W3 Validator](https://validator.w3.org).

_The same 2 warnings are present on all pages dues to missing headings on sections._

<details>
  <summary> (expand) Landing Page HTML Validation found 0 errors:</summary>

![Landing Page HTML Validation](/docs/test_img/html_validator/html_valid_landing.png)
</details>

<details>
  <summary> (expand) Login Page HTML Validation found 0 errors:</summary>

![Login Page HTML Validation](/docs/test_img/html_validator/html_valid_login.png)
</details>

<details>
  <summary> (expand) Registration Page HTML Validation found 0 errors:</summary>

![Registration Page HTML Validation](/docs/test_img/html_validator/html_valid_register.png)
</details>

<details>
  <summary> (expand) My Shelf Page HTML Validation found 0 errors:</summary>

![My Shelf Page HTML Validation](/docs/test_img/html_validator/html_valid_myshelf.png)
</details>

<details>
  <summary> (expand) Add to Shelf Page HTML Validation found 0 errors:</summary>

![Add to Shelf Page HTML Validation](/docs/test_img/html_validator/html_valid_addtoshelf.png)
</details>

<details>
  <summary> (expand) Profile Page HTML Validation found 0 errors:</summary>

![Profile Page HTML Validation](/docs/test_img/html_validator/html_valid_profile.png)
</details>

<details>
  <summary> (expand) Superuser Page HTML Validation found 0 errors:</summary>

![Superuser Page HTML Validation](/docs/test_img/html_validator/html_valid_superuser.png)
</details>

<details>
  <summary> (expand) Change Stock Page HTML Validation found 0 errors:</summary>

![Change Stock Page HTML Validation](/docs/test_img/html_validator/html_valid_changestock.png)
</details>


[Back to Top](#Testing-Documentation)

### CSS validation was carried out with [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

<details>
  <summary> (expand) css.style Jigsaw Validation found 0 errors:</summary>

![CSS Validation](/docs/test_img/css_validator/css_valid.png)
</details>





### Performance Tests were carried out using Chrome Lighthouse DevTools.

<details>
  <summary> (expand) Home Page Lighthouse Test:</summary>

![Home Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_index.PNG)
</details>

<details>
  <summary> (expand) Quiz Page Lighthouse Test:</summary>

![Quiz Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_quiz.PNG)
</details>

<details>
  <summary> (expand) Portfolio Page Lighthouse Test:</summary>

![Portfolio Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_portfolio.PNG)
</details>

<details>
  <summary> (expand) 404 Page Lighthouse Test:</summary>

![404 Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_404.PNG)
</details>

### JavaScript Code Tests were carried out with [JShint](https://jshint.com).

JSHint warnings are due to the use of shorthand for IF statements and the use of JQuery where JSHint interprets "$" as an unknown variable.

<details>
  <summary> (expand) email.js JSHint found 0 errors:</summary>

![EmailJS script](/docs/test_img/jshint_validator/jshint_valid_email.png)
</details>

<details>
  <summary> (expand) home.js JSHint found 0 errors 1 warning:</summary>

![EmailJS script](/docs/test_img/jshint_validator/jshint_valid_home.png)
</details>

<details>
  <summary> (expand) quiz.js JSHint found 0 errors 1 warning:</summary>

![EmailJS script](/docs/test_img/jshint_validator/jshint_valid_quiz.png)
</details>

<details>
  <summary> (expand) quiz_data.js JSHint found 0 errors:</summary>

![EmailJS script](/docs/test_img/jshint_validator/jshint_valid_quiz_data.png)
</details>

<details>
  <summary> (expand) portfolio.js JSHint found 0 errors, 3 warnings:</summary>

![EmailJS script](/docs/test_img/jshint_validator/jshint_valid_portfolio.png)
</details>


### Devices used for physical testing: 

* Samsung Galaxy S8,
* Samsung Tab A 9.7-inch tablet,
* 17-inch 1080p Laptop (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers),
* 24-inch 1080p Display (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers),
* 32-inch 2040p Display (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers).

Application performs as intended on all devices.

## **Testing of User Stories**

_GitHub does not allow videos hosted in the local repository to be played on the repository page.
Although when viewing on GitHub these videos appear fine, they might not be available in this format if this project is forked. Please refer to the Local Links if needed._


### 1. As a new user, I want to see recent data on major crypto-currencies by market capitalization.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Coin Badges on Landing Page | Load Landing Page. Hover over individual badges. | View current price for each currency. View 24 hour price highs and lows. | Works as expected |

<details>
  <summary> (Expand - User Story 1 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140587509-0f297a4c-b235-48f1-add7-e797432f4f5a.mp4

  [Local Link](docs/test_user_stories/user_story_1_test.mp4)
</details>

### 2. As a new user, I want to add personal crypto-currency assets.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Portfolio Page | Click the "Portfolio" Link in navbar. Click on Asset Input Field. Input symbol, name or select from list the asset. Click on "Enter amount" Input Field. Enter amount. Click "Add" button. | See the asset added to the table. | Works as expected |

<details>
  <summary> (Expand - User Story 2 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140587736-5d87a52a-8c8d-4aab-a639-995638890542.mp4

  [Local Link](docs/test_user_stories/user_story_2_test.mp4)
</details>

### 3. As a new user, I want to see the asset valuation.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Asset table on Portfolio Page | Assets added as described in User Story 2 are stored in Local Storage. Refresh Page, view table containing assets. | View current price and valuation for each asset added. | Works as expected |

<details>
  <summary> (Expand - User Story 3 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140587959-09b0f953-1d3e-4860-af74-68dfcda3cd13.mp4

  [Local Link](docs/test_user_stories/user_story_3_test.mp4)
</details>

### 4. As a new user, I want to see the total portfolio valuation.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Current Portfolio Value section at the top of Portfolio Page | Refresh Page. View total portfolio valuation. | See the total valuation of all assets. | Works as expected.

<details>
  <summary> (Expand - User Story 4 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588272-5daa2760-1f20-4c34-95ac-5e3d054a532b.mp4

  [Local Link](docs/test_user_stories/user_story_4_test.mp4)
</details>

### 5. As a new user, I want to learn new information relating to the blockchain.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Quiz Page | Click the Quiz Link on the navigation bar. Click the start button on the quiz. Play the game. | Find information related to the blockchain. | Works as expected |

<details>
  <summary> (Expand - User Story 5 testing video) </summary>
 
  https://user-images.githubusercontent.com/79543676/140588329-9636efce-2a13-4e88-9e22-93e0315f6c33.mp4

  [Local Link](docs/test_user_stories/user_story_5_test.mp4)
</details>

### 6. As a new user, I want to learn more about the knowledge quiz.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Quiz info button in the quiz title | Click on the information button. | See modal with information about the quiz. | Works as expected |

<details>
  <summary> (Expand - User Story 6 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588369-5b27cec6-1fd5-4d6e-a3d4-1142d739b90c.mp4

  [Local Link](docs/test_user_stories/user_story_6_test.mp4)
</details>

### 7. As a regular user, I want to store my portfolio data.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Add asset section on portfolio page | Click on portfolio link in navigation bar. Add asset as described in User Story 2. Close page / browser. Open page again. | To see added assets persist through different browsing session. See added data stored in Local Storage | Works as expected |

<details>
  <summary> (Expand - User Story 7 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588411-7e35764d-4540-418d-bdbb-b4aca894e4d0.mp4

  [Local Link](docs/test_user_stories/user_story_7_test.mp4)
</details>

### 8. As a regular user, I want the option to change the current webapp color theme.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Theme Switch in the Navbar | Click the theme switch in the Navbar | Page color scheme to change | Works as expected |

<details>
  <summary> (Expand - User Story 8 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588507-401f9bdd-999f-4bcf-8af4-13aa38fea442.mp4

  [Local Link](docs/test_user_stories/user_story_8_test.mp4)
</details>

### 9. As a regular user, I want the ability to edit previous portfolio entries.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Portfolio Page input fields and trash bin icons | To change the Holding amount of an existing asset, select the same asset in the dropdown menu and input new amount. To remove asset from table click the trash bin icon in the asset's table row. | Updated amount to show in table when updating. Asset to be removed when clicking trash bin. | Works as expected |

<details>
  <summary> (Expand - User Story 9 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588553-39bdb347-bf92-49c2-a5ac-56e3c12a9d17.mp4

  [Local Link](docs/test_user_stories/user_story_9_test.mp4)
</details>

### 10. As a regular user, I want to test the previously acquired knowledge.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| End screen on quiz game | Click on try again button at the end of the quiz | The quiz game starts over and offers the chance to gain a better score and better completion time | Works as expected |

<details>
  <summary> (Expand - User Story 10 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588603-f212437f-b608-4cd6-b7b4-f3445ee00d1e.mp4

  [Local Link](docs/test_user_stories/user_story_10_test.mp4)
</details>

### 11. As a site owner, I want the knowledge quiz to be versatile and easy to update.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| quiz_data.js script housing all the questions and answers for the quiz | Open project repository. Locate quiz_data.js in assets/js/. Open quiz_data.js and replace questions and answers. The quiz data is displayed dynamically thus making it easy for variable number of answers to be displayed for one question and not being hard coded in HTML to a specific number. | View new questions being displayed in the quiz. | Works as expected |

<details>
  <summary> (Expand - User Story 11 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588644-1648d384-a124-4d29-a357-085bc7a9844f.mp4

  [Local Link](docs/test_user_stories/user_story_11_test.mp4)
</details>

### 12. As a site owner, I want to provide the user a way to get in contact.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Email modal that uses EmailJS API | Click on "Get in touch" Link in the Navbar. Fill in the input fields. Click Send | Validation when the API sends the message to the site owners inbox. | Works as expected |

<details>
  <summary> (Expand - User Story 12 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588680-4250c1ec-af3e-48f5-8bfa-d4512ff0b61d.mp4

  [Local Link](docs/test_user_stories/user_story_12_test.mp4)
</details>

### 13. As a site owner, I want to showcase my social media.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Social media links in the page footer | Click on the social media icons in the page footer | Social media pages to open in new tab. | Works as expected |

<details>
  <summary> (Expand - User Story 13 testing video) </summary>

  https://user-images.githubusercontent.com/79543676/140588734-cf40597a-d084-48f9-8e8f-e13823850f84.mp4

  [Local Link](docs/test_user_stories/user_story_13_test.mp4)
</details>


## **Bugs**


