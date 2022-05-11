// $npx ts-node first.ts で実行できる(npx経由でts-nodeを呼び出す)
// TODO: ファイルを分けてエラーを潰す

const personName: string = 'ほげ太郎'

console.log(`Hello, ${personName}!`)

/* 変数 
 * 基本的にconst, letを使う(varは挙動が意図したものにならないことがある)
 */
let hoge: string;  // 違う型のデータを入れるとエラーになる
// hoge = 123;  // TS2322: Type 'number' is not assignable to type 'string'.
let huga = "huga!"  // 型推論でstring型になる
let piyo: any;  // 明示的にanyを指定することもできる
let birthYear: number | string;  // 「どっちでもいいよ(これ以外はエラー)」ができる
let favoriteAnimal: "猫" | "爬虫類"  // 特定の文字列に限定できる
let newBirthYear: number | "平成" | "令和"  // 合わせ技もできる

/* 変数のスコープ
 * const, letは宣言されたブロック内に限定される
 */
for (let i = 0; i < 10; i++) {
    // pass
}
// console.log(i)  // エラーになる

/* プリミティブ型 */

// boolean: pythonと違って空の配列や辞書はtrueになるから気をつけよう
const flag: boolean = true;

console.log(flag.toString());  // "true" or "false"
console.log(String(flag));  // "true" or "false"
console.log(Number(flag));  // 1 or 0

const notEmpty = Boolean("test string");

// number: 64ビットの浮動小数点数。想像する数値(Int/Float)は大体これでおk。正確な計算はdecimal.jsとかを使おう。
// bigint: 桁数制限のない整数。別途設定が必要。あまり使う機会はなさそう？
// 数値計算するときはMathオブジェクトを使う
const cnt: number = 10;

// string: JavaScriptはUTF-16を採用してる(らしい。文字コード何もわからない)
const userName: string = "hoge taro";
const errorLog: string = `エラーが発生しました。
コードを確認してください`;  // バッククオート``なら改行も認識してくれる
const moji: string = "ABCｱｲｳｴｵ㍻";
moji.normalize("NFKC");  // 正規化されて'ABCアイウエオ平成'になる。全角を求めてくるダサいUIを撲滅しよう。

console.log(`userName: ${userName}`);  // 便利！バッククオートを使う
// console.log(i18n`あなたは${userName}さんですね`)

// null と undefined
let favaoriteGame: string | null = null;  // 明示的にnullを許容してから入れる

/* 複合型 */

// 配列
const years: number[] = [2019, 2020, 2021];
years.push(2022);
years.push(2023, 2024);

const animals = ['cat', 'dog'];  // 型が明確であれば定義は省略可能

// タプル: readonlyも設定できるけど、デフォルトは変更可能。
const pet: [string, number] = ["あずき", 2021];
const pets: [string, string] = ["あずき", "あかふく"]  // 固定長の配列としても使える

// 配列からのデータ取り出し
const miso = ["赤味噌", "白味噌", "合わせ味噌"];
const [red, white, mix] = miso;
const [, ...otherRed] = miso;  // 2番目以降の要素の取り出し

// 配列の要素の存在チェック
if (miso.includes("赤味噌")) {
    // 処理
}

// 配列の加工: splice()という謎関数に割とみんな苦しめられてきた(らしい)。値をコピーするスプレッド構文が便利。
const others = ["マヨネーズ", "ケチャップ"];

const seasoning = [...miso.slice(0,2), "醤油", ...others];  // [ '赤味噌', '白味噌', '醤油', 'マヨネーズ', 'ケチャップ' ]
const copy = [...miso];  // スプレッド構文で配列のコピー

// 配列のソート
const numbers = [10, 2, 100];
numbers.sort();  // 10, 100, 2 数値は期待したソートにならない
numbers.sort((a, b) => a - b);  // 2, 10, 100
numbers.sort((a, b) => b - a);  // 100, 10, 2

const petAge = [
    {name: "むぎ", age: 5},
    {name: "ごま", age: 4},
    {name: "あずき", age: 1},
]
petAge.sort((a, b) => a.age - b.age)  // あずき、ごま、むぎ
const sorted = [...petAge].sort((a, b) => a.age - b.age)  // 非破壊にするためにスプレッド構文を組み合わせる

