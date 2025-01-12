import util
import markdown2
import random

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/create/", methods=["GET", "POST"])
def entry_create_view():
    """
    If the form is submitted, save the entry and redirect to the entry
    detail view; otherwise, render the create form
    """
    if request.method == "POST":
        return handle_entry_form()
    # GET request
    return render_template("entry_create.html")


@app.route("/")
def entry_list_view():
    """
    Render the list of entries
    """
    return render_template("entry_list.html", entries=util.list_entries())


@app.route("/wiki/<entry_title>/edit", methods=["GET", "POST"])
def entry_edit_view(entry_title):
    """
    If the form is submitted, call helper function to save the entry;
    otherwise, render the edit form with the entry content
    """
    if request.method == "POST":
        return handle_entry_form(entry_title)
    # GET request
    return render_template(
        "entry_edit.html",
        entry_content=util.get_entry(entry_title),
        entry_title=entry_title,
    )


@app.route("/wiki/<entry_title>/")
def entry_detail_view(entry_title):
    """
    Render the entry detail view with the content of the entry
    """
    return render_template(
        "entry_detail.html",
        entry_content=markdown2.markdown(util.get_entry(entry_title)),
        entry_title=entry_title,
    )


def handle_entry_form(entry_title=None):
    """
    Helper function to handle creating or editing an entry
    """
    if not entry_title:
        entry_title = request.form["entry_title"]
        if util.get_entry(entry_title):
            return render_template("error.html", message="Entry already exists")
    entry_content = request.form["entry_content"]
    util.save_entry(entry_title, entry_content)
    return redirect(f"/wiki/{entry_title}")


@app.route("/random/")
def random_entry_view():
    """
    Redirect to a random entry
    """
    return redirect(f"/wiki/{random.choice(util.list_entries())}")


@app.route("/search/")
def search_view():
    """
    Render the search results; render entry detail view if exact match
    """
    query = request.args.get("query")
    entries = util.list_entries()
    results = [entry for entry in entries if query.lower() in entry.lower()]
    if len(results) == 1 and results[0].lower() == query.lower():
        return redirect(f"/wiki/{results[0]}")
    return render_template("search_results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
