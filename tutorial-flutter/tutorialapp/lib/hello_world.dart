import 'package:flutter/material.dart';

// 拡張機能で⌘⇧P→dart openで調べるとdevtoolが色々使える
// Widget InspectorはLayout見れたりする。便利
void main() {
  // 与えられたWidgetを受け取って、それをツリーのルートに設定する
  // ルートになったウィジェットが画面を覆うように強制される
  runApp(
    const Center(
      child: Text(
        "Hello, world!",
        textDirection: TextDirection.ltr,
      ),
    ),
  );
}

/** 基本的なWidgets
 * Text: 言わずもがな
 * Row, Column: CSSのイメージで横/縦に並べられる
 * Stack: 要素を重ねて置ける(これが知りたかった……)
 * Container: 長方形。BoxDecorationを使うことで色々装飾できる
 */
