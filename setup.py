  
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "MailerGui", 
    version = "0.0.1",
    author = "Ubaid Usmani",
    author_email = "usmaniubaid@gmail.com",
    description = "Bulk Mailing Interface for mass mailing",
    entry_points = {"console_scripts" : [
                        'mailergui = MailerGui:mailer'
        ]},
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/GDGVIT/mailer-gui",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    
)