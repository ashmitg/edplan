
## Personalized Student Plan Generator


The Personalized Student Plan Generator is a project that aims to assist students in planning their academic course load based on their transfer documents from assist.org, IGETC requirements, preferred class load per quarter, and classes of interest. The frontend of this application is implemented as a Discord bot, allowing users to upload their assist.org course requirement document and specify their preferences for class distribution across quarters and summers. The bot utilizes data structures and algorithms, including a greedy algorithm, to create a balanced and sequential course plan for each student.



## Features

- Upload your assist.org course requirement document.
- Set preferences for maximum classes per quarter and summer.
- Specify classes of interest, such as Math, ECON, PSYC.
- The bot employs a greedy algorithm to create a well-balanced course plan.
- Sequential ordering of classes based on prerequisites.
- Receive a customized course plan tailored to your requirements.


## How to Run Locally

Clone the repo
```bash
  git clone https://github.com/ashmitg/educational-plan.git
  cd my-project
```
Install the packages: reccomended to use a env
```bash
    pip install -r requirements.txt
```
Run main.py ensuring your discord token is correctly configured

Congrats you ran the bot!

## Heroku Hosting

1. Make sure you have a heroku account
2. Log into heroku
```bash
heroku login
```
3. Procfile and requirements are already setup!
4. Next step deploy!
```bash
git add .
git commit -m "Push my bot!"
git push heroku master
```

## Authors

- [@ashmitg](https://www.github.com/ashmitg)


## License

[MIT](https://choosealicense.com/licenses/mit/)

