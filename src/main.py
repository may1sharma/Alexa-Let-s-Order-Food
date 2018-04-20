from flask import Flask, render_template, request
# import Data

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def welcome():
    return render_template('index.html')

@app.route("/recommend", methods=['GET','POST'])
def main():
    # d = Data()
    # username = request.form['username']
    # reco = d.getRecommendation([username], 10)
    # reco = reco.pack_columns(columns=['score', 'rank'], new_column_name='Details')
    # df = reco.to_dataframe().set_index('ProductId')
    # recommendations = df.to_dict(orient='dict')['Details']
    return render_template('recommendations.html')

if __name__ == '__main__':
    app.run()