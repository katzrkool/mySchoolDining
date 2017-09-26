# MySchoolDining Menu Fetcher
Downloads menu from MySchoolDining and prints it

## Prerequisites
* Requests
* Beautiful Soup 4

Both can be install via pip

`pip install requests bs4`

## Download
The latest release can be installed [here](https://github.com/katzrkool/mySchoolDining/releases)

## Usage
Run menu.py

It'll ask you for your mySchoolDining code

Example: For myschooldining.com/thenewschool, your url code is thenewschool

Once you enter that, it'll check if your school has multiple menus.

If you do, it'll ask you to pick one.

It'll then print out the menu.

Following that, it'll ask if you want to save data. If you agree, it'll save your school code and menu choice in a file called preferences.json

To delete your choices, delete preferences.json

Enjoy!

## Stuff to do
- [ ] Allow in program deletion of preferences
- [ ] Add support for headers like Lunch or Breakfast
- [ ] Testing various menus
