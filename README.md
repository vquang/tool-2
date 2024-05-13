
# HƯỚNG DẪN CÀI ĐẶT THƯ VIỆN VÀ CHẠY TOOL 2

## Mô tả công cụ
Là một công cụ giúp rà quét mã độc và phát hiện xâm nhập dựa trên phân tích log bằng học máy bên phía máy chủ web server.

## Cài đặt các công cụ tích hợp

Cài đặt công cụ: curl:

```bash
  sudo apt install curl
```

Cài đặt framework nodejs:

```bash
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  nvm install 20
  node -v
  npm -v
```

## Cài đặt các thư viện cho python

Cài đặt thư viện flask, numpy, pandas, scikit-learn và yara-python:

```bash
  pip install Flask numpy pandas scikit-learn yara-python
```

## Chạy tool

Tại thư mục tool-2, chạy file sau:

```bash
  ./run.sh
```
