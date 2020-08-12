# my_pelican_website

![github pages](https://github.com/scottyhq/scottyhq.github.io/workflows/github%20pages/badge.svg)

HTML generated on the 'master' branch with every commit

View the actual website: [https://scottyhq.github.io](https://scottyhq.github.io)


### To deploy on local computer
```
git clone https://github.com/scottyhq/scottyhq.github.io.git
cd scottyhq.github.io
conda env create -f environment.yml
conda activate pelican
# Modify content written in markdown in 'content folder'
git commit -a -m ‘updated content’
pelican content -o output -s pelicanconf.py
# preview locally with `pelican --listen` and go to http://localhost:8000
# build with GitHub Actions `git push`
# OR push changes locally to 'master' branch:
ghp-import output
git push git@github.com:scottyhq/scottyhq gh-pages:master
```