// 複数条件のソート: 総合スコアにする方がわかりやすいかも？
petAge.push({name: "あかふく", age: 1})
function cmpNum(a: number, b: number) {
    return (a < b) ? -1 : (a === b) ? 0 : 1
}
function cmpStr(a: string, b: string) {
    return (a < b) ? -1 : (a === b) ? 0 : 1
}
petAge.sort((a, b) => {
    const ageScore = cmpNum(a.age, b.age);
    const nameScore = cmpStr(a.name, b.name);
    return ageScore * 2 + nameScore;  // age優先でソート
})

// ループ: for ofが良さげ
var hogehugapiyo = ["hoge", "huga", "piyo"];
for (const value of hogehugapiyo) {
    console.log(value);
}
// entries()は出力ターゲットをES2015以上にしないと動作しない(けど便利)
// for (const [i, value] of hogehugapiyo.entries()) {
//     console.log(i, value);
// }

// TODO: iterableとイテレータ

// 読み込み専用の配列もあるけど、ライブラリであんまり使ってない気がする
const a: readonly number[] = [1,2,3];  // 型につける場合
const b = [1,2,3] as const;  // 値やリテラルにつける場合

// オブジェクト: 気軽になとまったデータを扱うときに使う。クラス定義とかはしなくても(一応)使える。
const key = "favorite drink";
const hito = {
    name: "hoge taro",
    favorite: "game",
    "home town": "その辺り",  // キー名に空白文字、マイナスがあるときは""で囲む
    [key]: "coffee"  // キー名に変数を使うときは[]で囲む
}
console.log(hito.name);
console.log(hito[key]);

// JSON
const json = JSON.stringify(hito, null, 2);
const hito2 = JSON.parse(json);  // 複製されて出てくるので、元のhitoとは別物

// オブジェクトからのデータ取り出し
const {name, favorite="walking"} = hito;  // 複数取り出し。デフォルトも設定可能
const {name, ...other} = hito;  // name以外の要素の取り出し。other変数にname以外の者が入る

// TODO: オプショナルチェイニング

// オブジェクトの要素の加工
const attributes = {
    job: "散歩",
    age: 20
}
const merged = {...hito, ...attributes}  // スプレッド構文でマージ

// 辞書用途はオブジェクトではなくてMapを使う(これもES2015以降に導入されたクラス)
const map = new Map<string, string>([
    ["hoge", "foo"],
    ["huga", "bar"],
])
for (const [key,value] of map) {
    console.log(`${key}: ${value}`)
}

// 読み込み専用のオブジェクト
type User = {
    name: string;
    age: number;
}
const u: Readonly<User> = {name: "huga jiro", age: 25}
const u2 = {name: "huga jiro", age: 25} as const;  // こっちでもいい

/* 基本的な構文 */

// 制御構文: if
const task = "";
if (task === "休憩中") {
    console.log("ゲームする");
  } else if (task === "仕事中") {
    console.log("適度な運動をする");
  } else {
    console.log("出勤する");
  }

// 制御構文: switch
switch (task) {
    case "休憩中":
      console.log("ゲームする");
      break;
    case "仕事中":
      console.log("適度な運動をする");
      break;
    default:
      console.log("出勤する");
    }

// 制御構文: for
for (let i = 0; i < 5; i++) {  // letはこのブロック内だけで有効になる
  console.log(i);
}
const array = [1,2,3];
for (const value of array) {
  console.log(value);
}

// TODO: forに使える諸々

// 制御構文: try .. catch
try {
    throw new Error("例外投げる")
} catch (e) {
    console.log(e);
} finally {
    //
}

/* 式: ちょっと戸惑いそうなやつ↓
 * 比較の演算子は===と==がある。前者はstrict,後者は文字列変換を挟んでから比較する。
 * **演算子: x ** yでMath.pow(x, y)と同じ累乗計算を行う。
 */

// 三項演算子: ReactのJSXでもよく使われる
const result = (day === "金曜日") ? "夜更かしする" : "大人しく寝る";

/* 基本的な型付け */

// any
function someFunction(opts: any) {
    console.log(opts.debug); // debugがあるかどうかチェックしないのでエラーにならない
}

// unknown: anyと違って変数を利用する場合には、型アサーションを使ってチェックを行わないとエラーになる

// 型に名前をつける
type Hoge = number | string;
const hoge2: Hoge = "huga!"
function hogePiyo(hoge: Hoge) {
    //
}

type Person = {
    name: string;
    favoriteDrink: string;
    favoriteGame?: string;  // Optional
}
const person: Person = {
    name: "hoge taro",
    favoriteDrink: "coffee"  // 項目がないとエラーになる
}

type Person2 = {
    name: string;
    favorite: string;
}
const p: Partial<Person2> = {name: "huga jiro"}  // 項目を任意にできる
const p2: Readonly<Person2> = {name: "piyo saburo", favorite: "beer"}

