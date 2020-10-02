source ~/.profile
echo "Creating new database..."
cd static
cat new_dev_db_test.sql | mysql -u root -p"$ROOT_PASS"
echo "Enforcing schema..."
cd ../
python3 manage.py migrate db
echo "Populating....."
python3 -m pdb -c c manage.py populate_db --collection Eng-NA
