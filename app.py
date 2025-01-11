import util
import markdown2

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def entry_list_view():
    return render_template("entry_list.html", entries=util.list_entries())


@app.route("/wiki/<entry_title>")
def entry_detail_view(entry_title):
    return render_template(
        "entry_detail.html", entry=markdown2.markdown(util.get_entry(entry_title))
    )
