<<<<<<< HEAD
# Lumiere
(Run) Starting the app
---------------------

Preferred (works with your current env):

```bash
python3 -m uvicorn app.main:app --reload
```

If you want to use the `uv` project runner, use the included wrapper which forces
the `python3` interpreter so `uv` uses the same site-packages as `python3`:

```bash
bash scripts/run_uv.sh
```

Or run `uv` directly with an explicit interpreter:

```bash
uv --python python3 run fastapi dev app/main.py
```

>>>>>>> 8aa34f4 (first commit)
