# R_N_A ｜ AIコンダクター

作りたいものに合わせてAIと道具を選び、どの仕事を任せるか、どこで自分が確かめるかを決めています。工程をつなぐ道具や、結果を検証する仕組みも自分で作ります。

## 技術の代表作　Quality Evidence Graph（QEG）

テストが通ったとき、その結果を根拠に「この変更はリリースしてよい」と言えるのは、どんなときか。QEGは、要求、コードの変更、リスク、テスト、実行記録を一つのグラフに結び、リリースの可否とその理由を示すツールです。[QEGの概要と使い方](https://github.com/RNA4219/quality-evidence-graph/blob/main/README_JA.md)

たとえば、ログインの手動テストをいつ廃止できるか。公開例では、後継のE2Eテストが同じリスクをカバーし、基準の3回を超えて5回連続で成功しています。手動テストに戻す条件も記録され、判定は `go` です。後継として登録したテストの実体が手動のままなら、QEGはその矛盾を指摘し、`disqualified` を返します。[廃止を認める例](https://github.com/RNA4219/quality-evidence-graph/tree/main/fixtures/positive-placement-change-retirement) · [矛盾を検出する例](https://github.com/RNA4219/quality-evidence-graph/blob/main/fixtures/negative-retirement-manual-replacement/expected-gate-verdict.json)

判定ロジックはRustで実装し、CLI、Node.js API、GitHub Actionsで共有しています。Node.jsからRustを直接呼び出すようにしたところ、Windows x64で同じサンプルを繰り返し判定した際の中央値は、1回あたり11.38 msから0.144 msになりました。[実装と計測条件](https://github.com/RNA4219/quality-evidence-graph/pull/19)

## ほかに作っているもの

- **RanD** は、論文やAIニュースの調査から、得られた知見の整理、評価、通知までをつなぐツールです。調査を1回実行すると、結果をMarkdownのレポートで読めます。[実装と実行例](https://github.com/RNA4219/RanD)
- **LLM Atelier** は、Android端末で動くローカルAIアプリです。Snapdragon 8 Gen 3搭載のnubia実機で、会話モデルの全43層をNPUに載せ、日本語で返事が来ることを確かめました。[実装とAPK](https://github.com/RNA4219/llm-atelier)
- **DEAD AIR FM** は、架空の深夜ラジオ局です。選局すると周波数表示が一瞬乱れ、次の曲に切り替わります。YuE2で生成した3曲とイラストを1枚のHTMLに収めました。[ブラウザーで選局して聴く](https://rna4219.github.io/anything-frontend-art-direction/examples/dead-air-fm/)
