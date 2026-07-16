<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:141e30,100:243b55&height=200&section=header&text=AI%20Conductor&fontSize=36&fontAlignY=40&fontColor=ffffff&animation=fadeIn"
    alt="AI Conductor"
  />
</p>

<h3 align="center">Autonomous R&amp;D Systems Engineer / Harness Engineer</h3>

<p align="center">
  Agent tooling · Verification harnesses · Control planes · Quality infrastructure
</p>

## About

AIを活用した研究・開発のための実行基盤、検証ハーネス、品質ツールを設計・実装しています。

QA / SDETを土台に、曖昧な要求を実行可能なワークフローへ落とし込み、コード分析、テスト、自動化、結果整理までを接続することが主な関心領域です。公開リポジトリでは、実際の開発で再利用できる単位へ分割したツールと運用資産を公開しています。

**AI Conductor** は、複数のAI、ツール、工程を目的に合わせて編成し、継続的な成果へつなげる立場を表す、自分なりの呼称です。

I build practical infrastructure for AI-assisted R&D: agent tooling, verification harnesses, control planes, and quality workflows.

## Eight Repositories, One Engineering Stack

以下は独立したデモの寄せ集めではなく、調査・要求整理から検証と品質判断までを支えるツール群です。

<p align="center">
  <a href="https://github.com/RNA4219/RanD"><b>RanD</b></a>
  &nbsp;→&nbsp;
  <a href="https://github.com/RNA4219/code-to-gate"><b>code-to-gate</b></a>
  &nbsp;→&nbsp;
  <a href="https://github.com/RNA4219/harness-auto-test-evidence"><b>HATE</b></a>
  &nbsp;→&nbsp;
  <a href="https://github.com/RNA4219/manual-bb-test-harness"><b>manual-bb</b></a>
  &nbsp;→&nbsp;
  <a href="https://github.com/RNA4219/quality-evidence-graph"><b>QEG</b></a>
</p>

<p align="center">
  <sub>Research &amp; Requirements → Code Analysis → Automated Testing → Manual Acceptance → Quality Analysis</sub>
</p>

- [domain-lakda-runner](https://github.com/RNA4219/domain-lakda-runner) supplies runtime exploration and reproducible execution results.
- [workflow-cookbook](https://github.com/RNA4219/workflow-cookbook) supplies reusable workflows, acceptance assets, and CI practices across the stack.
- [shipyard-cp](https://github.com/RNA4219/shipyard-cp) coordinates agent-assisted work across planning, development, acceptance, integration, and publishing.

| Layer | Repository | Responsibility |
|---|---|---|
| Research & Requirements | [RanD](https://github.com/RNA4219/RanD) | Research, hypothesis formation, requirement discovery, and acceptance framing. |
| Workflow Assets | [workflow-cookbook](https://github.com/RNA4219/workflow-cookbook) | Task Seeds, acceptance workflows, reusable CI, and development practices. |
| Agent Operations | [shipyard-cp](https://github.com/RNA4219/shipyard-cp) | Coordinates agent-assisted work across planning, development, acceptance, integration, and publishing. |
| Code Analysis | [code-to-gate](https://github.com/RNA4219/code-to-gate) | Converts source changes, static signals, architecture checks, and repository risk into reviewable results. |
| Runtime Exploration | [domain-lakda-runner](https://github.com/RNA4219/domain-lakda-runner) | Explores software behavior and produces reproducible runtime results. |
| Automated Testing | [harness-auto-test-evidence](https://github.com/RNA4219/harness-auto-test-evidence) | Normalizes automated test results for downstream use. |
| Manual Acceptance | [manual-bb-test-harness](https://github.com/RNA4219/manual-bb-test-harness) | Supports risk-based manual black-box testing and acceptance review. |
| Quality Analysis | [quality-evidence-graph](https://github.com/RNA4219/quality-evidence-graph) | Connects requirements, risks, changes, tests, and review results for quality assessment. |

## Current Work

I am continuing to integrate and extend these tools through private R&D projects.

プロジェクト固有の構成、運用方式、進捗詳細は公開せず、単独でも再利用価値を持つ部分だけをOSSとして切り出しています。

## Open Source Approach

- Build from concrete development and QA problems.
- Keep each repository independently understandable and usable.
- Include tests, examples, documentation, and CI with the implementation.
- Separate reusable public components from project-specific integration.
- Prefer working software and reproducible examples over broad claims.

## Focus Areas

`Autonomous R&D Systems` · `Agent Tooling` · `Harness Engineering` · `Control Planes` · `Quality Infrastructure` · `Developer Workflows` · `Test Automation` · `LLM-native Development`

## Core Stack

- **Languages:** Python, TypeScript / JavaScript, SQL, Bash
- **Interfaces & Data:** JSON Schema, SQLite, REST APIs, CLI tools, structured outputs
- **QA & Automation:** pytest, Playwright, Airtest, Jest / Vitest, coverage, CodeQL, GitHub Actions
- **Runtime & Infrastructure:** Docker / OCI containers, devcontainers, async processing, local-first tooling
- **LLM Systems:** OpenAI-compatible APIs, local LLMs, llama.cpp / Ollama, routing and orchestration tooling
