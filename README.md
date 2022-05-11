1. set local python version

- `pyenv local 3.10.4`
- check (ternimal)
  - `cat .python-version`

2. virtualenv

- `pyenv virtualenv 3.10.4 python_virtualenv_3.10.4`
- check (ternimal)
  - `pyenv shell python_virtualenv_3.10.4`

3. m1 mac의 경우 soundfile을 읽어 오기위해 libsndfile을 연결해야함

- libsndfile 설치
  - `brew install libsndfile`
- libsndfile python 가상환경에 연결
  - `bash -c "ln -s /opt/homebrew/lib/libsndfile.* /Users/jinwook/.pyenv/versions/python_virtualenv_3.10.4/lib/python3.10/site-packages/_soundfile_data/"`
