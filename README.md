# file-cleanup-days-ago

If have a directory with files of the form `filename - yyyy-mm-dd`, delete files older than 3 days.

### Requirements

* [arrow](https://pypi.python.org/pypi/arrow)

### Future

Should turn into an actual script using [click](http://click.pocoo.org) where the user can pass in the regular expression to utilize for filename / date searches as well as pass in the # of days prior to trigger a delete.