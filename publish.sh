pelican content -o output -s publishconf.py
ghp-import -b master output
git push origin master
