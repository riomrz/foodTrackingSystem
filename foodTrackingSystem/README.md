*** The public site is reachable from https://mauribtc.eu.pythonanywhere.com/ ***

Tech notes:

A STAFF STATUS ADMIN IS SUPPOSED TO USE THE /foodTrackingSystemAdmin PAGE in order to add new products.
admin/ page is left as default in order to let a superuser to be able to access it.
A user with superuser privileges can access admin/ page with all permissions, while a user with staff status can access only the foodTrackingSystemAdmin/ page and add products.

*** IF the Redis server is down the app will show an error page at /foodTrackingSystemAdmin ***