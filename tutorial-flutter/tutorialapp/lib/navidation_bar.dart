import 'package:flutter/material.dart';

class MyAppBar extends StatelessWidget {
  const MyAppBar({required this.title, super.key});

  // ウィジェットサブクラスのフィールドは常にfinalとマークされる(?)

  final Widget title;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 56.0, // in lojical pixels
      padding: const EdgeInsets.symmetric(horizontal: 8.0),
      decoration: BoxDecoration(color: Colors.blue[500]),
      // Row is a horizontal, linear layout.
      child: Row(
        children: [
          const IconButton(
            // pubspec.yamlでuses-material-design: trueにしてると使える
            icon: Icon(Icons.menu),
            tooltip: 'Navigation menu',
            onPressed: null, // null disables the button
          ),
          // Expanded expands its child
          // to fill the available space.
          Expanded(
            child: title,
          ),
          const IconButton(
            icon: Icon(Icons.search),
            tooltip: 'Search',
            onPressed: null,
          ),
        ],
      ),
    );
  }
}

class MyScaffold extends StatelessWidget {
  const MyScaffold({super.key});

  @override
  Widget build(BuildContext context) {
    // Material is a conceptual piece
    // of paper on which the UI appears.
    return Material(
      // Column is a vertical, linear layout.
      child: Column(children: [
        MyAppBar(
          title: Text(
            "Example title",
            style: Theme.of(context) //
                .primaryTextTheme
                .titleLarge,
          ),
        ),
        const Expanded(
          child: Center(
            child: Text("Hello, world."),
          ),
        ),
      ]),
    );
  }
}

void main() {
  runApp(
    // MaterialAppを使うかどうかはオプションだけど、公式は推奨してる
    const MaterialApp(
      title: 'My app', // used by the OS task switcher
      home: SafeArea(
        child: MyScaffold(),
      ),
    ),
  );
}
