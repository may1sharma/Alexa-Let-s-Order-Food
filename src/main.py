from flask import Flask, render_template, request
from process import Data
import sys

app = Flask(__name__)
data = Data()

@app.route("/", methods=['GET','POST'])
def welcome():
    popular = data.whatsTrending(20)
    ids = data.getAllItems()
    return render_template('index.html', popular=popular, data=ids)


@app.route("/recommend", methods=['GET','POST'])
def user():
    username = request.args.get('user')
    if username == 'query': username = request.form['username']
    profilename = data.getUserName(username)
    reco = data.getRecoForUser([username], 10)
    history = data.userHistory(username, 10)
    return render_template('recommendations.html', user=profilename, reco=reco, hist=history)

@app.route("/item", methods=['GET','POST'])
def item():
    item = request.args.get('item')
    if item == 'query': item = request.form['item']
    name = data.queryAmazon([item])[0].encode('UTF8')
    img_url = data.queryAmazon([item], 'Images')[0].encode('UTF8')
    rating = data.getAverageRating(item)
    similar = data.getSimilarItems(item, 10)
    helpful = data.helpfulReviews(item, 5)
    return render_template('item.html', id=item, name=name, url=img_url, rating=rating, similar=similar, helpful=helpful)

if __name__ == '__main__':
    if len(sys.argv)==2 and sys.argv[1] == 'create':
        data.createModels()
    elif len(sys.argv)==2 and sys.argv[1] == 'debug':
        app.debug = True
        app.run(threaded=True)
    else:
        app.run(threaded=True)