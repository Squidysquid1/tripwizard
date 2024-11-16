PRAGMA foreign_keys = 1;

DROP TABLE IF EXISTS `City`;
CREATE TABLE `City` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255),
  country VARCHAR(255) -- Could make country a separate table
);
