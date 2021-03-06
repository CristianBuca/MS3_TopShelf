# Testing Documentation

![Top Shelf Scotch](/docs/design/logos.png)

![Responsive Design](/docs/responsive_design/responsive_design.jpg)

# Table of contents

- **[HTML Validation](#html-validation)**
- **[CSS Validation](#css-validation)**
- **[Accessibility Validation](#accessibility-validation)**
- **[Lighthouse Tests](#lighthouse-tests)**
- **[Javascript Validation](#javascript-validation)**
- **[Python Validation](#python-validation)**
- **[Physical Testing](#physical-testing)**
- **[Testing of User Stories](#testing-of-user-stories)**
  * [New User Stories](#new-user-stories)
  * [Regular User Stories](#regular-user-stories)
  * [Superuser Stories](#superuser-stories)
  * [Site Owner Stories](#site-owner-stories)

- **[Bugs](#bugs)**

## **[Return to Readme.md](/README.md)**

## **You can find the deployed website** [**HERE**](https://ms3-top-shelf.herokuapp.com/)

# HTML Validation

## HTML validation was carried out with [W3 Validator](https://validator.w3.org).

_The same 2 warnings are present on all pages dues to missing headings on sections._

<details>
  <summary> (expand) Landing Page HTML Validation found 0 errors:</summary>

![Landing Page HTML Validation](/docs/test_img/html_validator/html_valid_landing.png)
</details>

<details>
  <summary> (expand) Login Page HTML Validation found 1 false error due to wtForms handling the form's action on the backend::</summary>

![Login Page HTML Validation](/docs/test_img/html_validator/html_valid_login.png)
</details>

<details>
  <summary> (expand) Registration Page HTML Validation found 1 false error due to wtForms handling the form's action on the backend:</summary>

![Registration Page HTML Validation](/docs/test_img/html_validator/html_valid_register.png)
</details>

<details>
  <summary> (expand) My Shelf Page HTML Validation found 0 errors:</summary>

![My Shelf Page HTML Validation](/docs/test_img/html_validator/html_valid_myshelf.png)
</details>

<details>
  <summary> (expand) Add to Shelf Page HTML Validation found 1 false error due to wtForms handling the form's action on the backend:</summary>

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

# CSS Validation

## CSS validation was carried out with [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

<details>
  <summary> (expand) css.style Jigsaw Validation found 0 errors:</summary>

![CSS Validation](/docs/test_img/css_validator/css_valid.png)
</details>

# Accessibility Validation

## Accessibility Evaluation was carried out with [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org).

<details>
  <summary> (expand) Landing Page WAVE Validation found 0 errors:</summary>

![Landing Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_landing.png)
</details>

<details>
  <summary> (expand) Login Page WAVE Validation found 0 errors:</summary>

![Login Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_login.png)
</details>

<details>
  <summary> (expand) Registration Page WAVE Validation found 0 errors:</summary>

![Registration Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_register.png)
</details>

<details>
  <summary> (expand) My Shelf Page WAVE Validation found 0 errors:</summary>

![My Shelf Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_myshelf.png)
</details>

<details>
  <summary> (expand) Add to Shelf Page WAVE Validation found 0 errors:</summary>

![Add to Shelf Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_addtoshelf.png)
</details>

<details>
  <summary> (expand) Profile Page WAVE Validation found 0 errors:</summary>

![Profile Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_profile.png)
</details>

<details>
  <summary> (expand) Superuser Page WAVE Validation found 0 errors:</summary>

![Superuser Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_superuser.png)
</details>

<details>
  <summary> (expand) Change Stock Page WAVE Validation found 0 errors:</summary>

![Change Stock Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_changestock.png)
</details>

[Back to Top](#testing-documentation)

# Lighthouse Tests

## Performance Tests were carried out using Chrome Lighthouse DevTools.

<details>
  <summary> (expand) Landing Page Lighthouse Test:</summary>

![Landing Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_landing.jpg)
</details>

<details>
  <summary> (expand) Login Page Lighthouse Test:</summary>

![Login Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_login.jpg)
</details>

<details>
  <summary> (expand) Registration Page Lighthouse Test:</summary>

![Registration Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_register.jpg)
</details>

<details>
  <summary> (expand) My Shelf Page Lighthouse Test:</summary>

![My Shelf Lighthouse Test](/docs/test_img/lighthouse/lighthouse_myshelf.jpg)
</details>

<details>
  <summary> (expand) Add to Shelf Page Lighthouse Test:</summary>

![Add to Shelf Lighthouse Test](/docs/test_img/lighthouse/lighthouse_addtoshelf.jpg)
</details>

<details>
  <summary> (expand) Profile Page Lighthouse Test:</summary>

![Profile Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_profile.jpg)
</details>

<details>
  <summary> (expand) Superuser Page Lighthouse Test:</summary>

![Superuser Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_superuser.jpg)
</details>

<details>
  <summary> (expand) Change Stock Page Lighthouse Test:</summary>

![Change Stock Page Lighthouse Test](/docs/test_img/lighthouse/lighthouse_changeitem.jpg)
</details>

# Javascript Validation

## JavaScript Code Tests were carried out with [JShint](https://jshint.com).


<details>
  <summary> (expand) script.js JSHint found 0 errors:</summary>

![script.js JSHint Test](/docs/test_img/jshint_validator/jshint_valid_script.png)
</details>

<details>
  <summary> (expand) form_validation.js JSHint found 0 errors:</summary>

![form_validation.js JSHint Test](/docs/test_img/jshint_validator/jshint_valid_form.png)
</details>

# Python Validation

## Python Code Tests were carried out with [Pep8](http://pep8online.com)

<details>
  <summary> (expand) app.py Pep8 found 0 errors:</summary>

![app.py Pep8 Test](/docs/test_img/pep8_valid/pep8_valid_app.png)
</details>

<details>
  <summary> (expand) forms.py Pep8 found 0 errors:</summary>

![forms.py Pep8 Test](/docs/test_img/pep8_valid/pep8_valid_forms.png)
</details>

# Physical Testing

## Devices used for physical testing: 

* Samsung Galaxy S8,
* Samsung Tab A 9.7-inch tablet,
* 17-inch 1080p Laptop (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers),
* 24-inch 1080p Display (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers),
* 32-inch 2040p Display (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers).

Application performs as intended on all devices.


[Back to Top](#testing-documentation)


# Testing of User Stories

_GitHub does not allow videos hosted in the local repository to be played on the repository page.
Although when viewing on GitHub these videos appear fine, they might not be available in this format if this project is forked. Please refer to the Local Links if needed._

## New User Stories

### 1. As a new user, I want to be able to register an account

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Registration Page | Click "Register" link on the Navbar. Fill in the registration form. Click Submit. | Account stored in database and access to user-only features on the app | Works as expected |

<details>
  <summary> (Expand - User Story 1 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678124-6ae25e80-094c-42aa-9ebe-5fea8ea67ef1.mp4


  [Local Link](/docs/test_user_stories/user_story_1.mp4)
</details>

### 2. As a new user, I want to be able to login and access my account.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Login Page | Click "Login" link on the Navbar. Fill in the login form with own credentials. Click Submit. | Gain access to previously registered account on app | Works as expected |

<details>
  <summary> (Expand - User Story 2 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678143-97c831d9-09f2-43b3-8506-b0a8b000d0eb.mp4


  [Local Link](/docs/test_user_stories/user_story_2.mp4)
</details>

### 3. As a new user, I want to be able to logout.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Logout button in the expanded Floating Action Button | Hover over the Floating Action Button at the bottom right-hand corner of the page. Click the Logout button. | Being logged out of the app | Works as expected |

<details>
  <summary> (Expand - User Story 3 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678147-47baefb6-7a5b-49a5-bce9-928dee459ed5.mp4


  [Local Link](/docs/test_user_stories/user_story_3.mp4)
</details>

### 4. As a new user, I want to view collections in the database.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Landing Page | Click the Logo or "All Shelves" button on the navbar | To view entries from other user's collections | Works as expected |

<details>
  <summary> (Expand - User Story 4 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678153-666f1ae8-17b3-4e02-85a0-437893a3f2f9.mp4


  [Local Link](/docs/test_user_stories/user_story_4.mp4)
</details>

### 5. As a new user, I want to be able to search in the database.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Search bar at the top of the Landing Page | Click the Search Field at the top of the Landing Page. Enter the name of the item, region or distillery you are trying to find. Click Search | For all entries in the database containing my search parameters to be filtered and displayed | Works as expected |

<details>
  <summary> (Expand - User Story 5 testing video) </summary>
 

https://user-images.githubusercontent.com/79543676/151678156-a8098480-7669-4b5c-a929-6b0f1c317946.mp4


  [Local Link](/docs/test_user_stories/user_story_5.mp4)
</details>

### 6. As a new user, I want to be able to add my own items to the database.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Add to Shelf Page | Click the "Add to Shelf" link in the navbar. Fill in the form. Submit the form. | Fot the entry to be created in the database and be displayed in personal and public collection | Works as expected |

<details>
  <summary> (Expand - User Story 6 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678158-eca06797-1e84-42f7-896c-7cb3803fe007.mp4


  [Local Link](/docs/test_user_stories/user_story_6.mp4)
</details>

### 7. As a new user, I want to be able to view my collection in the database.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| My Shelf Page | Click the "My Shelf" link in the navbar. View collection in the drop-down card collection. Click on each item to view individually | To view personal collection in the database | Works as expected |

<details>
  <summary> (Expand - User Story 7 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678163-cdf90185-6d6a-4b37-bf01-581374583dd8.mp4


  [Local Link]/docs/test_user_stories/user_story_7.mp4)
</details>

[Back to Top](#testing-documentation)

## Regular User Stories

### 8. As a regular user, I want to be able to edit entries in my collection.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Change Stock Page | Click the "My Shelf" link in the navbar. Select the item to be updated from the drop-down collection. Click the "Change" button. Update the field in the form | For the entry to be updated in the databse and displayed accordingly | Works as expected |

<details>
  <summary> (Expand - User Story 8 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678168-00953c5d-38fc-4986-a01c-030ec9624ff5.mp4


  [Local Link](/docs/test_user_stories/user_story_8.mp4)
</details>

### 9. As a regular user, I want to be able to delete entries in my collection.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| My Shelf Page | Click the "My Shelf" link in the navbar. Select the item to be updated from the drop-down collection. Click the "Remove from Shelf" button. Confirm removal in the pop-up | For the item to be deleted from the database and from personal and public collections | Works as expected |

<details>
  <summary> (Expand - User Story 9 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678170-d6fd3376-6de1-430f-a666-422c7332dbc2.mp4


  [Local Link](/docs/test_user_stories/user_story_9.mp4)
</details>

### 10. As a regular user, I want to be able to change my password.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Profile Page | Click the "Profile" link in the navbar. Fill in the form with new password and new password confirmation. Submit the form | For password associated with account in the database to be updated | Woks as expected |

<details>
  <summary> (Expand - User Story 10 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678174-c2b39c57-405f-4060-b0e0-38f1e7679e0d.mp4


  [Local Link](/docs/test_user_stories/user_story_10.mp4)
</details>

### 11. As a regular user, I want to be able to change my avatar.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Profile Page | Click the "Profile" link in the navbar. Update the avatar link in the form along with password and confirmation. Submit the form. Refresh page to view new avatar | For the avatar associated with account to be updated | Works as expected |

<details>
  <summary> (Expand - User Story 11 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678181-658a472c-0e8c-46df-ba55-e4c4550f33c2.mp4


  [Local Link](/docs/test_user_stories/user_story_11.mp4)
</details>

[Back to Top](#testing-documentation)

## Superuser Stories

### 12. As a superuser, I want to be able to search the database for users and entries.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Superuser Page | Click on "Profile" link in the navbar. Click on the green Floating Action Button at the bottom right hand corner of the page. Access Superuser Page and click the search field at the top of the page. Input username or item. | To view the results of my search filtered from the database and displayed on the page | Works as expected |

<details>
  <summary> (Expand - User Story 12 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678188-38ad8e33-5809-4c72-af64-5b6df85929c7.mp4


  [Local Link](/docs/test_user_stories/user_story_12.mp4)
</details>

### 13. As a superuser, I want to be able to remove users from the database.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Superuser Page | Click on "Profile" link in the navbar. Click on the green Floating Action Button at the bottom right hand corner of the page. Access Superuser Page and click "Remove User" button present next to each user in the database. Confirm Removal from the pop-up modal | For the selected user to be removed from the database | Works as expected |

<details>
  <summary> (Expand - User Story 13 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678193-c087a708-5ff8-420e-94f2-0d71fe2e1463.mp4


  [Local Link](/docs/test_user_stories/user_story_13.mp4)
</details>

### 14. As a superuser, I want to be able to remove user created entries from the database.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Superuser Page | Click on "Profile" link in the navbar. Click on the green Floating Action Button at the bottom right hand corner of the page. Access Superuser Page and click "Remove from Shelf" button present next to each item in the database. Confirm Removal from the pop-up modal | For the selected item to be removed from the database | Works as expected |

<details>
  <summary> (Expand - User Story 14 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678198-71ccac72-deff-4ac6-84e0-1fcfb00bb306.mp4


  [Local Link](/docs/test_user_stories/user_story_14.mp4)
</details>

[Back to Top](#testing-documentation)

## Site Owner Stories

### 15. As a site owner, I want the app to be responsive.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Materialize Grid layout and collapsible navbar | Change the width of the browser window. | For the page to adapt to different width sizes and navbar to collapse/expand | Works as expected |

<details>
  <summary> (Expand - User Story 15 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678201-a2401cbd-adcd-44f2-a6a3-f529b27ebc13.mp4


  [Local Link](/docs/test_user_stories/user_story_15.mp4)
</details>

### 16. As a site owner, I want to have users with admin privileges.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Superuser status in the database | As a database admin change the "superuser" field in the user collection to TRUE | For the selected user to be able to access the superuser page | Works as expected |

<details>
  <summary> (Expand - User Story 16 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678206-05bcfa91-89d9-4283-997d-11e1961956e2.mp4


  [Local Link](/docs/test_user_stories/user_story_16.mp4)
</details>

### 17. As a site owner, I want to showcase my social media.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Page Footer | Navigate to the bottom of any page. Click on the social media links | For the links to take me to the respective social media sites | Works as expected |

<details>
  <summary> (Expand - User Story 17 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678208-70c8d63a-5d7e-4fcb-b9fc-111b5d384f1c.mp4


  [Local Link](/docs/test_user_stories/user_story_17.mp4)
</details>

### 18. As a site owner, I want to provide feedback to the user when errors occur.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Flash message section below the navbar | Perform any database CRUD operations, try to register with user/email already in the database, try to login with wrong credentials. | To see a flash message describing the success/failure of the operation | Works as expected |

<details>
  <summary> (Expand - User Story 18 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678219-1c14bd6b-5607-4bc5-972b-968fdb921184.mp4


  [Local Link](/docs/test_user_stories/user_story_18.mp4)
</details>

### 19. As a site owner, I want forms to be validated on the client side.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| JQuery form validation | Fill in the input fields on forms | To see feedback when input does not match the required criteria | Works as expected |

<details>
  <summary> (Expand - User Story 19 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678226-7ca5a696-11d2-4854-a2c0-31aed34e0eb7.mp4


  [Local Link](/docs/test_user_stories/user_story_19.mp4)
</details>

### 20. As a site owner, I want forms to be validated on the backend.

|Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| wtForms validation in python | Fill in the input fields on the forms | To see feedback when input does not validate | Works as expected |

<details>
  <summary> (Expand - User Story 20 testing video) </summary>


https://user-images.githubusercontent.com/79543676/151678228-d0f6ffff-2a99-4a8f-9238-38e78441c6df.mp4


  [Local Link](/docs/test_user_stories/user_story_20.mp4)
</details>

[Back to Top](#testing-documentation)

# Bugs

**Bug 1**: 

```
pymongo.errors.ServerSelectionTimeoutError: myfirstcluster-shard-00-01.leode.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129),myfirstcluster-shard-00-02.leode.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129),myfirstcluster-shard-00-00.leode.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129), Timeout: 30s, Topology Description: <TopologyDescription id: 61ccc65dc46da4714b1e084e, topology_type: ReplicaSetNoPrimary, servers: [<ServerDescription ('myfirstcluster-shard-00-00.leode.mongodb.net', 
27017) server_type: Unknown, rtt: None, error=AutoReconnect('myfirstcluster-shard-00-00.leode.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)')>, <ServerDescription ('myfirstcluster-shard-00-01.leode.mongodb.net', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('myfirstcluster-shard-00-01.leode.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)')>, <ServerDescription ('myfirstcluster-shard-00-02.leode.mongodb.net', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('myfirstcluster-shard-00-02.leode.mongodb.net:27017: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)')>]>

```

**Try**: Code Institute Tutor came across a thread stating that pyMongo and Python v10 might throw SSL certificate errors. Suggested installing virtual environments and trying different versions of Python. Unfortunately that did not solve the issue but did help with overall development process.

**Fix**: Found the solution [HERE](https://www.mongodb.com/community/forums/t/keep-getting-serverselectiontimeouterror/126190/12). I needed to download new certificates for Windows.

**Bug 2**: Cookie Key Error when running this route

```python
@app.route("/profile/<username>", methods=["GET", "POST"])
	def profile(username):
	    #grab the session user's username from db
	    username = mongo.db.users.find_one(
	        {"username": session["user"]})["username"]
	    
	    if session["user"]:
	        return render_template("profile.html", username=username)
	

	    return redirect(url_for("login"))
```
**Fix**: 

```python
if session.get('user') is not None:
```

**Bug 3**: Confirmation modal for removal of items from database removes first item on list and not item that activates the modal.

**Fix**: Change modal id and the data target that calls the modal to be dynamic based on item ID.

```html
<button data-target="remove-{{ item._id }}" class="btn modal-trigger">Remove from Shelf</button>
<div id="remove-{{ item._id }}" class="modal">
```

**Problem:** 

Images for items or user avatars are entered by the user in the form of external links. If external link is broken or user decides to enter a random string instead of functional link, I wanted to replace the missing image with a default image for display purposes.

**Try:**

```javascript
$('img').on('error', function() {
    $(this).attr('src', '/static/images/avatar_default.jpg');
})
```

Unfortunately this would not trigger 100% of the time. It behaved differently on different browsers but most of the time it would only work after a page refresh.

**Solution:**

Use Ajax to check if there is a 404 status on each <img> field and replace the source:

```javascript
$("img").each( function () 
{
    var _this = $(this);
    
    $.ajax({
        url:$(this).attr('src'),
        type:'HEAD',
        async: false,
        error:
            function(e)
            {
                if (e.status == '404') {
                    $(_this).attr('src', '/static/images/avatar_default.jpg');
                }
            }
    });
});
```
[Back to Top](#testing-documentation)
