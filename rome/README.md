# rome

## what's rome?

フロントエンドのformatter, linter, bundlerなど、これまで多くの選択肢があったものを一つにまとめる思想で作られた(作っている)パッケージ。  
(触った時点ではまだlinterはサポートしてない？)

## install

```zsh
pnpm add -D rome@next
```

### やったこと(備忘録)

anyenv→nodenv経由でバージョン管理しているnodeの更新。  
[anyenv update](https://github.com/znz/anyenv-update)が便利だった。

## scripts

```json
// package.json
    "scripts": {
        "format": "rome format ."
    },
```

これで`pnpm format`が使えるようになる。(yarnでもnpmでも同様)

## formatter

VS Code extensionがある。
