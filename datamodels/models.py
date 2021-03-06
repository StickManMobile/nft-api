from importlib.metadata import metadata
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_json import mutable_json_type
from dataclasses import dataclass
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()


@dataclass
class Contract(Base, SerializerMixin):
    __tablename__ = 'contract'
    contract_id = Column(String, primary_key=True)
    contract_name = Column(String)
    contract_symb = Column(String)
    contract_type = Column(String)

    def __repr__(self):
        return "<Contract(Name='{}', Symbol'{}', Type={})>"\
            .format(self.contract_name, self.contract_symb, self.contract_type)


@dataclass
class NFT(Base, SerializerMixin):
    __tablename__ = 'nft'
    token_id = Column(Integer, primary_key=True)
    contract_id = Column(String)
    chain = Column(String)
    meta = Column(mutable_json_type(dbtype=JSONB, nested=True))
    metadata_url = Column(String)
    file_url = Column(String)
    cached_file_url = Column(String)
    mint_date = Column(Date)
    file_information = Column(mutable_json_type(dbtype=JSONB, nested=True))
    updated_date = Column(Date)
