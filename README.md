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
- [x] 拗音対応
- [x] 促音対応
- [ ] ピッチ対応
  - https://masarakki.github.io/blog/2012/10/07/make-yukkuri-to-use-accent/
  - イントネーションと Hz(https://www.jpf.go.jp/j/project/japanese/archive/globe/07/08.pdf)
  - 音階と Hz(https://tomari.org/main/java/oto.html)
    - 60Hz で一度くらい?
- [ ] ブレス対応
  ```
  <notations>
  <articulations>
    <breath-mark/>
    </articulations>
  </notations>
  ```
