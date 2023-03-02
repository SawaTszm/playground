import 'package:flutter/material.dart';

class Product {
  const Product({required this.name});

  final String name;
}

typedef CartChangedCallback = Function(Product product, bool inCart);

class ShoppingListItem extends StatelessWidget {
  ShoppingListItem({
    required this.product,
    required this.inCart,
    required this.onCartChanged,
  }) : super(key: ObjectKey(product));

  final Product product;
  final bool inCart;
  final CartChangedCallback onCartChanged;

  Color _getColor(BuildContext context) {
    // ツリーの異なる部分が異なるテーマを持つことができるため、
    // テーマはBuildContextに依存します。
    // BuildContextは、ビルドが行われる場所を示すため、
    // どのテーマを使用するかを示します。

    return inCart //
        ? Colors.black54
        : Theme.of(context).primaryColor;
  }

  TextStyle? _getTextStyle(BuildContext context) {
    if (!inCart) return null;

    return const TextStyle(
      color: Colors.black54,
      decoration: TextDecoration.lineThrough,
    );
  }

  @override
  Widget build(BuildContext context) {
    return ListTile(
      onTap: () {
        onCartChanged(product, inCart);
      },
      leading: CircleAvatar(
        backgroundColor: _getColor(context),
        child: Text(product.name[0]),
      ),
      title: Text(
        product.name,
        style: _getTextStyle(context),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
      home: Scaffold(
    body: Center(
        child: ShoppingListItem(
      product: const Product(name: "Chips"),
      inCart: true,
      onCartChanged: (product, inCart) {},
    )),
  )));
}

/**(翻訳文章)
 * ShoppingListItem ウィジェットは、ステートレス・ウィジェットの一般的なパターンに従っています。
 * コンストラクタで受け取った値を最終メンバー変数に格納し、build()関数でそれを使用します。
 * たとえば、inCartブール値は、現在のテーマの原色を使用するものと、
 * グレーを使用するものの2つの視覚的な外観を切り替えます。
 *
 * ユーザーがリスト項目をタップしても、ウィジェットはinCartの値を直接変更しません。
 * 代わりに、ウィジェットは親ウィジェットから受け取ったonCartChanged関数を呼び出します。
 * このパターンでは、ウィジェット階層の上位に状態を保存することで、
 * 状態をより長く持続させることができます。
 * 極端な話、runApp()に渡されたウィジェットに格納された状態は、
 * アプリケーションの寿命まで持続します。

 * 親が onCartChanged コールバックを受信すると、親は内部状態を更新し、
 * これをきっかけに親は再構築し、新しい inCart 値を持つ ShoppingListItem の
 * 新しいインスタンスを作成します。
 * 親ウィジェットが再構築されると ShoppingListItem の新しいインスタンスが作成されますが、
 * フレームワークは新しく構築されたウィジェットと以前に構築されたウィジェットを比較し、
 * その差分のみを基礎となる RenderObject に適用するので、この操作は安価です。
 */