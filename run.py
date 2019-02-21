from flask import Flask, render_template

app = Flask(__name__)
posts = [
  {
    'author':'Don',
    'title': "Test post 1",
    'content': "Test content 1"
  },
  {
    'author':'Don',
    'title': "Test post 2",
    'content': "Test content 2"
  },
  {
    'author':'Don',
    'title': "Test post 3",
    'content': "Test content 3"
  },
]

@app.route('/')
def home():
  return render_template('home.html', posts = posts)




if __name__ == "__main__":
  app.run(debug = True)
