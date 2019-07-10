`python-package-template`
===
This repository contains everything you need to make a new Python project that:
- checks against the [Black](https://github.com/python/black) code style
- performs whatever tests you like
- Does testing and format checking in parallel
- has everything needed to make a Python package that can be easily installed with `pip`
- automatically packages itself to PyPI on new tags (or "releases" for those who are still separating `git` from GitHub)
## Setup
After clicking the shiny green "Use this template" button, a few things need to change to get everything going good.
* In `setup.py`
  * The [location of `__init__.py`](https://github.com/homebrew-limelight/python-package-template/blob/master/setup.py#L7)
  * The [package name](https://github.com/homebrew-limelight/python-package-template/blob/master/setup.py#L19)
  * [Your name and email](https://github.com/homebrew-limelight/python-package-template/blob/master/setup.py#L21-L22)
  * The [project short description](https://github.com/homebrew-limelight/python-package-template/blob/master/setup.py#L23), [url](https://github.com/homebrew-limelight/python-package-template/blob/master/setup.py#L26)
  * Optionally (but a very good idea) expand the [list of classifiers.](https://github.com/homebrew-limelight/python-package-template/blob/master/setup.py#L28-L34) You can find all the ones PyPI supports [online.](https://pypi.org/classifiers/)
* In `.travis.yml`
  * Set [your PyPI username and password.](https://github.com/homebrew-limelight/python-package-template/blob/master/.travis.yml#L17-L19) `.travis.yml` has instructions on protecting your password from prying eyes.
  * Add or remove [`script` lines.](https://github.com/homebrew-limelight/python-package-template/blob/master/.travis.yml#L10) Every `script` is called in parallel.
* `LICENSE` - duh
* This file - replace it entirely with your own README!

You'll also need to make sure Travis has access to this repository on the create page:  
![being nice to travis](https://i.imgur.com/JsBakWH.png)

And then you're done! Enjoy your ~~slave labor~~ automatic tests and deployments!
