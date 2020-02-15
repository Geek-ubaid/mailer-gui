<p align="center">
	<img src="https://user-images.githubusercontent.com/30529572/72455010-fb38d400-37e7-11ea-9c1e-8cdeb5f5906e.png" />
	<h2 align="center"> MailerGui </h2>
	<h4 align="center"> A pip package with a GUI interface for managing bulk mailing of organization events <h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](INSERT_LINK_FOR_DOCS_HERE) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](INSERT_UI_LINK_HERE)


## Functionalities
- [X]  Send Bulk Mail at once
- [X]  Send test mail to any email
- [X]  View and edit HTML template
- [X]  Set Placeholder values for the template
- [X]  Recipients extraction from .csv file with view support
- [X]  Send mail with/without attachments
- [X]  Send plainText/HTML mails
- [ ]  View and Download Logs of the bulk mail tasks

<br>

## Application Overview

<details open>
<summary> Landing Screen </summary>
<br><br>
<p align='center'>
<img src='MailerGui\Data\Screens\main_screen.PNG'/><br><br>
This is the main page of the application. This is the landing screen where you will operate all the operations like sending mails and selecting the data to be send.
</p>
</details>

<br>

<details>
<summary> Login Screen </summary>
<br><br>	
<p align='center'>
<img src='MailerGui\Data\Screens\login_screen.PNG'/><br><br>
This is the landing page of the application for logging into the application. Use your username and password which you will set at the intial installation.
</p>
</details>


<br>

<details>
<summary> Recipients View Screen </summary>
<br><br>
<p align='center'>
<img src='MailerGui\Data\Screens\recipients_screen.PNG'/><br><br>
Here the user will be able to see all the recipients details imported in to the application. You can view all the imported recipients at once.
</p>
</details>

<br>

<details>
<summary> Previewing HTML Screen </summary>
<br><br>
<p align='center'>
<img src='MailerGui\Data\Screens\view_html.PNG'/><br><br>
This window will help you view the html template you are sending. You can verify the placeholder text by taking a look at how mail will look in reciever's mailbox.
</p>
</details>

<br>

<details>
<summary> Summary Screen </summary>
<br><br>
<p align='center'>
<img src='MailerGui\Data\Screens\confirm screen.PNG'/><br><br>
This window will help the user to confirm all the selected items before starting the bulk mail process. This window will  user to validate all the details are correct or not and confirm by ticking the check box before starting the bulk process. This will reduce the chances of error.
</p>
</details>

<br>

<details>
<summary> Progress Screen </summary>
<br><br>
<p align='center'>
<img src='MailerGui\Data\Screens\progress_screen.PNG'/><br><br>
This window will show real time logs of the bulk process. This will help the user monitor the process and validate whether the mails are not sending and keep a check on all the bounce rate of mails.
</p>
</details>

<br>

## Instructions to run

* Setup up Python env
		
	```bash
	pip install virtualenv
	virtualenv env
	```  
* Activate Environment
	- Windows
	```bash
	cd env/Scripts && activate
	```
	- Linux
	```bash
	source ./env/Scripts/activate
	```

* Install from pip package(WIP)
  ```bash
  pip install MailerGui
  ```
	
* Add the following variables to your PATH:

	```bash
	# your login credentials to MailerGui
	LOGIN_NAME

	# your password
	PASSKEY

	# mailgun API key
	API_KEY

	# mailgun domain name
	DOMAIN_MAIL

	# sender mail address
	FROM_MAIL
	```

	Find a sample of the environment variables [here](./MailerGui/.env.sample). Windows user can make .env file based on the sample env file.

- You can also Build from source (Current Scenario)
	- clone the repo
		```bash
		git clone repo_name 
		```
	- Change the working directory
		```bash
		cd MailerGui
		```
	- Create a virtual env based on the instructions given above.

	- Install all the requirements in the active environment
		```bash
		pip install -r requirements.txt
		```
	- Run the program by executing
		```bash
		python main_gui.py
		```
	
<br>


## Contributors

* [Geek-Ubaid](https://github.com/Geek-ubaid)


<br>


<p align="center">
	Made with :heart: by DSC VIT
</p>

