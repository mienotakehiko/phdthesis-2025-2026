Code4-L.spthy の実行方法

1. Code4-M.py を、拡張子なしの myoracle というファイル名に変更する
2. Code4-L.spthy と同じディレクトリに Code4-L.spthyを置く
3. --heuristic=o のオプションを付与して実行

実行コード)
tamarin-prover --prove --heuristic=o --oraclename=myoracle code4-L.spthy


参考)
diff を付与する場合は、下記
tamarin-prover --prove --diff --heuristic=o --oraclename=myoracle code4-L.spthy