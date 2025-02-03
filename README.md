![img](doc/img/img.png)

# Background
This repo is a quick Python implementation of the
['Pataphysical calendar](https://en.wikipedia.org/wiki/'Pataphysics#Pataphysical_calendar).

It comes with a small Streamlit app so you can convert dates between vulgate (Gregorian) and 'Pataphysical, and vice-versa.

# Quickstart


## Streamlit app
uv
```
uv pip install requirements.txt
uv run streamlit run app.py
```

pip
```
python -m venv .venv
source .venv/bin/activate
pip install requirements.txt
streamlit run app.py
```


## Python
```
>>> from cal import PataphysicalDate
>>> from datetime import date
>>> d = date.today()
>>> d
datetime.date(2025, 2, 2)
>>> pd = PataphysicalDate.from_vulgate(d)
>>> pd
Sunday 8 Gueules 152
>>> pd2 = PataphysicalDate.from_str('8 Gueules 152')
>>> pd2
Sunday 8 Gueules 152
>>> pd2.date_vulg
datetime.date(2025, 2, 2)
```




