# cmdblog-backend

## Contribution

このrepositoryへの修正は以下の流れで行います。

0. `gh repo fork cmdblog/cmdblog-backend`でこのrepositoryをforkする (初回のみ)
1. `git checkout main` or `git switch main`でmainブランチに移動する
2. `git fetch upstream`でlocalのupstreamを更新する
3. `git rebase upstream/main`で、最新のupstream/mainをlocalのmainブランチに取り込む
4. `git checkout -b <わかりやすいブランチ名>` or `git switch -c <わかりやすいブランチ名>` で機能用ブランチを切る
5. コードに修正を加え、必要ならばテストを付け、`git commit` `git push` する
6. 本repositoryへのPRを作成し、reviewを受ける
7. approveされた後、PR作成者(or 誰でもいい)がmergeボタンを押す
8. PR画面からremoteの機能用ブランチを消す
9. `git cehckout main` or `git switch main`でmainブランチに戻り、`git fetch --prune` `git fetch -D <当該ブランチ名>` で、機能用ブランチを削除する
