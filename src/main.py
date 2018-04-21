from flask import Flask, render_template, request
from process import Data
import graphlab as gl

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def welcome():
    return render_template('index.html')

@app.route("/recommend", methods=['GET','POST'])
def main():
    d = Data()
    username = request.form['username']
    reco = d.getRecommendation([username], 10)
    pn = d.queryAmazon(reco['ProductId'])
    pn = [x.encode('UTF8') for x in pn]
    reco.add_column(gl.SArray(pn), name='ProductName')
    rn = d.queryAmazon(reco['ProductId'], 'Images')
    rn = [x.encode('UTF8') for x in rn]
    reco.add_column(gl.SArray(rn), name='ProductURL')
    reco = reco.pack_columns(columns=['score', 'rank', 'ProductName', 'ProductURL'], new_column_name='Details')
    df = reco.to_dataframe().set_index('ProductId')
    recommendations = df.to_dict(orient='dict')['Details']
    return render_template('recommendations.html', user=username, reco=recommendations)

if __name__ == '__main__':
    app.run()