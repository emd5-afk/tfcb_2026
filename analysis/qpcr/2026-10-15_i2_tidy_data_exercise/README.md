# Tidy the Lecture 3 qPCR data

The two qPCR plate layouts were combined into a tidy table with one row per
well of one plate. The original Cq measurements and well annotations were
transcribed without calculating or filtering values; the workbook's note for
well F07 on plate 7 is retained in the `note` column.

The table was prepared with Python 3.12.3 using its standard-library
`zipfile`, `xml.etree.ElementTree`, and `csv` modules.

## Changelog

- 2026-10-15: Added the tidy table for plates 4 and 7.
