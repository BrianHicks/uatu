# UATU

Put this in your pipe (`uatu.yaml`):

```yaml
test:
  watch: .+\.py
  transform: tests/%s
  command: nosetests
```

and smoke it:

`$ uatu`

Or, slightly more advanced:

```yaml
test:
  watch: (?P<path>.+)/(?P<file>.+)\.py
  transform: %(path)s/tests/%(file)s_tests.py
  command: nosetests

lint:
  watch: .+\.py
  command: pylint -r n
```

If you get *really* crazy, specify `transform_command`. Your command
should accept the filename from STDIN and output the transformed
filename to STDOUT. Examples to come.

## Q&A:

 - WTF? There's no code here!

   Yeah, pretty much. Watch the repo or something. The first legit
   release I'll push out to pypi.

## Contributing:

In case you go crazy and want to contribute to a project with no code
(IE this one), I'm using git flow, and you probably should too, since
releases are going to be fairly infrequent but hopefully stable. If you
don't want to, just make topic branches off `develop`. Either way, make
a pull request for your feature/whatever branch, and I'll merge it.

([About the Name](http://en.wikipedia.org/wiki/Uatu)) (because every
open-source project needs a colorful name.)
