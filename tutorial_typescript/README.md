# tutorial_typescript

[仕事ですぐに使えるTypeScript](https://future-architect.github.io/typescript-guide/)を参考にしています。  
前提知識の構築として、[フロントエンドウェブ開発者 - MDN](https://developer.mozilla.org/ja/docs/Learn/Front-end_web_developer)の内容も含みます。

## 初めに

### 環境作成

```bash
$npm init -y
# package.jsonが生成される
# "private: true"を追記(一応)
$npm install --save-dev ts-node typescript
```

### インストールしたコマンドを実行する

```bash
$npx ts-node
> # REPL
```

`scripts`に登録する方法もある。

```bash
$npm run start
> tutorial_typescript@1.0.0 start
> ts-node
```

### TypeScriptの環境を設定する

```bash
$npx tsc --init
> message TS6071: Successfully created a tsconfig.json file.
```


## 参照

[セレクターのリファレンス表](https://developer.mozilla.org/ja/docs/Learn/CSS/Building_blocks/Selectors#reference_table_of_selectors)  
[cssの値と単位](https://developer.mozilla.org/ja/docs/Learn/CSS/Building_blocks/Values_and_units)  
