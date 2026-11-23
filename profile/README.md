# プロフィールを更新する

公開先は [github.com/RNA4219](https://github.com/RNA4219) です。本文は [template.md](template.md)、リリースの掲載対象は [update_readme.py](update_readme.py) の `PROJECTS` で編集します。生成した `Readme.md` はリポジトリ直下に置きます。

## 本文とリリース

テンプレートか生成スクリプトをmainへ反映すると、GitHub Actionsが掲載作品の最新正式リリースを取得し、公開日の新しい順に並べます。毎日04:17（日本時間）にも実行を予定しています。手動更新は [Actionsの「Run workflow」](https://github.com/RNA4219/RNA4219/actions/workflows/profile.yml) から実行できます。内容が変わった回だけコミットします。取得に失敗した場合は、前回のREADMEを保持します。

ローカルで本文を生成するには、リポジトリのルートで `python profile/update_readme.py` を実行します。Python 3.9以上の標準ライブラリを使います。

## 表紙を組み直す

譜面の出典はQEG v0.4.2の[手動テストを廃止できる例](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/positive-placement-change-retirement)と[後継も手動だった例](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/negative-retirement-manual-replacement)です。連続成功回数・判定基準・失格理由を同じ版から取得します。この例の版は固定し、配布中の最新版は本文で更新します。

表紙を変更するときは、Python 3.11とPillow 12.1.1を用意し、`python profile/render_cover.py` を実行します。出力は `assets/qeg-score.png` と `assets/qeg-score-mobile.png` です。日本語の説明、根拠へのリンク、画像の代替テキストはテンプレートにあります。

## 意匠の根拠

[Anything Frontend Art Direction](https://github.com/RNA4219/anything-frontend-art-direction) の手順で「代表作と判定理由を見つけ、その実装を開く」を入口の目的にしました。CINRAの青森県立美術館サイト制作記録では、固有の文字をメインナビゲーションに用いています。掲載された狭幅画面で大きな「美術館に行く」の直下に案内リンクが並ぶ構成を確認し、作品名と実装・入力・出力へのリンクを隣接させました。[制作記録](https://www.cinra.co.jp/work/aomorikenbi)

山崎晴太郎『余白のための楽譜 #01』では、演奏中の音と音の断片が別々の画面に投影されます。制作写真では中央と左右で異なる形が見えます。ここから、実データで形を決める考え方を取り入れました。QEGの五つの点は成功5回、下の括弧は基準3回、切れ目は自動化の根拠が欠けた箇所です。[作者の解説と展示写真](https://seiyamazaki.com/artworks/music-for-the-margin/)

写真を表紙にして判定を次の図で見せる案と、作品名と判定を一枚に組む案を同じ本文で比較しました。後者では、スマートフォンのREADME先頭でも作品名と二つの判定がそろいます。点を外すと成功回数を数えにくくなるため、譜面には点を残しました。

作品名はInstrument Serifを使っています。同じ大きさでTimes New Romanと組み比べると字幅が狭く、作品名の隣に判定を並べる余白が取れました。作者名と判定のラベルはBarlow Condensedです。同梱書体の出典とライセンスは [Instrument Serif](https://github.com/google/fonts/tree/main/ofl/instrumentserif)・[利用条件](fonts/InstrumentSerif-OFL.txt)、[Barlow Condensed](https://github.com/google/fonts/tree/main/ofl/barlowcondensed)・[利用条件](fonts/BarlowCondensed-OFL.txt)を参照してください。
