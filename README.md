Coverage: 100%
# Python-Project-week10
The project is games management system, it is built to allow you to check information on games and which publishers published what games. The application has full CRUD functionality. 

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

# Prerequisites
## Software needed
Visual Studio Code - I use VSC for my code and terminal, to install it,  https://code.virtualstudio.com/download follow the instruction here to download your own

Google Cloud Platform account – I use GCP for running my VMs and to host my Database, create an account here, https://cloud.google.com

Github – I use github as my online repository, create an account here, https://github.com/


# Installing
Create a GCP account to receive, this gives you $300 of free credit for 90 days, after which you will need to pay.

Create firewall rules for port 5000 and port  8080, you will use port 5000 to run the app and port 8080 is to use for Jenkins(touched on later).

On GCP, create a new VM instance, adding the port 5000 rule, make sure that you change the boot OS to ubuntu as the default is Debian. To maximise credits for the 3 months, I’d recommend using a small or medium vm as they cost less credits to keep running.

Open VSC, download the SSH extension. Using this extension in the click the green button in the bottom left and open the .ssh/config file.

Create a new user profile with the hostname set as the VM external IP address and the user as the name of your local user.

Delete the file .ssh/known_hosts with the command ‘rm known_hosts’ in terminal.

Run the command ssh-keygen and press enter until it displays your key as art.

Then run the command cat .ssh/id_rsa.pub to display the public ssh key, copy this and edit VM instance on GCP to include this ssh key.

Click the green button in the bottom left of VSC then click connect to host, select the new host user profile and click yes to continue.

Once you have connected to the vm, run ssh-keygen and cat .ssh/id_rsa.pub and copy the public ssh key from the vm.

Paste this key into your github ssh keys, this will allow you to use ssh keys to clone repositories and such which decreases vulnerabilities and thus will make your database more secure.

Then clone the repository using ‘git clone git@github.com:KugananK/Python-Project-week10.git’

Run the command ‘bash startup.sh’

Open the app on port 5000, this will be your VM’s external IP with ‘:5000’ at the end of it in your browser.

# Testing
To run the testing use the command ‘python3 -m pytest --cov-report term-missing --cov application/ test/’

This will also run automatically upon creating a Jenkins build, this command will show you which lines of code have not been tested and it will also show you what tests are erroring

class TestViews(TestBase):
    def test_game_get(self):
        response = self.client.get(url_for('indexgames'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SampleTestGame', response.data)

This test above extends the TestBase class which before every test will create a test publisher and assign it a test game. This specific test will then test the get method for the indexgames. This will check whether the output is SampleTestGame. This will pass as the TestBase class creates a game called SampleTestGame.

# Built With

•	Flask
•	Jenkins
# Coded With

•	Python
•	HTML
# Authors

•	Kajan Kugananthajothy - Author - kuganank
# License

This project is licensed under the MIT license
 
# Acknowledgments

•	Hat tip to bros Afzal and Zake
•	Qa-community
•	W3schools
