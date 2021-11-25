flask-seed
=======================================


SETUP
---------------------------------------

### .env ファイルの準備

パスワードを記載するためバージョン管理システムに登録しないファイル `.env` を作成します。

```sh
$ touch .env
```

`.env` ファイルの中に `POSTGRES_PASSWORD` を1行加えてください
```
POSTGRES_PASSWORD=何かパスワードを書いてください
```

### イメージのビルド

```sh
$ docker compose build
```

TEST
---------------------------------------

### テストモードのインタラクティブシェルに入る

```sh
$ docker compose run --rm web_test bash
```

### テストの実行

```sh
pytest tests/
```

MIGRATION
---------------------------------------

操作する際にはインタラクティブシェルに入る

- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/index.html)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)


### migration ファイルの生成

```sh
$ alembic revision --autogenerate -m 'name of the migration'
```

### migration の実行

```sh
$ alembic upgrade head
```

### バージョンを一つ戻す

```sh
$ alembic downgrade -1
```

### バージョン履歴を見る

```sh
$ alembic history --verbose
```

### 生成される差分があるかチェック

```sh
$ alembic-autogen-check --config alembic.ini
```


DEV
=======================

### 開発サーバ起動

```sh
$ docker compose up
```
Ctrl-C で終了


### 開発モードのインタラクティブシェルに入る

```sh
$ docker compose run --rm web bash
```
