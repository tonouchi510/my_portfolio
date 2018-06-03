# 備忘録
コーディング中に困った事とその解決策を残していく

## myapps/mnist
### template内で配列にランダムアクセスできない
- 独自のtemplateタグを作る（templatetagsフォルダ内）

### モデルフォームに用意した入力項目がDB登録に必要な項目に足りないとき
- post後，サーバ側の処理で，足りない項目を補完した上で，新たにモデルフォームを作成しなおし，それをDBに登録という形で対処できる。
- view内で該当処理を記載

### canvasに書いた絵をサーバ側に画像として保存したい
- formのsubmit時にPOSTデータを追加するスクリプトを書くことで対応した
  - http://raining.bear-life.com/javascript/javascript%E3%81%A7post%E3%81%AE%E5%80%A4%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B

### canvasに書いた絵をサーバ側に画像として保存したい(その2)
- submitでページ遷移したくなかった
- ajaxを使えば遷移せずPOST通信で特定部分だけを変更できる
  - https://teratail.com/questions/128895
  - https://qiita.com/zakiyamaaaaa/items/bdda422db2ccbaea60d9
- これに関しても，templateのmnist.htmlで記載
