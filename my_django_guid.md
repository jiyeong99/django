# django guide
## 1. 프로젝트 폴더 생성
```bash
mkdir test-pjt
```

## 2. 가상환경 생성
```bash
python -m venve .venv
ls
```

## 3. 가상환경 활성화
```bash
source .venv/Scripts/activate
```

### 4. 가상환경 종료
```bash
deactivate
```

## 5.. django install
```bash
pip install django==3.2.13
pip list
```
## 6. django 프로젝트 시작
```bash
django-admin startproject <pjt-name> .
ls
```
### migration error
```bash
python manage.py migrate
```

## 7. server 구동
```bash
python manage.py runserver
```
- 종료시 ctrl + break
   