# Osawa_tech_4.2
4年後期テクニカルレポート

提案手法の実装に用いたコードがそれぞれ含まれている，

# Headフォルダ - クラスタヘッドのコード
## main.py
### connect_esp_wifi()
ESP32のWi-Fiに接続する．
### receiving()
ソケット通信でデータを受信する．このコードではbuffer_sizeでチャンク分けされたデータを受け取る，
### toServer()
データをサーバーに送信する．サーバーのurlを指定して，HTTPリクエストのPOSTで送信している．ステータスコードが201なら送信成功として'Data saved sucessfully'メッセージを返す．それ以外のステータスコードであれば送信失敗として'Failed to save data'メッセージを返す．
### logs()
rtcモジュールを用いてデバイスが稼働していた時間を記録する．

# Memberフォルダ - クラスターメンバーのコード

# Monitorフォルダ - INAを動かすコード

