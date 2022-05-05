import flask
import crud
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/byname', methods=['GET'])
def by_name():
    session = crud.start_session()
    nfts = crud.query_nft_by_name("APE", session)
    list = []
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)

@app.route('/bycontract', methods=['GET'])
def by_contract():
    session = crud.start_session()
    nfts = crud.query_nft_by_contract_address("0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d", session)
    list = []
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)
    
@app.route('/byname2', methods=['GET'])
def by_contract2():
    session = crud.start_session()
    nfts = crud.query_nft_by_name("APE", session)
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)

@app.route('/byname3', methods=['GET'])
def home2():
    session = crud.start_session()
    list = []
    nfts = crud.query_nft_by_name("APE", session)
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)

app.run()