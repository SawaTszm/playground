// https://dart.dev/samples
// 各項目から詳しいlanguage tutorialに飛べる。

// mian()が必ず必要。consoleに何かを表示する場合はprint()を使う。
void main() {
  print('Hello, World!');
}

// 型推論のおかげで(!)ほとんどの変数は明示的な型を必要としない
// https://dart.dev/guides/language/language-tour#variables
var name = 'hoge taro';
var year = 2023;
var antennaDiameter = 3.7;
var flybyObjects = ['Jupiter', 'Saturn', 'Uranus', 'Neptune'];
var image = {
  'tags': ['saturn'],
  'url': '//path/to/saturn.jpg'
};

// この辺は普通に使える。assert?も使える
// https://dart.dev/guides/language/language-tour#control-flow-statements
if (year >= 2001) {
  print('21st century');
} else if (year >= 1901) {
  print('20th century');
}

for (final object in flybyObjects) {
  print(object);
}

for (int month = 1; month <= 12; month++) {
  print(month);
}

while (year < 2016) {
  year += 1;
}

// 関数の引数/戻り値の型を書くことが推奨されてる。(def XXX() じゃないのでぱっと見に注意)
int fibonacci(int n) {
  if (n == 0 || n == 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

var result = fibonacci(20);

// arrow関数
flybyObjects.where((name) => name.contains('turn')).forEach(print);

// これは普通のコメント

/* この書き方もできる */

/// これはドキュメントコメント。ドキュメントライブラリに使用される(便利そう)

// インポートの指定はstr型なので注意
// core libraries(組み込み？)のインポート
import 'dart:math';

// 外部パッケージのインポート
import 'package:test/test.dart';

// ファイルからインポート
import 'path/to/my_other_file.dart';

// クラスの例
class Spacecraft {
  // properties
  String name;
  DateTime? launchDate;
  // Read-only non-final property. 凄くスマート……
  int? get launchYear => launchDate?.year;

  // メンバーへの代入のための構文シュガーを持つコンストラクター(?)
  Spacecraft(this.name, this.launchDate) {
    // Initialization code goes here.
  }

  // デフォルトのコンストラクターに転送する名前付きコンストラクター(?)
  Spacecraft.unlaunched(String name) : this(name, null);

  // メソッド
  void describe() {
    print('Spacecraft: $name');
    // Type promotion doesn't work on getters.
    var launchDate = this.launchDate;
    if (launchDate != null) {
      int years = DateTime.now().difference(launchDate).inDays ~/ 365;
      print('Launched: $launchYear ($years years ago)');
    } else {
      print('Unlaunched');
    }
  }
}

// クラスを使う時:
var voyager = Spacecraft('Hoge Taro', DateTime(2023, 2, 20));
voyager.describe();

var voyager3 = Spacecraft.unlaunched('Hoge Saburo');
voyager3.describe();

// Enums
// https://dart.dev/samples#enums
// enum HogeFamily { taro, jiro, saburo }

// 継承(Inheritance)
class Orbiter extends Spacecraft {
  double altitude;

  Orbiter(super.name, DateTime super.launchDate, this.altitude);
}

// mixin: 複数のクラス階層でコードを再利用する方法(?)
mixin Piloted {
  int astronauts = 1;

  void describeCrew() {
    print('Number of astronauts: $astronauts');
  }
}

// mixinを使う:
class PilotedCraft extends Spacecraft with Piloted {
  // ···
}

// インターフェース
// Dartにはinterfaceキーワードがない代わりに、クラスが暗黙的にinterfaceを定義できる
// (classなら大体interfaceにできるってこと)
class MockSpaceship implements Spacecraft {
  // ···
}

// 抽象クラス
abstract class Describable {
  void describe();

  void describeWithEmphasis() {
    print('=========');
    describe();
    print('=========');
  }
}

// 非同期関数
const oneSecond = Duration(seconds: 1);
// ···
Future<void> printWithDelay(String message) async {
  await Future.delayed(oneSecond);
  print(message);
}

// 上のコードはこれと同じ:
Future<void> printWithDelay(String message) {
  return Future.delayed(oneSecond).then((_) {
    print(message);
  });
}

// 非同期関数を使うことで読みやすくなる例:
Future<void> createDescriptions(Iterable<String> objects) async {
  for (final object in objects) {
    try {
      var file = File('$object.txt');
      if (await file.exists()) {
        var modified = await file.lastModified();
        print(
            'File for $object already exists. It was modified on $modified.');
        continue;
      }
      await file.create();
      await file.writeAsString('Start describing $object in this file.');
    } on IOException catch (e) {
      print('Cannot create description for $object: $e');
    }
  }
}

// async* も使える
Stream<String> report(Spacecraft craft, Iterable<String> objects) async* {
  for (final object in objects) {
    await Future.delayed(oneSecond);
    yield '${craft.name} flies by $object';
  }
}

// 例外を投げる
if (astronauts == 0) {
  throw StateError('No astronauts.');
}

// エラーハンドリング
Future<void> describeFlybyObjects(List<String> flybyObjects) async {
  try {
    for (final object in flybyObjects) {
      var description = await File('$object.txt').readAsString();
      print(description);
    }
  } on IOException catch (e) {
    print('Could not describe object: $e');
  } finally {
    flybyObjects.clear();
  }
}
