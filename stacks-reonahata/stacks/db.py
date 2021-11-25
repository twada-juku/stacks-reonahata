import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

def create_session(test_config=None):
    """SQLAlchemy の session を作成する。
    test_config 引数に既に（テスト用の） Session が格納されている場合はそちらを優先する"""
    if test_config is not None and 'sa_session' in test_config:
        return test_config['sa_session']
    engine = create_engine(os.environ['DATABASE_URL'])
    sa_session = scoped_session(sessionmaker(bind=engine))
    return sa_session
