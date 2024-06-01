
# Steganography Lab 
This GitHub is part of the Cybersecurity lab developed by the [Science Mentorship Institute](https://www.sci-mi.org "Science Mentorship Institute") for the [Computer Science Mentorship Program](https://sci-mi.org/csmp.html "Computer Science Mentorship Program at the Science Mentorship Institute").

The goal is for students to have a chance to have some simple exposure to the Python programming language, running it (either in CodeSpaces on GitHub or locally), and the concepts behind Steganography.

## Running
There are two directions you can use to run this, depending on if you have a personal machine and want to get it running. Codespaces will be only online (and will likely be smoother). Local setup will involve downloading the code to your machine.

You should already have a GitHub account. We want to create a copy of this repository that is yours, called a "fork." Click `fork` at the top-right of the screen, then click the button at the bottom that says `create fork`. You can change some settings/text if you want to, but be warned that it might break functionality. 

### Codespaces
Clicking the green `Code` button at the top of this page, there will be a drop down with two tabs, one saying `Local` and one saying `Codespaces`. Click `Codespaces`. Click `Create Codespace on Main`.

Once your Codespace has started up, navigate to `notebooks/stego_encoding.ipynb` on the left-hand side. 

### Local Setup
If you wish to use your local machine, please talk to your mentor about this beforehand so you two can get your system set up correctly. 

What you need:
- IDE/Text editor. I would suggest VS Code with the Jupyter Notebook and Python extensions. You can use PyCharm, JupyterLab, etc., but they will require more work to get running.
- A local clone of this repo. Click the green `Code` button and copy the HTTPS (Windows) or SSH (macOS/Linux). In the terminal or with the Desktop app clone the repo. In the terminal you can run 
```git clone <repo URL>```
and it will copy into the current directory.

Once you have something to run it in and the code locally, open up the repo with your IDE. If you have a sophisticated tool (e.g. VS Code or PyCharm), it will direct you to install any packages you are missing. Make sure to open up the repo directory, not the individual files, as the Jupyter Notebooks need to be able to find the rest of the code, and this can break if the editor does not know the correct place to run them.
