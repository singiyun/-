from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
  return render_template("home.html", name="singiyun")


@app.route("/hello")
def hello():
  return render_template("search.html")


app.run("0.0.0.0")

#home.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Job Scrapper</title>
</head>
<body>
  <h1>Job Scrapper</h1>
  <h4>What job do you want?</h4>
  <form action="/search">
    <input type="text" name="keyword" placeholder="Write keyword please" />
    <button>Search</button>
  </form>
</body>
</html>

#search.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Search Results:</h1>
</body>
</html>