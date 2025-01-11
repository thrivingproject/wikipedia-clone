import util
import markdown2

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def entry_list_view():
    return render_template("entry_list.html", entries=util.list_entries())


@app.route("/wiki/<entry_title>/edit", methods=["GET", "POST"])
def entry_edit_view(entry_title):
    if request.method == "POST":
        entry_content = request.form["entry_content"]
        util.save_entry(entry_title, entry_content)
        return redirect(f"/wiki/{entry_title}")
    # GET request
    return render_template(
        "entry_edit.html",
        entry_content=util.get_entry(entry_title),
        entry_title=entry_title,
    )


@app.route("/wiki/<entry_title>")
def entry_detail_view(entry_title):
    return render_template(
        "entry_detail.html",
        entry_content=markdown2.markdown(util.get_entry(entry_title)),
        entry_title=entry_title,
    )


if __name__ == "__main__":
    app.run(debug=True)
