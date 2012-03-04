import utils
import secrets

# settings you can modify
local_server_port = 5001

db_name = 'testdb'

mysql_db_user = 'rcos-dabuzz'
mysql_db_password = secrets.mysql_db_password

# automatic settings you probably shouldn't modify
hostname = utils.run_bash('hostname')
is_local = not hostname == 'stonelinks'
