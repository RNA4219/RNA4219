<!-- このREADMEは profile/template.md から生成しています。 -->
<picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/RNA4219/RNA4219/main/assets/qeg-score-mobile.png">
  <img src="./assets/qeg-score.png" alt="R_N_A ｜ AIコンダクター。技術の代表作 Quality Evidence Graph。ログインテストの公開例では、E2Eの5回連続成功と、後継も手動のため失格となったケースを比較できます。">
</picture>

**[Quality Evidence Graph の実装を開く](https://github.com/RNA4219/quality-evidence-graph)** · [成功例の入力](https://github.com/RNA4219/quality-evidence-graph/tree/v0.4.2/fixtures/positive-placement-change-retirement) · [失格理由の出力](https://github.com/RNA4219/quality-evidence-graph/blob/v0.4.2/fixtures/negative-retirement-manual-replacement/expected-gate-verdict.json)

**AIコンダクターのR_N_Aです。** 論文を調べるときも、曲の流れるWeb作品を作るときも、どのAIに何を任せ、何を自分で確かめるかを決めています。必要な道具は自分で作ります。

## 技術の代表作 · Quality Evidence Graph

**ログインの手動テストを、いつ廃止していいか。** QEGは、変更・リスク・テスト・実行記録を結び、リリースの可否とその理由を返します。[QEGの設計と使い方](https://github.com/RNA4219/quality-evidence-graph/blob/main/README_JA.md)

表紙の譜面は、QEGの公開サンプルを図にしたものです。上段の一点がE2Eテストの成功1回、括弧が基準の3回です。同じリスクを検証して5回連続で成功し、手動に戻す条件も記録された例は `go`。下段は、後継テストの実体がまだ手動だった例です。自動化の根拠が途切れ、`DQ-14` で失格になります。

判定ロジックはRustで実装し、CLI、Node.js API、GitHub Actionsで共有しています。Node.jsからRustを直接呼び出すようにすると、Windows x64で同じサンプルを繰り返し判定したときの中央値は **11.38 ms → 0.144 ms** になりました。[実装と計測条件](https://github.com/RNA4219/quality-evidence-graph/pull/19)

## 最近のリリース

{{releases}}

## 研究と制作

**RanD** では、論文やAIニュースの調査から知見の整理、評価、通知までをつないでいます。一度実行すると、調査結果をMarkdownで読めます。[調査を実行する](https://github.com/RNA4219/RanD#readme)

**LLM Atelier** は、Android端末で動くローカルAIアプリです。Snapdragon 8 Gen 3搭載のnubia実機で、会話モデルの全43層をNPUに載せ、日本語の応答を確かめました。[実装とAPK](https://github.com/RNA4219/llm-atelier)

**DEAD AIR FM** は、選局すると周波数表示が乱れ、次の曲が流れる架空の深夜ラジオ局。自作のデザインスキルとMotion Atlasを使い、YuE2で作った3曲とイラストを1枚のHTMLに収めました。[ブラウザーで選局して聴く](https://rna4219.github.io/anything-frontend-art-direction/examples/dead-air-fm/) · [制作に使ったスキル](https://github.com/RNA4219/anything-frontend-art-direction)

<a href="https://rna4219.github.io/anything-frontend-art-direction/examples/dead-air-fm/"><img src="https://raw.githubusercontent.com/RNA4219/anything-frontend-art-direction/main/docs/dead-air-fm.webp" width="500" alt="DEAD AIR FMを開く。ヘッドホンを着けたDJと選局画面。"></a>
