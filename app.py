from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates")

# List of careers
careers = [
    "Software Engineer",
    "Data Scientist",
    "Graphic Designer",
    "Digital Marketer",
    "Product Manager",
    "Teacher",
    "Doctor",
    "Lawyer",
    "Chef",
    "Writer"
]

# List to store posts
posts = []

# Home page
@app.route("/")
def home():
    return render_template("home.html", careers=careers, posts=posts)

# Search functionality
@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    filtered_careers = [career for career in careers if query in career.lower()]
    return render_template("home.html", careers=filtered_careers, posts=posts)

# Post functionality
@app.route("/post", methods=["POST"])
def create_post():
    content = request.form.get("content")
    if content:
        posts.append(content)
    return redirect("/")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)