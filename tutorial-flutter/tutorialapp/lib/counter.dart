import 'package:flutter/material.dart';

class Counter extends StatefulWidget {
  // このクラスはstate(状態保持)のための構成。
  // StatefulWidgetから提供されるstateオブジェクトにより、
  // build時に使用される値を保持できる。

  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _counter = 0;

  void _increment() {
    setState(() {
      // setState()を呼び出すことで、FlutterくんにこのStateが更新された事を伝えて
      // build()を再実行させることで表示される値を更新させる事ができる。
      // 逆にいうとsetState()を呼ばずに_counterを更新すると表示は変わらずに内部データだけが
      // 変わった状態にできる。
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // setState()が呼ばれる度にこのbuildも走る。
    // Flutterくんはbuild()再実行の高速化をすごく頑張っているので
    // Widgetのインスタンスを複製したりせずに素直に値を更新すれば良いよって言ってる(多分)。
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        ElevatedButton(
          onPressed: _increment,
          child: const Text('増やす'),
        ),
        const SizedBox(
          width: 16,
        ),
        Text('Count: $_counter'),
      ],
    );
  }
}

void main() {
  runApp(const MaterialApp(
    home: Scaffold(
      body: Center(
        child: Counter(),
      ),
    ),
  ));
}

/** (翻訳文章)
 * なぜStatefulWidgetとStateが別々のオブジェクトなのか不思議に思うかもしれません。
 * Flutterでは、この2つのタイプのオブジェクトは異なるライフサイクルを持ちます。
 * Widgetは一時的なオブジェクトで、現在の状態のアプリケーションのプレゼンテーションを構築するために使用されます。
 * 一方、Stateオブジェクトはbuild()を呼び出す間、永続的に存在し、情報を記憶することができます。
 * 
 * 上の例では、ユーザーからの入力を受け付け、その結果を直接build()メソッドで使用しています。
 * 例えば、あるウィジェットは日付や場所などの特定の情報を収集する目的で複雑なユーザーインターフェースを表示し、
 * 別のウィジェットはその情報を使って全体の表示を変更するかもしれません。
 * 
 * Flutterでは、変更通知はコールバックによってウィジェット階層の「上」に流れ、
 * 現在の状態はプレゼンテーションを行うステートレスウィジェットに「下」に流れます。
 * このフローをリダイレクトする共通の親は、ステートです。
 * 次の少し複雑な例では、これが実際にどのように機能するかを示しています。
 */
