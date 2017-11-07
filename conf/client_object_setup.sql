CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                         name TEXT NOT NULL,
                                                                   path TEXT NOT NULL,
                                                                             hash VARCHAR NOT NULL,
                                                                                          cdate DATETIME NOT NULL,
                                                                                                         mdate DATETIME NOT NULL,
                                                                                                                        SIZE BIGINT UNSIGNED)
