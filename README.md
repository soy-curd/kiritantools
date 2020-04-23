## How to use

```
docker build -t kiritan .
sh run.sh
```

```
./NEUTRINO/Run.sh ../score sample1
```

## music xml

- xml
- DOCTYPE
- score-partwise
  - identification # ソフトウェア情報
  - defaults # ページレイアウト、フォント
  - part-list
    - score-part
      - part-name # 楽器、音量
  - part
    - measure # number, width
      - note
        - lyric
          - text

## TODO

- [x] xml 仕様
- [x] python で xml 操作
- [x] 日本語がエンコード
- [x] header が消える
