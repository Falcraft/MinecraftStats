import jaydebeapi


class Permissions():
    def __init__(self):
        self.permissions = {}
        conn =  jaydebeapi.connect("org.h2.Driver", "jdbc:h2:./downloads/luckperms-h2", {'user': ""}, "h2_driver-1.4.197.jar",)
        cur = conn.cursor()
        cur.execute("Select * from luckperms_players")
        tmp = cur.fetchall()
        for t in tmp:
            self.permissions[t[0]] = t[2]


    def is_visitor(self, uuid):
        return self.permissions[uuid] == "visiteur" if uuid in self.permissions else True

