# CI 練習專案

一個用來練習 **測試 + GitHub Actions CI** 的小型 Python 專案。

## 專案結構

```
.
├── app/
│   ├── __init__.py          # 讓 app 成為一個 Python 套件
│   └── calculator.py        # 要被測試的程式碼
├── tests/
│   └── test_calculator.py   # pytest 測試
├── .github/workflows/
│   └── ci.yml               # GitHub Actions 設定：每次 push / PR 自動跑測試
├── pytest.ini               # pytest 設定
├── requirements-dev.txt     # 開發用套件（pytest）
└── .gitignore               # 不要上傳到 Git 的檔案
```

## 在本機執行測試

```bash
pip install -r requirements-dev.txt
pytest -v
```

## 推上 GitHub

1. 到 https://github.com/new 建立一個新的 repo（例如 `ci-practice`），**不要**勾選加入 README。
2. 在這個資料夾執行：

```bash
git init
git add .
git commit -m "Initial commit: calculator with tests and CI"
git branch -M main
git remote add origin https://github.com/<你的帳號>/ci-practice.git
git push -u origin main
```

3. 打開 repo 的 **Actions** 分頁，應該會看到 CI 正在執行，三個 Python 版本都變綠色 ✅ 就成功了。

## 下一步練習：讓 CI 抓到 bug

1. 開一個新分支：`git checkout -b break-something`
2. 故意改壞程式，例如把 `add` 改成 `return a - b`
3. commit 並 push，然後在 GitHub 上開 Pull Request
4. 觀察 PR 頁面底部的檢查結果變成紅色 ❌，點進去看是哪個測試失敗
