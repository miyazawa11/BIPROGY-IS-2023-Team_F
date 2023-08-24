# BIPROGY-IS-2023-Team_F/BackEnd
このプロジェクトは園児の出欠管理のAPIを提供します。
APIリファレンスは[こちら](https://github.com/tsyu12345/BIPROGY-IS-2023-Team_F/blob/feature/B-readme/BackEnd/api_doc/api_doc.md)。
## Requirements
Python version: 3.9.6

## Setup
仮想環境を作成してください。
```shell
python -m venv venv
```
仮想環境を有効化してください。
Windowsの場合
```shell
./venv/Scripts/activate
```

Macの場合
```shell
source venv/bin/activate
```

必要なPythonライブラリをインストールしてください。
```shell
pip install -r requirements.txt
```

## Flaskを起動する

データベースの初期化をする。
```shell
flask --app attendance init-db
```
`instance/attendance.db`ができます。

Flaskを起動する。
```
flask --app attendance run
```
