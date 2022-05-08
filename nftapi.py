import flask
import dbaccess.crud as crud
import json
import pytest
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/byname', methods=['GET'])
def by_name():
    search = request.args.get('name')
    session = crud.start_session()
    nfts = crud.query_nft_by_name(search, session)
    list = []
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)


@app.route('/bycontract', methods=['GET'])
def by_contract():
    search = request.args.get('contract')
    session = crud.start_session()
    nfts = crud.query_nft_by_contract_address(search, session)
    list = []
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)


@app.route('/bycontracttoken', methods=['GET'])
def by_contract2():
    search = request.args.get('contract')
    token = request.args.get('token')
    session = crud.start_session()
    nfts = crud.query_nft_by_contract_address_token(search, token, session)
    for data in nfts:
        list.append(data.to_dict())
    return json.dumps(list)


@app.route('/index', methods=['GET'])
def home2():
    return "NOT YET IMPLEMENTED"


app.run()
