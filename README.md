---
Hello, my name is Jessica Ayala. The below information is some brief documentation in regards to the Amazon project created for automation purposes. This project is python selenium based.
----
Overview
----
  - Installation Requirements, Tools
  - Feature Files, Scenarios
  - Python Files, Code Description
---  
Tools/Installation Requirements
---
Automating in Python Selenium you will need following external tools:
  - Install Python 2 or Python3 (In this repo, you will see we are using Py3)
    (Use pip3 to do installs such as selenium)
  - Install Chromedriver
  - Install Selenium
  - Set environment variables
  - Install Git (Allow you to edit, commit, push changes to repo)
  - Selenium + Cucumber plug in

---
Feature Files
---
Initially, test cases are identified upon reviewing scopes for new feature/implementations. These are normally stored into feature files based on their scope. Feature files in automation are important because they give the DEV/QA an informative view of behaviours of our testing (BDD based). They're helpful to know how features work for users, hence it's important that feature files are laid out in a readable way. Not only are they helpful to see how features are working for users, but it's also a good practice for QA to run regression or smoke tests by either adding a tag per scenario or by running all feature files. 
Scenarios in this repo are styled with Gherkin language:
   - Use @Given, @And, @When, @Then for the begining of each step in a scenario
   - Use "feature:" for the begining of a feature file, stating the file's main functionally
   - Use "scenario:" for the begining of a scenario, and write out verification statement
   
 *Note: Currently consists of the Amazon flows for creating a new account on main site, adding items to shopping cart.*   

---
Python Files
---
After creating feature files + scenarios/steps, you then can add step definitions pertaining to each feature file. (This is where the code is stored for each scenario/step). It is defined to tell the Chrome webdriver what to do. 

---
Running Tests
---
Tests can be run by adding tags (e.g. @regression, @smoke, @jessica) in a particular scenario depending on what the goal is or all scenarios in a feature file can be executed simultaneously with the run button as well without having to add tags.



  
