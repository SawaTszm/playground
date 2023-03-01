import 'package:flutter/material.dart';

void main() {
  runApp(
    const MaterialApp(
      title: 'Flutter Tutorial',
      home: TutorialHome(),
    ),
  );
}

class TutorialHome extends StatelessWidget {
  const TutorialHome({super.key});

  @override
  Widget build(BuildContext context) {
    // Scaffold is a layout for the major Material Components
    // rootの要素としてよく使われて、それぞれのウィジェットが引数として渡される。
    return Scaffold(
      appBar: AppBar(
          leading: const IconButton(
            onPressed: null,
            tooltip: 'Navigation menu',
            icon: Icon(Icons.menu),
          ),
          title: const Text('Example title'),
          actions: const [
            IconButton(
                onPressed: null, tooltip: 'Search', icon: Icon(Icons.search))
          ]),
      // body is the majority of the screen.
      body: const Center(
        child: Text('Hello, world!'),
      ),
      floatingActionButton: const FloatingActionButton(
          onPressed: null, tooltip: 'Add', child: Icon(Icons.add)),
    );
  }
}

/**Materialは、Flutterに含まれる2つのバンドルデザインの1つ。
 * iOS中心のデザインを作成するには、独自のバージョンのCupertinoAppとCupertinoNavigationBarを含む、
 * Cupertinoコンポーネントパッケージを参照するといい(らしい)。
 */

/**
 * StatelessWidgetは親ウィジェットから引数を受け取り、それを最終メンバ変数に格納して、
 * build()が要求された時にその格納された値を使用して子ウィジェットの引数を代入する。
 * ユーザの入力に反応するなど、より複雑な反応をするためには状態を保持するStateオブジェクトを生成できる
 * StatefullWidgetを使う必要がある。
 */
