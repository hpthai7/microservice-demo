mongo <<EOF
var user = '$MONGO_INITDB_ROOT_USERNAME';
var passwd = '$MONGO_INITDB_ROOT_PASSWORD';
var admin = db.getSiblingDB('admin');
admin.auth(user, passwd);
var xpmdb = db.getSiblingDB('testdb');
xpmdb.createCollection('users');
xpmdb.createUser({user:'tester', pwd:'tester!2020', roles: [{role:'readWrite', db: 'testdb'}]});
EOF
