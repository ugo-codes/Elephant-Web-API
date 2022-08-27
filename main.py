import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from forms import ElephantForm
from api import get_by_name, get_by_sex

# initialize the Flask application
app = Flask(__name__)
# set a secret key for use for the flask form
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
# initialize the app to use bootstrap
Bootstrap(app)


# a route to the home page
@app.route("/", methods=["GET", "POST"])
def home():
    """
    This method is called when the home route is loaded on the web browser. It renders the home page
    :return: (str) the web page is rendered
    """

    # initialize the form
    form = ElephantForm(request.form)

    # if the user has submitted the form, and it is valid
    if form.validate_on_submit():
        # get the search and user input from the form
        search = form.search.data
        user_input = form.input.data

        # redirect the user to the result url and pass the sear and user input
        return redirect(url_for("result", search=search, user_input=user_input))

    # return the index.html web page
    return render_template("index.html", form=form)


# a route to the home page
@app.route("/result/<search>/<user_input>")
def result(search: str, user_input: str):
    """
    This method is called when the result route is loaded on the web browser. It renders the result page
    :param search: (str) what aspect of the elephant the user want to search for
    i.e Name or Sex
    :param user_input: (str) exactly what the user is searching for
    :return: (str) The web page to be rendered
    """

    # if the search is equal to Name and the user_input is meaningful
    if search == "Name" and user_input != "...":
        # get the search result
        results = get_by_name(user_input)

    # if the search is equal to Sex and the user_input is meaningful
    elif search == "Sex" and user_input != "...":
        # get the search result
        results = get_by_sex(user_input)

    # render the result.html page with the results
    return render_template("result.html", results=results)


# if this is the main app run this flask application in debug mode
if __name__ == "__main__":
    app.run(debug=True)
