# Howto release PyWPS

This document gives you, as PyWPS release master complete tutorial of how to get
PyWPS release rolled up and deployed to target server, create packages etc.

## PyWPS versioning

PyWPS uses [Debian version naming system](https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version). Every policy should be checked against it.

PyWPS uses 3 numbers release description: MAJOR.MINOR.MAINTENANCE. Within MAJOR
releases, we should aim, not to break backwards compatibility.

Event MINOR version numbers (0, 2, 4, 6, ...) are considered as stable, where as
odd numbers (1, 3, 5, 7, ...) are current development branches. MINOR releases
should add new features.

MAINTENANCE number should be used for bugfix releases only. No new features are
added.

For release candindates `MAJOR.MINOR.MAINTENANCE-rcX` format should be used.

## Go to `master` branch

```
git checkout master
```
## Fix files, create tags, commit, push

* Fix the [VERSION.txt](https://github.com/geopython/pywps/blob/master/VERSION.txt) file.
* Fix the [pywps/__init__.py](https://github.com/geopython/pywps/blob/master/pywps/__init__.py) file `__version__` attribute
* Fix the [debian/changelog](https://github.com/geopython/pywps/blob/master/debian/changelog) file

```
git commit -m"Creating new release of PYWPS X.Y.Z[-rcX] fixes" -a
```

* Create tag in PyWPS main source tree

```
git tag X.Y.Z[-rcX]
git push
git push --tags
```

* Update version in `VERSION.txt` and `pywps/__init__.py` to dev branch, e.g.
`4.1-dev` and push to master:

```
git checkout master
$EDITOR VERSION.txt pywps/__init__.py # add 4.1-dev version
git commit -m"Updating version to 4.1-dev"
git push
```

### Send PyWPS to http://pypi.python.org repository (only for stable releases)

```
cd /tmp
git clone git@github.com:geopython/pywps.git pywps-4
cd pywps-4
git checkout X.Y.Z
python setup.py bdist_egg upload
```

## Fix pywps-demo project (only for stable releases)

```
git checkout master
```
* Fix the [VERSION.txt](https://github.com/geopython/pywps-demo/blob/master/VERSION.txt) file.

```
$EDITOR VERSION.txt
git commit -m"Creating new release of PYWPS X.Y.Z fixes #TICKET_NUMBER" -a
git push
```

* Add tag, once pull request is accepted

```
git tag X.Y.Z
git push --tags
```

## Fix web pages && write to mailing list

```
PyWPS [X.Y.Z]
#############

The PyWPS Development team announces the release of PyWPS X.Y.Z.

Features of this version:
 - [SHOULD COPY THIS FROM Changelog]

To download this version, please follow the link below [2].

NOTE: [IF ANY]

What is PyWPS:
--------------

PyWPS (Python Web Processing Service) is implementation of Web
Processing Service standard from Open Geospatial Consortium (OGC(R)). 
Processes can be written using GRASS GIS, but usage of other programs, like
R package, GDAL or PROJ tools, is possible as well.

Happy GISing!

PyWPS Development team

[1] http://pywps.org
[2] http://pywps.org/download
```