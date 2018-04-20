from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def welcome():
    return render_template('index.html')

@app.route("/recommend", methods=['GET','POST'])
def main():
    username = request.form['username']
    recommendations = []
    # recommendations = func_call(username)
    print ("Username: "+username)
    print ("Recommendations: ")
    print (recommendations)
    return render_template('recommendations.html', user=username, recommendations=recommendations)

if __name__ == '__main__':
    app.run()