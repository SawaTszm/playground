import 'package:flutter/material.dart';

class CounterDisplay extends StatelessWidget {
  const CounterDisplay({required this.count, super.key});

  final int count;

  @override
  Widget build(BuildContext context) {
    return Text('Count: $count');
  }
}

class CounterIncrementor extends StatelessWidget {
  const CounterIncrementor({required this.onPressed, super.key});

  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(onPressed: onPressed, child: const Text('増やす'));
  }
}

class Counter extends StatefulWidget {
  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _counter = 0;

  void _increment() {
    setState(
      () {
        ++_counter;
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        CounterIncrementor(
          onPressed: _increment,
        ),
        const SizedBox(
          width: 16,
        ),
        CounterDisplay(count: _counter),
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
  )));
}

/**
 * ちょっと流れがわかった気がする……？
 * イベント発火(今回でいうCounterIncrementor(ボタン)が押されたとか)は下のウィジェットから上へ上がってきて、
 * そのイベントに沿って上のStatefulWidgetでsetState()を呼び出した上で値を更新したら、それを検知して
 * stateの値を使っている下の階層のウィジェットでrebuildが走る形。
 */

/**(翻訳文章)
 * 2つの新しいステートレスウィジェットが作成され、
 * カウンターの表示 (CounterDisplay) とカウンターの変更 (CounterIncrementor) が
 * きれいに分離されていることに注目してください。
 * 
 * 最終的な結果は前の例と同じですが、責任の分離により、親ウィジェットの単純性を維持したまま、
 * 個々のウィジェットでより複雑な機能をカプセル化することができます。
 */
