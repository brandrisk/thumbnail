Build

`python -m build`

Install

`pip install dist/thumbnail-0.2-py2.py3-none-any.whl`

Get image size

```
python -m thumbnail getsize --fp image.png

> 1920 x 1280
```

Make thumbnail

```
python -m thumbnail make --fp image.png --sizes 100,200,300

> image-100.png saved
> image-200.png saved
> image-300.png saved
```
