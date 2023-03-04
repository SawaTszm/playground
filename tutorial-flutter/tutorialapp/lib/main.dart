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
              colorScheme:
                  ColorScheme.fromSeed(seedColor: Colors.deepPurpleAccent)),
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

  // "WordPair"型(それ以外はエラーになる)
  var favorites = <WordPair>[];

  void toggleFavorite() {
    if (favorites.contains(current)) {
      favorites.remove(current);
    } else {
      favorites.add(current);
    }
    notifyListeners();
  }
}

class MyHomePage extends StatelessWidget {
  // すべてのウィジェットはbuild()メソッドを定義し、ウィジェットの状況が変わるたびに自動的に呼び出されるため、ウィジェットは常に最新の状態に保たれます。
  @override
  Widget build(BuildContext context) {
    // MyHomePageでは、watchメソッドを使ってアプリの現在の状態の変化を追跡します。
    var appState = context.watch<MyAppState>();
    var pair = appState.current;

    IconData favoriteIcon;
    if (appState.favorites.contains(pair)) {
      favoriteIcon = Icons.favorite;
    } else {
      favoriteIcon = Icons.favorite_border;
    }

    // すべてのビルドメソッドは、ウィジェットまたは（より一般的には）ウィジェットのネストされたツリーを返す必要があります。
    // この場合、トップレベルのウィジェットはScaffoldです。このコードラボではScaffoldを使うことはありませんが、便利なウィジェットで、実際のFlutterアプリの大半に搭載されているものです。
    return Scaffold(
      // ColumnはFlutterで最も基本的なレイアウトウィジェットの1つです。
      // 任意の数の子ウィジェットを受け取り、上から下へ列を作ることができます。
      // デフォルトでは、カラムは視覚的に子を一番上に配置します。すぐにこれを変更して、カラムが中央に配置されるようにします。
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // この2番目のテキスト・ウィジェットは、appStateを受け取り、そのクラスの唯一のメンバーであるcurrent（これはWordPairです）にアクセスします。
            // WordPairは、asPascalCaseやasSnakeCaseなど、便利なゲッターをいくつか提供しています。ここではasLowerCaseを使用していますが、他の選択肢を好むのであれば、今すぐ変更できます。
            BigCard(pair: pair),
            SizedBox(height: 10), // 大体隙間(margin)を取るために使われるWidget
            Row(
              mainAxisSize:
                  MainAxisSize.min, // 真ん中にする(普通にmainAxisAlignment使ってもいい)
              children: [
                ElevatedButton.icon(
                  onPressed: appState.toggleFavorite,
                  icon: Icon(favoriteIcon),
                  label: Text("いいね!"),
                ),
                SizedBox(width: 10),
                ElevatedButton(
                    onPressed: () {
                      appState.getNext();
                    },
                    child: Text("次へ")),
              ],
            )
            // Flutterのコードがいかに末尾のカンマを多用しているかに注目してください。なぜならchildrenはこの特定のColumnパラメータリストの最後の（そして唯一の）メンバーだからです。
            // しかし、一般的に末尾のカンマを使うのは良い考えです。メンバーを増やすのが簡単になりますし、Dartの自動整形がそこに改行を入れるようにするヒントにもなります。詳細は、「コードの書式設定」を参照してください。
          ],
        ),
      ),
    );
  }
}

// Text(pair: pair);の行にカーソルを合わせた状態で⌘. → Extract Widget、BigCardとtypeしてEnter でWidgetとして抽出できる
// StatelessWidgetのところにカーソルを合わせて⌘.したら、convert StatefulWidget もできる。sugeeee
class BigCard extends StatelessWidget {
  const BigCard({
    super.key,
    required this.pair,
  });

  final WordPair pair;

  @override
  Widget build(BuildContext context) {
    // 現在のテーマをthemeに保存
    var theme = Theme.of(context);
    // theme.textThemeにアクセスすることでアプリのフォントテーマにアクセスできる
    // nullを許容してる変数(TextStyle?: displayMedium)をCasting away nullabilityするための"bank operator"が"!"
    // (displayMedium as TextStyle)と同義。
    // copyWith: 定義した変更を加えたTextStyleを返す。
    // ⌘⇧spaceで、関数の引数として渡せる値の完全なリストが見られる(!)
    var style = theme.textTheme.displayMedium!.copyWith(
      color: theme.colorScheme.onPrimary,
    );

    // 注：Flutterでは、できる限り継承ではなく、合成を使います。ここでは、paddingがTextの属性である代わりに、ウィジェットになっているのです。
    // こうすることで、ウィジェットはその1つの責任に集中でき、開発者はUIをどのように構成するか、完全に自由にできるようになります。
    // 例えば、Paddingウィジェットを使って、テキスト、画像、ボタン、独自のカスタムウィジェット、またはアプリ全体をパッド化することができます。ウィジェットは、何を包んでいるかは気にしません。
    return Card(
      // 現在のテーマのcolorSchemeに沿って色を決定する(primary: メインカラー)
      color: theme.colorScheme.primary,
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Text(
          pair.asLowerCase,
          style: style,
          // スクリーンリーダー用とかに読み上げやすいPascalCaseにする
          semanticsLabel: pair.asPascalCase,
        ),
      ),
    );
  }
}

// 次、Theme and style から
