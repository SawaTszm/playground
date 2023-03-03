import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
        create: (context) => MyAppState(),
        child: MaterialApp(
          title: "Namer App",
          theme: ThemeData(
              useMaterial3: true,
              colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepOrange)),
          home: MyHomePage(),
        ));
  }
}

class MyAppState extends ChangeNotifier {
  var current = WordPair.random();

  void getNext() {
    current = WordPair.random();
    notifyListeners();
  }
}

class MyHomePage extends StatelessWidget {
  // すべてのウィジェットはbuild()メソッドを定義し、ウィジェットの状況が変わるたびに自動的に呼び出されるため、ウィジェットは常に最新の状態に保たれます。
  @override
  Widget build(BuildContext context) {
    // MyHomePageでは、watchメソッドを使ってアプリの現在の状態の変化を追跡します。
    var appState = context.watch<MyAppState>();

    // すべてのビルドメソッドは、ウィジェットまたは（より一般的には）ウィジェットのネストされたツリーを返す必要があります。
    // この場合、トップレベルのウィジェットはScaffoldです。このコードラボではScaffoldを使うことはありませんが、便利なウィジェットで、実際のFlutterアプリの大半に搭載されているものです。
    return Scaffold(
      // ColumnはFlutterで最も基本的なレイアウトウィジェットの1つです。
      // 任意の数の子ウィジェットを受け取り、上から下へ列を作ることができます。
      // デフォルトでは、カラムは視覚的に子を一番上に配置します。すぐにこれを変更して、カラムが中央に配置されるようにします。
      body: Column(
        children: [
          Text("A random AWESOME idea:"),
          // この2番目のテキスト・ウィジェットは、appStateを受け取り、そのクラスの唯一のメンバーであるcurrent（これはWordPairです）にアクセスします。
          // WordPairは、asPascalCaseやasSnakeCaseなど、便利なゲッターをいくつか提供しています。ここではasLowerCaseを使用していますが、他の選択肢を好むのであれば、今すぐ変更できます。
          Text(appState.current.asLowerCase),
          ElevatedButton(
              onPressed: () {
                appState.getNext();
              },
              child: Text("次へ"))
          // Flutterのコードがいかに末尾のカンマを多用しているかに注目してください。なぜならchildrenはこの特定のColumnパラメータリストの最後の（そして唯一の）メンバーだからです。
          // しかし、一般的に末尾のカンマを使うのは良い考えです。メンバーを増やすのが簡単になりますし、Dartの自動整形がそこに改行を入れるようにするヒントにもなります。詳細は、「コードの書式設定」を参照してください。
        ],
      ),
    );
  }
}
