# README #

How to deploy your Streamlit app to Heroku. Here are the 4 main steps:

1. Prepare your app files
2. Create a Git repository
3. Create a Heroku app
4. Deploy your app on Heroku

### (1) Prepare your app files ###

* Rename your Streamlit app to `app.py`
* All your data files should be in the same folder as `app.py`. In my case I only have 1 datafile, namely: `unemployment.tsv`
* Create a file called `requirements.txt` and include the name of all the packages used in your app. In my case I only used:
```
pandas
streamlit
altair
vega_datasets
```
* Copy the `setup.sh` and `Procfile` from this repository in your folder
* Create a file named `README.md` and add instructions for users to run your app using Streamlit if they choose to clone this repository. Here is an example of what you can write in `README.md`:
```
# README #
After cloning this repository you can run the Streamlit app using the following command: `streamlit run app.py`
```

### (2) Create a Git repository ###

* On GitHub or BitBucket create an empty repository. Note that you need to have an account on these platforms. In my case, I used BitBucket and created an empty repository called `test-streamlit`, [https://bitbucket.org/uqlab/test-streamlit.git](https://bitbucket.org/uqlab/test-streamlit.git)
* Commit and push your files into your repository. In my case I executed the following commands in my folder (note that the git url will be different for you and the name of the datafiles as well):
```
git init
git remote add origin https://bitbucket.org/uqlab/test-streamlit.git
git add README.md
git add setup.sh
git add Procfile
git add requirements.txt
git add app.py
git add unemployment.tsv
git commit -m "first commit"
git push origin master
```

### (3) Create a Heroku app ###

* Create a free account on [Heroku](https://www.heroku.com)
* Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#other-installation-methods). In my case, I had challenges installing the CLI using the installer provided for Windows. Instead, I have used the `npm` approach. In this case you need to have `node` and `npm` installed. Namely, I executed the following command:
```
npm install -g heroku
```
* Create a new app on Heroku using the following commands. In my case, I called the app `uncc-test-streamlit`
```
heroku login
heroku create uncc-test-streamlit
```
* Once the create command executes it will return 2 URLs. One URL that you can use to access your app online and a Git URL that we will use to deploy your app. In my case, I got the following response:
```
Creating app... done, ⬢ uncc-test-streamlit
https://uncc-test-streamlit.herokuapp.com/ | https://git.heroku.com/uncc-test-streamlit.git
```
* At this point this is an empty app - you can access the URLs but there is nothing interestng there

### (4) Deploy your app on Heroku ###

* To deploy your app on Heroku you need to push your files in the Heroku git repository, which was returned at the time of app creation. In my case this is `https://git.heroku.com/uncc-test-streamlit.git` and I have executed the following commands:
```
git remote add heroku https://git.heroku.com/uncc-test-streamlit.git
git push heroku master
```
* It will take some time for the app to be deployed. If successful you will get a message like this:
```
remote: -----> Launching...
remote:        Released v3
remote:        https://uncc-test-streamlit.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
```
* At this point you can access your app using the provided URL. In my case: [https://uncc-test-streamlit.herokuapp.com/](https://uncc-test-streamlit.herokuapp.com/)