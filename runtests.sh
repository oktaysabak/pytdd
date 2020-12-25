echo "Discovering tests..."
coverage run -m unittest discover
sleep 1
echo "Reporting tests..."
coverage report -m --skip-empty
sleep 1
echo "Report created. check htmlcov/index.html"
coverage html --skip-empty
