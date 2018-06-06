# My-Portfolio
Djangoを使ったWebアプリケーション作成の練習用リポジトリ

これまで自分が作ってきたDeepLearning系の実装を，作品集として見やすくまとめたWebアプリケーションを作成する


## 利用フレームワーク
- Django2.0
- Bootstrap4
- Keras2.1.5
- Tensorflow1.5.1

## 作品集
とりあえず以下のものをwebアプリケーション化予定

### Digit Recognition（作成済み）
MNISTという手書き数字認識用のデータセット（28x28ピクセル）を使用

- 精度:99.4%
- 画面上に手書きした数字を識別させるアプリケーションを作成
- 入力された数字は再学習用に新たなデータセットとして登録する
- 直近の8例の識別結果を例として表示

### cifar-10 Recognition
cifar-10という10クラスの一般物体認識用データセット(32x32x3)を使用

- 精度:90％程度
- 今のところアプリケーション要素は考えられていない


### Neural Machine Translation
英日翻訳用のデータセットを使用

- BLEU4精度:0.2程度
- 基本的なseq2seqに，attentionを加えたモデルを使用
- 入力した英文から日本語訳を出力するアプリケーションを実装予定
- ビームサーチの出力も同時に可視化する
- 精度はまだ十分でないため，今後AIAYN等のモデルに改良予定

### Capsule Network
- 昨年話題になったCapsNetの検証結果を表示
- また，続編についても検証予定

### Meteor Search

- Deep Analyticsのコンペ（Meteor-Search）に挑戦した結果を記載
- 時系列性は単純に3Dconvで対応させた

### Caption Generation
MSCOCOのデータセットを利用

- ドラッグドロップした任意の画像のキャプションを出力するアプリケーションを実装予定
- 実装は単純なAttention とCNNを使ったモデル

### GAN

- Conditional GANで指定した画像を生成するアプリケーションを作成予定
- 現状はMNIST，Cifar-10のみ
- 今後はGANでの補完も試したい

### DQN
- cartpol等の基本的な強化学習用タスクの学習過程を表示する予定

### Face(未実装)
https://github.com/HCIILAB/SCUT-FBP5500-Database-Release

このデータセット使って何か作る予定

