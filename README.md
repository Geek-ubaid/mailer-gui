<p align="center">
	<img src="https://user-images.githubusercontent.com/30529572/72455010-fb38d400-37e7-11ea-9c1e-8cdeb5f5906e.png" />
	<h2 align="center"> MailerGui </h2>
	<h4 align="center"> A pip package with a GUI interface for managing bulk mailing of organization events <h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](INSERT_LINK_FOR_DOCS_HERE) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](INSERT_UI_LINK_HERE)


## Functionalities
- [ ]  Send Bulk Mail at once
- [X]  Send test mail to any email
- [X]  View and edit HTML template
- [ ]  Set Placeholder values for the template
- [X]  Recipients extraction from .csv file with view support
- [ ]  View and Download Logs of the bulk mail tasks
- [X]  Send mail with/without attachments
- [X]  Send plainText/HTML mails

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

# sendgrid API key
API_KEY
```

Find a sample of the environment variables [here](./MailerGui/.env.sample)


- You can also Build from source (Current Scenario)
	- clone the repo
	```bash
	git clone repo_name 
	```
	- Change the working directory
	```bash
	cd MailerGui
	```
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
<br>

<p align="center">
	Made with :heart: by DSC VIT
</p>

