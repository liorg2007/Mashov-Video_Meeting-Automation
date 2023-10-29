# Mashov-Video_Meeting-Automation
<img src="https://web.mashov.info/students/images/logo_students.png" style="width:100px; height:100px;">
Selenium code that enters to the web app "משוב", logs in, and enters a live meeting.

Mashov(Version: 3.20210425) has a vulnerability in the video meeting feature that allows the same user to enter the meeting with different session_id.
It then shows in the meeting the same person several times.

The code is rather simple, it requires the username and password to log in, the number of the lesson from the available ones and the number of entries.

## Libraries
Libraries:
```
pip install selenium
pip install webdriver_manager
pip install time
```
