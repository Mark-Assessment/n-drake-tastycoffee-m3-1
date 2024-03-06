# Tasty Coffee

This is the **TEST.md** file for a comprehensive resource for coffee enthusiasts, aficionados, and anyone curious about the world of coffee beans.

You can view the **LIVE website** through the following two links:

[GitHub](https://github.com/OrgNateDrake/milestone-project-3)<br>
[Heroku](https://milestone-3-project-29f9ad62c493.herokuapp.com)

A snapshot of the project with responsive design:

[I Am Responsive](https://ui.dev/amiresponsive?url=https://milestone-3-project-29f9ad62c493.herokuapp.com)

![I Am Responsive](/images/am-i-responsive.jpeg)


## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Deployment](#deployment)
- [Testing](#testing)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
    - [Manual Testing Completed](#manual-testing-completed)
    - [Manual Tests for Tasty Coffee Website](#manual-tests-for-tasty-coffee-website)
    - [Test Case 1: User Registration](#test-case-1-user-registration)
    - [Test Case 2: User Login](#test-case-2-user-login)
    - [Test Case 3: Adding a Coffee Profile](#test-case-3-adding-a-coffee-profile)
    - [Test Case 4: Updating a Coffee Profile](#test-case-4-updating-a-coffee-profile)
    - [Test Case 5: Deleting a Coffee Profile](#test-case-5-deleting-a-coffee-profile)
    - [Test Case 6: Searching for Coffee Profiles](#test-case-6-searching-for-coffee-profiles)
    - [Test Case 7: Responsive Design Across Devices](#test-case-7-responsive-design-across-devices)
    - [Test Case 8: Edge Cases](test-case-8-edge-cases)




## Getting Started

To get a copy of this project up and running on your local machine, follow these steps.

### Prerequisites

- Web browser: (Chrome, Firefox, Safari, etc.)
- IDE or Text Editor: (GitPod, Visual Studio Code, Sublime Text, Atom, etc.)

### Installation

1. Clone my repository with the following link:

[Git Clone](https://github.com/OrgNateDrake/milestone-project-3)

2. Open the project in your preferred IDE or Text Editor.

### Deployment

You can view the live site through **Heroku**, using the following link:

[Heroku - Live Site](https://milestone-3-project-29f9ad62c493.herokuapp.com)

The project was also deployed with GitHub Pages using the following steps...

1. Log in to [GitHub](https://github.com/).
2. At the top of the Repository (not top of page), locate and click the **Settings** Button on the menu.
3. Scroll down the Settings page until you locate the **Pages** Section (on the left of the page) and click.
4. Under **Build and deployment**, **Branch**. Click the dropdown called "None" and select **Main Branch**.
5. The page will automatically refresh.
6. Click **Save**.
7. Scroll back down through the page to locate the now published [Site Link](https://github.com) in the **GitHub Pages** section.


## Testing

### Automated Testing:

**Principles:**

1. **Repeatability:** Automated tests can be executed repeatedly without any variation in their steps and expected outcomes.

2. **Consistency:** Automated tests perform the same steps and checks each time, eliminating human errors and ensuring consistent results.

3. **Efficiency:** Automated tests can run quickly and efficiently, covering a large number of test cases in a short time.

4. **Regression Testing:** Automated tests are particularly useful for regression testing, where previously tested functionality is retested to ensure that new changes have not introduced defects.

5. **Data-Driven Testing:** Automation allows for data-driven testing, where tests are executed with different sets of data to verify various scenarios.

6. **Continuous Integration/Continuous Deployment (CI/CD):** Automated tests can be integrated into the CI/CD pipeline, allowing for immediate feedback on code changes and ensuring that only high-quality code is deployed.

**When to Deploy Automated Testing:**

- **Regression Testing:** Automated tests are ideal for regularly checking existing functionality after code changes.
- **Highly Repetitive Tests:** Tasks like data validation, login/logout procedures, and API testing can be automated for efficiency.
- **Load and Performance Testing:** Automated tools can simulate a large number of users to test system performance under heavy loads.
- **Cross-Browser and Cross-Platform Testing:** Automated frameworks can be used to test web applications on different browsers and platforms.

### Manual Testing:

**Principles:**

1. **Exploratory Testing:** Manual testing is excellent for exploratory testing, where testers actively explore the application to discover unforeseen issues and usability problems.

2. **User Experience (UX) Testing:** Manual testers can assess the application's user-friendliness, usability, and overall user experience, providing valuable insights.

3. **Ad Hoc Testing:** In situations where test cases aren't well-defined or documented, manual testers can perform ad hoc testing to identify issues.

4. **Non-Functional Testing:** Tests related to subjective criteria like aesthetics, layout, and overall look and feel are often better suited for manual testing.

**When to Deploy Manual Testing:**

- **Usability Testing:** To evaluate the user interface and overall user experience.
- **Exploratory Testing:** When new features are introduced or when test cases are not yet well-defined.
- **Complex Test Scenarios:** For intricate and multi-step test cases where human intuition is required.
- **Non-Functional Testing:** Assessing subjective aspects like aesthetics, accessibility, and human factors.

In practice, a combination of both automated and manual testing is often employed to ensure comprehensive test coverage. Automated testing is efficient for repetitive and regression testing, while manual testing is valuable for exploratory and usability aspects. The choice between them depends on project requirements, budget constraints, and the specific nature of the testing needed for a particular software application.

### Manual Testing Completed

To ensure the functionality, usability, and responsiveness of my web based application, a series of manual exploratory tests were conducted. These tests allowed me to thoroughly assess the website's performance and user experience across various scenarios and devices.

### Manual Tests for Tasty Coffee Website

### Test Case 1: User Registration

**Description:**
This test case verifies the functionality of user registration on the Tasty Coffee website.

**Steps:**
1. Open the Tasty Coffee website.
2. Navigate to the registration page.
3. Fill in the required fields with valid information (e.g., username, email, password).
4. Click on the "Register" button.

**Expected Results:**
- The user should be successfully registered and redirected to the home page.
- The user's profile should be created in the database.

### Test Case 2: User Login

**Description:**
This test case verifies the functionality of user login on the Tasty Coffee website.

**Steps:**
1. Open the Tasty Coffee website.
2. Navigate to the login page.
3. Enter valid login credentials (username/email and password).
4. Click on the "Login" button.

**Expected Results:**
- The user should be successfully logged in and redirected to the home page.
- The user's session should be maintained.
- Unauthorised users with bad credentials should not be allowed to login.

### Test Case 3: Adding a Coffee Profile

**Description:**
This test case verifies the functionality of adding a coffee profile to the website. Only by a registered user or a superuser.

**Steps:**
1. Login to the Tasty Coffee website.
2. Navigate to the profile creation page.
3. Fill in the required fields for the coffee profile (species, strength, quality, description).
4. Click on the "Add Profile" button.

**Expected Results:**
- The coffee profile should be successfully added to the database, with the username linked.
- The newly added profile should be searchable by visitors to the site.

### Test Case 4: Updating a Coffee Profile

**Description:**
This test case verifies the functionality of updating an existing coffee profile on the website. Only by the original posting user or a superuser.

**Steps:**
1. Login to the Tasty Coffee website.
2. Navigate to the profile editing page for an existing coffee profile.
3. Modify the desired fields (species, strength, quality, description).
4. Click on the "Update Profile" button.

**Expected Results:**
- The coffee profile should be successfully updated in the database.
- Changes should be reflected in the profile details displayed on the website.

### Test Case 5: Deleting a Coffee Profile

**Description:**
This test case verifies the functionality of deleting an existing coffee profile from the website. Only by the original posting user or a superuser.

**Steps:**
1. Login to the Tasty Coffee website.
2. Navigate to the profile editing page for an existing coffee profile.
3. Click on the "Delete Profile" button.

**Expected Results:**
- The coffee profile should be successfully deleted from the database.
- The profile should no longer be visible or searchable on the website.

### Test Case 6: Searching for Coffee Profiles

**Description:**
This test case verifies the functionality of searching for coffee profiles on the Tasty Coffee website. By any user, registered or not registered.

**Steps:**
1. Open the Tasty Coffee website.
2. Locate the search bar.
3. Enter a search query (e.g., coffee species, strength, quality).
4. Press the "Enter" key or click on the search icon.

**Expected Results:**
- Relevant coffee profiles matching the search query should be displayed.
- The search results should be accurate and relevant to the query entered.

### Test Case 7: Responsive Design Across Devices

**Description:**
This test case verifies the responsiveness of the Tasty Coffee website across various devices and screen sizes.

**Steps:**
1. Access the Tasty Coffee website using different devices (e.g., desktop, laptop, tablet, smartphone).
2. Resize the browser window to simulate different screen sizes.
3. Navigate through different pages and features of the website.

**Expected Results:**
- The website should adapt smoothly to different screen sizes without any layout or functionality issues.
- Content should be readable and accessible on all devices, with no horizontal scrolling required.

### Test Case 8: Edge Cases

**Description:**
This test case explores edge cases and potential unusual scenarios that may occur on the Tasty Coffee website.

**Steps:**
1. Perform actions or input data that are outside the normal usage patterns.
2. Attempt to trigger errors or unexpected behavior by entering invalid data or performing uncommon actions.
3. Test the robustness of the website's error handling and recovery mechanisms.

**Expected Results:**
- The website should gracefully handle edge cases, providing clear error messages or guidance to the user.
- Critical functionalities should not break under unexpected circumstances, and the website should maintain stability.