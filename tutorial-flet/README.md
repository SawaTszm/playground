# tutorial-flet

## fletとは

[flet](https://flet.dev/docs/)

pythonでflutterアプリを実装するためのフレームワーク。  
(書いてる時点ではpythonで、を売りにしてるしガイドもpythonだけだけど、今後複数言語対応を見据えてる様子)

## 使い方

```zsh
pip install flet
```

後はフレームワークの仕様に沿って書いていって、`python <file名>.py`するだけ。

## memo

### 状態変化に対する再レンダリング(ビルド?)

> Flet implements imperative UI model where you "manually" build application UI with stateful controls and then mutate it by updating control properties. Flutter implements declarative model where UI is automatically re-built on application data changes. Managing application state in modern frontend applications is inherently complex task and Flet's "old-school" approach could be more attractive to programmers without frontend experience.

Flutterはデータが更新されたら自動でリビルドしてくれるけど、Fletは完全に手動。  
一見短所っぽいけど、だからこそフロントエンドに馴染みのないバックエンドエンジニアには受け入れられやすいんじゃないか。(ふんわり訳)  

(これをみると規模感によっては素直にflutterを使った方が良さそうと思えてくる)

### コントローラー

Fletのコントローラを制御するためにはオブジェクトへの参照(変数)を持っておく必要がある。  
言い換えると、「実際に使われる時にどういう条件で生成された何かを確認することが(エディタの定義参照を見る以外では)難しい」ということ。  
（どんな言語でもある問題だと思うけど、状態遷移が度々挟まるFletの書き方だと尚更）

なので、Fletは、コントロールへの参照を定義し、イベントハンドラでその参照を使用し、後でツリーを構築しながら実際のコントロールに参照を設定することができる`Ref`ユーティリティクラスを提供している。このアイデアはReactからきている（！）。  
全てのFletコントロールがref プロパティを持ってる。

ただ、参照の前に`.current`が付き纏うことになるので若干冗長にはなる。使用はお好みで、って書いてある。  
