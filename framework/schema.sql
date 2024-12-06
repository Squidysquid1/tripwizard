PRAGMA foreign_keys = 1;

-- We didn't end up using this, but this was written by Jason

DROP TABLE IF EXISTS `City`;
CREATE TABLE `City` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255),
  country VARCHAR(255) -- Could make country a separate table
);
