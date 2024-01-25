import datetime
today = datetime.datetime.now()
str_s = str(today)
eval(str_s)
repr_s = repr(today)
t = eval(repr_s)
type(t)