// 属性名が可変なオブジェクト
const animal: { [key: string]: string} = {
    "ねこ": "cat",
    "いぬ": "dog",
}

// 型のand(交差型(Intersection Type)とか呼ばれる)
type Twitter = {
    twitterId: string;
}
type Youtube = {
    youtuveId: string;
}
const vtuber: Twitter & Youtube = {
    twitterId: "xxxxxx",
    youtuveId: "xxxxxx",
}

// タグ付き合併型: パラメータの値によって必要な属性が変わる柔軟な型定義
// TODO: CheetahGridライブラリでのJSONでのカラム定義

// 型ガード: typeofやinstanceof, in, 比較などが組み込みで使える
let userNameOrId: string|number = "";

if (typeof userNameOrId === "string") {
    // このブロックではuserNameOrIdはstring型として扱われる
} else {
    // このブロックではuserNameOrIdはnumber型として扱われる
}

// ユーザ定義の型ガード
// eslint-disable-next-line @typescript-eslint/no-explicit-any
function isArray(arg: any): arg is Array {
    return Array.isArray(arg);
}

// 型アサーション: 混乱の元になるので可能な限り使わない
const page: any = { name: "profile page" };
const page2: string = page as string;  // pageをstring型として代入

// keyof: 動的な型宣言
// TODO: よくわかってないのでもう一回見る
type Animal = {
    name: string;
    isAdult: boolean;
};
type Key = keyof Animal;  // name | isAdult が割り当てられる
const key2: Key = "name"  // 指定されたキー以外はエラーになる

// インターフェースを使った型定義
interface Person3 {
    name: string;
    favoriteGame: string;
}

/* 関数
 * 名前がない関数は無名関数、もしくはアノニマス関数と呼ぶ。変数への代入や他関数の引数に入れるために用いられる。
 * オブジェクトに属する関数は「メソッド」と呼ばれる(英語だと呼び分けあるんだろうか……)。
*/

// 関数の引数と返り値の型定義: 変数と同じく、明確な場合は省略も可能
function checkFlag(flag: boolean): string {
    return flag.toString()
}
const normalize = (input: string): string => {  // 無名関数(単純に関数の名前が抜けてるだけ(多分)。"(引数): 返り値の型 => {}")
    return input.toLowerCase();
}
function greeting(): void {  // 返り値ない場合はvoid
    console.log("おはよう");
}

// TODO: 関数を扱う変数の型定義
let check: (arg1: string, arg2: number) => boolean;
// arg2が関数の場合：
let check2: (arg1: string, arg2: (arg3: string) => number) => boolean;

// 関数を扱う変数に、デフォルトで何もしない関数を設定する
let callback: (name: string) => void;  // 変数宣言(わかりやすさのために代入はなし)
callback = (name: string): void => {};  // ダミーの関数を設定

// デフォルト引数
function f(name="爬虫類", favorite="コオロギ") {
    console.log(`${name}は大体${favorite}が好きです`)
}
f();  // デフォルト引数があるので省略して呼べる

// 関数を含むオブジェクトの定義方法
const smallAnimal = {
    getName() {
      return "爬虫類"
    },
    _favorite: "コオロギ",
    get favorite() {
      return this._favorite;
    },
    set favorite(favorite) {
      this._favorite = favorite;
    }
};

// TODO: クロージャとthisとアロー関数
// TODO: 即時実行関数はもう使わない

/* その他の組み込み型・関数 */

// Date: 組み込みがあまり評判が良くなく、追加モジュールが多い。今後置き換えられるかも。
const now = new Date();  // 現在時刻でDateのインスタンス作成
const nowStr = Date();  // newをつけないと文字列として返ってくる
const now2 = Date.now();  // ミリ秒単位のエポック時刻取得
const start = Date.now();  // ...時間のかかる処理...↓
const duration = Date.now() - start;  // 経過時間（ミリ秒）の取得
const d = new Date(2020, 8, 21, 21, 10, 5);  // 2020年9月21日21時10分5秒
const d2 = new Date(Date.UTC(2020, 8, 21, 11, 10, 5))  // UTC基準で

// ここまで書いたけど組み込みなら必要な時に公式のドキュメント読めばいいか
// 他：RegExp(正規表現), JSON, URLとURLSearchParams

/* TODO: クラス(一旦飛ばし) */

/* 非同期処理
 * async/awaitの形が結構主流だよ(コールバック・Promiseを経て)
 */
// TODO: Promise.all()
