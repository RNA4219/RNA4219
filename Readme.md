AIコンダクターの R_N_A です。論文を追うための道具を作ったり、Android端末で言語モデルを動かしたりしています。趣味の創作にもAIを使います。

画面のデザインをAIに任せたくて、美術館のサイトやゲームの画面を調べてもらいました。書体の選び方や余白の取り方について、制作者自身が語った理由を集め、AIが次の画面を作るときに参照できるスキルにしました。[Anything Frontend Art Directionのスキルと作例](https://github.com/RNA4219/anything-frontend-art-direction)

## 技術の代表作 · Quality Evidence Graph

昨日通ったテストを、今日のリリースの根拠にできるか。Quality Evidence Graph（QEG）では、変更内容とそのリスクを、テストと実行記録に結びつけます。何をいつ確かめたのかを後からたどれます。どの記録をリリースの根拠にできるか、その基準もコードと一緒に公開しています。[QEGの実装](https://github.com/RNA4219/quality-evidence-graph) · [判定に使う基準](https://github.com/RNA4219/quality-evidence-graph/blob/main/docs/spec/evidence-acceptance-standard.md)

ログインの手動テストを廃止したいとき、QEGは代わりのテストの記録を調べます。公開例では、同じリスクを確かめる自動テストが5回続けて成功し、手動テストに戻す条件も記録してあります。この例の判定は `go` です。代わりに別の手動テストを指定した例では、自動化の条件を満たさず `DQ-14` で失格になります。[成功例の入力](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/positive-placement-change-retirement) · [失格理由の出力](https://github.com/RNA4219/quality-evidence-graph/blob/v0.4.2/fixtures/negative-retirement-manual-replacement/expected-gate-verdict.json)

<details>
<summary>2つの例の判定図と、Rust実装の計測結果を見る</summary>

<picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/RNA4219/RNA4219/main/assets/qeg-score-mobile.png">
  <img src="./assets/qeg-score.png" alt="上段の5点はE2Eテストが5回続けて成功した記録。括弧は判定基準の3回を示す。下段の切れ目は、後継のテストも手動だったため失格になった箇所。">
</picture>

CLI、Node.js API、GitHub Actionsは、どれも同じRustのコードで判定します。Windows x64で同じサンプルを繰り返し判定し、処理時間を測りました。Node.jsからRustを直接呼ぶ実装に変えると、中央値は11.38 msから0.144 msに短くなりました。[実装と計測条件](https://github.com/RNA4219/quality-evidence-graph/pull/19) · [QEGの設計と使い方](https://github.com/RNA4219/quality-evidence-graph/blob/main/README_JA.md)

</details>

## 論文調査とAndroid実機での開発

- **RanD** で論文やAIニュースを集めています。集めた資料の評価結果はMarkdownで読めます。[RanDで調査を実行する](https://github.com/RNA4219/RanD#readme)
- **LLM Atelier** では、Android端末の中で言語モデルを動かしています。Snapdragon 8 Gen 3を搭載したnubiaの実機で、会話モデルの全43層をNPUに載せ、日本語で応答することを確かめました。[実装とAPK](https://github.com/RNA4219/llm-atelier)

## 音楽と画面 · DEAD AIR FM

[![DEAD AIR FMの選局画面。ピンクの局名と、シアンのジャケットを着たDJ。](https://raw.githubusercontent.com/RNA4219/anything-frontend-art-direction/main/docs/dead-air-fm.webp)](https://rna4219.github.io/anything-frontend-art-direction/examples/dead-air-fm/)

87.9 MHzではダークエレクトロが流れます。92.4 MHzに合わせると、周波数表示が一瞬乱れてアンビエントダブに切り替わります。YuE2で作った3曲とイラストを、一枚のHTMLに収めました。[放送を聴く](https://rna4219.github.io/anything-frontend-art-direction/examples/dead-air-fm/) · [制作に使ったデザインスキル](https://github.com/RNA4219/anything-frontend-art-direction)
