# プロフィールを更新する

公開先は [github.com/RNA4219](https://github.com/RNA4219) です。本文は [Readme.md](../Readme.md) を直接編集してmainに反映します。固定リポジトリはGitHubプロフィールの「Customize your pins」で選びます。

## 冒頭の波形

冒頭の画像を押すと、自作ラジオ「DEAD AIR FM」が開きます。波形は87.9 MHzの「Midnight Circuit」から、3小節目と4小節目を切り出したものです。針は曲のテンポ（128 BPM）に合わせて3.75秒で一周します。端末で動きを減らす設定にしている場合は静止画を表示します。

作業台に上がる湯気の横で名前が読める [skulitomのプロフィール](https://github.com/skulitom) と、リポジトリを放送中の曲に見立てた [OthmanAdiのCommit FM](https://github.com/OthmanAdi/commit-fm) を参考にしました。名前は固定し、曲に合わせて針とその周囲の波形だけが動きます。

[音源を含むHTML](https://github.com/RNA4219/anything-frontend-art-direction/blob/f39c407d2f9d79dd931023abd61dd53e81945fb6/examples/dead-air-fm/index.html) を使って画像を作り直せます。PythonにNumPyとPillowをインストールし、FFmpegをパスに通してから `python profile/render_radio.py <index.htmlのパス>` を実行してください。

## 旧バナーの制作記録と判定図の編集

表紙の[光跡の原画](moss-signal.webp)はDGX Spark上のComfyUIでMOSS Image SFTを使って生成しました。[生成に使ったAPI形式のワークフロー](moss-signal-api.json)にはプロンプト、モデル名、seed（421937）、サイズ（1408×608）、サンプリング条件を収めています。同じモデルのあるComfyUIの `/prompt` にこのJSONをPOSTすると生成できます。名前と肩書きは [render_sleeve.py](render_sleeve.py) で後から組みます。

Python 3.11とPillow 12.1.1を用意し、リポジトリのルートで次を実行します。

```sh
python profile/render_sleeve.py
```

PC用の `assets/rna-sleeve.webp` と狭幅用の `assets/rna-sleeve-mobile.webp` ができます。生成画像もコミットしてください。書体は [Instrument Serif](https://github.com/google/fonts/tree/main/ofl/instrumentserif)・[利用条件](fonts/InstrumentSerif-OFL.txt) と [Barlow Condensed](https://github.com/google/fonts/tree/main/ofl/barlowcondensed)・[利用条件](fonts/BarlowCondensed-OFL.txt) を同梱しています。画像を表示できないときも名前・肩書き・二つのリンクを本文から読めます。

QEGの節を開くと表示される譜面は別の図です。`python profile/render_cover.py` を実行すると、QEG v0.4.2の[成功例](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/positive-placement-change-retirement)と[失格例](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/negative-retirement-manual-replacement)からPC用と狭幅用のPNGを生成します。事例の版は固定しています。

## 意匠の根拠

冒頭では論文調査・ローカルAI・音楽に触れ、デザインスキルの投稿から来た人にはスキルと作例へのリンクを置きます。最初の見出しは技術の代表作QEGです。実装と証拠の採用基準へ進め、その下に調査・実機開発と音楽作品が続きます。

- **本人をどう紹介するか。** Maggie Appletonは、自身の仕事をデザイン・人類学・開発にまたがるものと説明しています。本人のサイトを開くと、最も大きな一文では何を作る人かを動詞で語り、肩書きはその下にあります。ここから、名前と普段作っているものを先に読める構成を取り入れました。[トップ](https://maggieappleton.com/)・[本人の説明](https://maggieappleton.com/about)
- **光と文字をどう結ぶか。** Robert Henkeの『Lumière』では、一つの音と光の図形を対応させています。作者の公演写真を手がかりに、複数の線がひとつの形を作る構図を試しました。生成画の青白い線と同じ色を、名前の二本の下線に置いています。[作者の説明と公演写真](https://roberthenke.com/concerts/lumiere.html)
- **名前をどう組むか。** モバイル表紙の同じ位置に、同じ115pxで `R_N_A` を組みました。Times New Romanでは幅359pxになり、末尾のAが挿絵にかかります。Instrument Serifは260pxで、名前を大きくしながら黒地に余白を残せるため採用しました。
- **三案の比較。** 音響機器の配線、光の軌跡、演算モジュールの分解図を、同じ名前と肩書きで比較しました。採用した光跡は線が右で束になる部分を残して切り出し、PC用は1408×184px、狭幅用は768×148pxの帯に収めています。
