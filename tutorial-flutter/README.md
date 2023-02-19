# flutter-tutorial

## やったこと

### インストール

バージョン管理に[fvm](https://fvm.app/)を使います。

```zsh
brew tap leoafarias/fvm
brew install fvm
fvm global stable
```

### flutter

これから触ろう……と思ったところで[flet](https://flet.dev/)なるものを教えてもらったので、先にそっちを触ると思います。  

fletから帰ってきた: `Container.decoration`が(少なくとも現時点では)定義できなさそうで、サッとpythonでユーティリティアプリ系とか作りたいなと思った時には凄く良い選択肢になるけど、結局込み入ったところまで入っていった結果「flutterで実装されたあれこれがfletにはまだない」状態になって歯痒くなるなら最初からflutter(Dart)本体を勉強しながら触った方が良さそうだなと思ったので帰ってきました。  
ただ、pythonで触り始められたことで言語障壁がほぼない状態でflutterの構造への解像度を上げられたのは本当にありがたかったです。Thanks flet...  

### プロジェクト作成

```zsh
flutter create -i swift -a kotlin testapp
# All done!
# In order to run your application, type:
# 
#   $ cd testapp
#   $ flutter run
# 
# Your application code is in testapp/lib/main.dart.

cd testapp
flutter run
# ウィンドウが立ち上がります
```
