# プロフィールを更新する

公開先は [github.com/RNA4219](https://github.com/RNA4219) です。本文は [template.md](template.md)、リリースの掲載対象は [update_readme.py](update_readme.py) の `PROJECTS` で編集します。生成した `Readme.md` はリポジトリ直下に置きます。

## 本文とリリース

テンプレートか生成スクリプトをmainへ反映すると、GitHub Actionsが掲載作品の最新正式リリースを取得し、公開日の新しい順に並べます。毎日04:17（日本時間）にも実行を予定しています。手動更新は [Actionsの「Run workflow」](https://github.com/RNA4219/RNA4219/actions/workflows/profile.yml) から実行できます。内容が変わった回だけコミットします。取得に失敗した場合は、前回のREADMEを保持します。

ローカルで本文を生成するには、リポジトリのルートで `python profile/update_readme.py` を実行します。Python 3.9以上の標準ライブラリを使います。

## 表紙と判定図の編集

表紙の原画は [press-hand.webp](press-hand.webp) です。ImageGenで作った、紙テープの記録に赤鉛筆を入れる手の挿絵です。文字と絵の位置、名前の二本の下線の色は [render_sleeve.py](render_sleeve.py) で編集します。

Python 3.11とPillow 12.1.1を用意し、リポジトリのルートで次を実行します。

```sh
python profile/render_sleeve.py
```

PC用の `assets/rna-sleeve.webp` と狭幅用の `assets/rna-sleeve-mobile.webp` ができます。生成画像もコミットしてください。書体は [Instrument Serif](https://github.com/google/fonts/tree/main/ofl/instrumentserif)・[利用条件](fonts/InstrumentSerif-OFL.txt) と [Barlow Condensed](https://github.com/google/fonts/tree/main/ofl/barlowcondensed)・[利用条件](fonts/BarlowCondensed-OFL.txt) を同梱しています。画像を表示できないときも名前・肩書き・二つのリンクを本文から読めます。

QEGの節を開くと表示される譜面は別の図です。`python profile/render_cover.py` を実行すると、QEG v0.4.2の[成功例](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/positive-placement-change-retirement)と[失格例](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/negative-retirement-manual-replacement)からPC用と狭幅用のPNGを生成します。事例の版は固定しています。

## 意匠の根拠

初めて訪れた人がR_N_Aの仕事を一文でつかみ、技術に興味があればQEGの実装を、制作に興味があればラジオを開ける順にしました。QEGは技術の代表作として本文の最初に置きました。

- **本人をどう紹介するか。** Maggie Appletonは、自身の仕事をデザイン・人類学・開発にまたがるものと説明しています。本人のサイトを開くと、最も大きな一文では何を作る人かを動詞で語り、肩書きはその下にあります。ここから、名前と「AIに何を任せ、何を自分で確かめるか」を先に読める構成を取り入れました。[トップ](https://maggieappleton.com/)・[本人の説明](https://maggieappleton.com/about)
- **色をどこに使うか。** 作者自身のDEAD AIR FMでは、ヘッドホンのコードと局名がピンク、ジャケットと再生操作がシアンです。公開画面と制作記録を照合しました。表紙では赤鉛筆の朱を、R_N_Aの名前に元からある二本の下線に拾っています。紙テープに赤を入れる仕草には、出力を自分で確かめる姿を重ねました。[実際の放送画面](https://rna4219.github.io/anything-frontend-art-direction/examples/dead-air-fm/)・[制作記録](https://github.com/RNA4219/anything-frontend-art-direction#readme)
- **名前をどう組むか。** モバイル表紙の同じ位置に、同じ115pxで `R_N_A` を組みました。Times New Romanでは幅359pxになり、末尾のAが挿絵にかかります。Instrument Serifは260pxで、名前を大きくしながら黒地に余白を残せるため採用しました。
- **採用と棄却。** 同じ名前・肩書き・二作品・本文で、手を大きく置く見開きと、作品名を二段に並べて挿絵を添える目録を、GitHubの本文幅846pxと308pxで比較しました。目録は二作を拾いやすく、見開きは狭幅でも鉛筆の先と紙の赤丸が残ります。見開きを採り、作品を選ぶ操作には直下のテキストリンクを使いました。名前の下線を紙色に戻した版でも情報は同じですが、筆先の朱が名前へ続く印象が消えるため、少しずらした朱の重ねを残しています。
