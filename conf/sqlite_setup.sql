CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           name TEXT NOT NULL,
                                                                     fqdn TEXT NOT NULL,
                                                                               fingerprint TEXT NOT NULL,
                                                                                                ip VARCHAR(16),
                                                                                                   DATABASE varchar(8));


CREATE INDEX IF NOT EXISTS clients_idx ON clients (name,ip,DATABASE);
