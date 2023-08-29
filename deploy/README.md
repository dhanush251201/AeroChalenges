# webhunt
```shell
gunicorn -c conf.py webhunt:app --reload --daemon
```

# insepct
```shell
gunicorn -c conf.py inspect:app --reload --daemon
```

# GuardianFlight
```shell
gunicorn -c conf.py guardian:app --reload --daemon
```

# SQLI
```shell
gunicorn -c conf.py app:app --reload --daemon
```

<!-- /home/gms/aerovision-challenge-websites/deploy -->