b <- read_excel("Chapter 5.xlsx", col_names = FALSE, col_types = "text",
                sheet = 1,range = cell_cols("B"))
library(readxl)
for (i in 2:12) {
  a <- read_excel("Chapter 5.xlsx", col_names = FALSE, col_types = "text",
                  sheet = i,range = cell_cols("B"))
  b <- rbind(b, a)
  b <- na.omit(b)
}
write.table(b, file = "Dictation Mistakes in Chapter5.txt", sep = "\n", col.names = FALSE, row.names = FALSE, quote = FALSE) 