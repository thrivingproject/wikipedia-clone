import util
import markdown2
import random

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/create/", methods=["GET", "POST"])
def article_create_view():
    """
    View to create a new article
    """
    if request.method == "POST":
        return handle_article_form()
    # GET request
    return render_template("article_create.html")


@app.route("/")
def article_list_view():
    """
    View to list all entries
    """
    return render_template("article_list.html", entries=util.list_entries())


@app.route("/wiki/<article_title>/edit", methods=["GET", "POST"])
def article_edit_view(article_title):
    """
    View to edit an existing article
    """
    if request.method == "POST":
        return handle_article_form(article_title)
    # GET request
    return render_template(
        "article_edit.html",
        article_content=util.get_article(article_title),
        article_title=article_title,
        active_action="edit",
    )


@app.route("/wiki/<article_title>/")
def article_detail_view(article_title):
    """
    View to display an article in markdown
    """
    article = util.get_article(article_title)
    if not article:
        return render_template("article_dne.html")
    return render_template(
        "article_detail.html",
        article_content=markdown2.markdown(article),
        article_title=article_title,
        active_action="read",
    )


def handle_article_form(article_title=None):
    """
    Helper function to handle creating or editing an article
    """
    if not article_title:
        article_title = request.form["article_title"]
        if util.get_article(article_title):
            return render_template("error.html", message="article already exists")
    util.save_article(article_title, request.form["article_content"])
    return redirect(f"/wiki/{article_title}")


@app.route("/random/")
def random_article_view():
    """
    View to redirect to a random article
    """
    return redirect(f"/wiki/{random.choice(util.list_entries())}")


@app.route("/search/")
def search_view():
    """
    View to search for entries
    """
    query = request.args.get("query")
    entries = util.list_entries()
    results = [article for article in entries if query.lower() in article.lower()]
    if len(results) == 1 and results[0].lower() == query.lower():
        return redirect(f"/wiki/{results[0]}")
    return render_template("search_results.html", results=results, query=query)


if __name__ == "__main__":
    app.run(debug=True)
