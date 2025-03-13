Frontend Automated Test Challenge

   This project is a small test suite testing functionalities of six specific webpages.

Project Structure

Tests and functions related to them are all in /Tests folder.
Each page has its own separate test suire, containing all tests related to that one page.
Each test should be called test_{page name} to ensure that all tests can be run together.

Prerequisites

- Python 3.x
- Chrome browser installed
- ChromeDriver matching your Chrome browser version

Installation

1. Clone the repository
2. Install dependencies using: pip install -r requirements.txt

Running Tests

To run all tests use: pytest Tests/

To run a specific test file use: pytest Tests/test_ExitIntent.py
or run the specific file with Python, for example: python Tests/test_ExitIntent.py

Test Scenarios

 Drag and Drop
- Tests drag and drop functionality
- URL: https://the-internet.herokuapp.com/drag_and_drop
- One positive test and one negative test for drag and drop functionality

 Dynamic Controls
- Tests dynamic checkbox and input field controls
- URL: https://the-internet.herokuapp.com/dynamic_controls
- Both checkbox and input field tested before and after enabling/disabling. 
  Additionally, input field is used as a part of the test.

 Exit Intent
- Tests exit intent modal functionality
- URL: https://the-internet.herokuapp.com/exit_intent
- As the modal window can appear only one per tab instance, there is one test - in which the test 
  expects the modal window to appear and then it is closed

 Frames
- Tests nested frames functionality
- URL: https://the-internet.herokuapp.com/nested_frames
- URL: https://the-internet.herokuapp.com/iframes
- Two separate tests for catching frames and reading text that they hold.

 Secure File Download
- Tests secure file download functionality
- URL: https://the-internet.herokuapp.com/download_secure
- One test for downloading a file, where the test asserts that the file is properly downloaded and 
  contains the expected text.

 Shadow DOM
- Tests shadow DOM functionality
- URL: https://the-internet.herokuapp.com/shadowdom
- Two tests in which the test find a specific shadow root and reads the text from underneath it.


Utilities file

The Utilities.py file contains common functions used across tests:
- setup_driver(): Configures and initializes the Chrome WebDriver

Contributing
 1. Fork the repository
 2. Create your feature branch
 3. Commit your changes
 4. Push to the branch
 5. Create a new Pull Request