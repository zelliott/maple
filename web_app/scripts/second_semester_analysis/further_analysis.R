library(dplyr)

tbl <- read.table("results.csv", sep=",")
data <- tbl_df(tbl)
colnames(data) <- c("id", "topic", "accuracy", "difficulty", "time", "length", "groupId", "testId")

# results <- data %>% group_by(topic) %>% summarise(
#   avglength = mean(length),
#   avgaccuracy = mean(accuracy),
#   avgdifficulty = mean(difficulty))

# results <- data %>% group_by(accuracy) %>% summarise(
#   avgdifficulty = mean(difficulty),
#   avglength = mean(length))

results <- data %>% group_by_(.dots=c("testId"))%>% summarize(
    avgaccuracy = mean(accuracy),
    avgdifficulty = mean(difficulty)
)

print(results, n=380)