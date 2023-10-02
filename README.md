# adap-autotest-android
pip3 install --upgrade pip
pip install -r requirements.txt
pytest  test_authorization.py  -s -v --html=reports\report.html --capture=tee-sys
xcrun xctrace list devices get uid of iphone
